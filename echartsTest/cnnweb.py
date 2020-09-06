#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/10 8:30
# @Author: hdq
# @File  : cnnweb.py
import tensorflow as tf
import os

def create_variable(shape, stddev=0.01):
    return tf.Variable(tf.random_normal(shape=shape, stddev=stddev))


# x表示id的数据为,
# x=tf.placeholder(tf.float32,shape=[None,20,80,3])
# 元素格式
# y_true =tf.placeholder(tf.int32,shape=[None,4*26])
#  y_predict=create_cnn_model(x)
def create_cnn_model(x, picweight, picheight, inputchannel, recognizenum, type, filter=None, ride= None, outputchannel=None,keep_prob=None,middlechannel=1024):
    # 卷积层
    if not outputchannel:
        outputchannel=[32,64]
    if not filter:
        filter=[5,5]
    if not ride:
        ride=[2,2]

    # 5*5的filter 通道数 输出通道数
    conv1_weights = create_variable([filter[0], filter[0], inputchannel, outputchannel[0]])
    conv1_bias = create_variable([outputchannel[0]])
    conv1_tensor = tf.nn.conv2d(input=x, filter=conv1_weights, strides=[1, 1, 1, 1], padding="SAME") + conv1_bias
    # 激活层
    relu1_x = tf.nn.relu(conv1_tensor)
    # 池化层
    pool1_x = tf.nn.max_pool(value=relu1_x, ksize=[1, 2, 2, 1], strides=[1, ride[0], ride[0], 1], padding="SAME")
    inputw = picweight / ride[0]
    inputh = picheight / ride[0]

    pool2_x=pool1_x
    for i in range(len(outputchannel)-1):
        # 卷积大层 20*80*inputchannel-> 10*40*outputchannel1
        conv2_weights = create_variable([filter[i+1], filter[i+1], outputchannel[i], outputchannel[i+1]])
        conv2_bias = create_variable([outputchannel[i+1]])
        con2_tensor = tf.nn.conv2d(input=pool2_x, filter=conv2_weights, strides=[1, 1, 1, 1], padding="SAME") + conv2_bias
        # 激活层
        relu2_x = tf.nn.relu(con2_tensor)
        # 池化层
        pool2_x = tf.nn.max_pool(value=relu2_x, ksize=[1, 2, 2, 1], strides=[1, ride[i+1], ride[i+1], 1], padding="SAME")

        inputw = int(inputw / ride[i+1])
        inputh = int(inputh / ride[i+1])


    if keep_prob:
        '''第一全连接层的权重和偏置'''
        x_fc = tf.reshape(pool2_x, shape=[-1, inputw * inputh * outputchannel[len(outputchannel) - 1]])
        weights_fc = create_variable([inputw * inputh * outputchannel[len(outputchannel) - 1], middlechannel])
        bias_fc = create_variable([middlechannel])
        h_fc = tf.nn.relu(tf.matmul(x_fc, weights_fc) + bias_fc)
        h_fc_drop = tf.nn.dropout(h_fc, keep_prob)
        '''第二全连接层的权重和偏置'''
        w_fc2 = create_variable([middlechannel,recognizenum * type])
        b_fc2 = create_variable([recognizenum * type])
        y_predict=tf.matmul(h_fc_drop, w_fc2) + b_fc2
    else:
        # 全连接层 28*28/ride(2)->14*14
        x_fc = tf.reshape(pool2_x, shape=[-1, inputw * inputh * outputchannel[len(outputchannel) - 1]])
        weights_fc = create_variable([inputw * inputh * outputchannel[len(outputchannel) - 1], recognizenum * type])
        bias_fc = create_variable([recognizenum * type])
        y_predict = tf.matmul(x_fc, weights_fc) + bias_fc

    return y_predict




def start_cnn_train_model(imagevalue, labelnplist, recognizenum, type, width, height, model, channel=3,
                          learningrate=0.01,
                          learingtimes=100,
                          outputchannel=None,
                          adamoptimizer=True,
                          filter=None,
                          ride=None,
                          signmoid=True,
                          readmodel=False,
                          reset=True,
                          notexistsavemodel=True,
                          savemodel=False,
                          keep_prob=None,
                          middlechannel=1024
                          ):
    if not outputchannel:
        outputchannel=[32,64]
    if not filter:
        filter=[5,5]
    if not ride:
        ride=[2,2]

    # 准备输入数据
    x = tf.placeholder(tf.float32, shape=[None, height, width, channel])
    y_true = tf.placeholder(tf.float32, shape=[None, recognizenum * type])
    keep_probtf=None
    if(keep_prob):
        keep_probtf = tf.placeholder(tf.float32)
    y_predict = create_cnn_model(x, width, height, channel, recognizenum, type, outputchannel=outputchannel,
                                 filter=filter,ride=ride,keep_prob=keep_prob,middlechannel=middlechannel)

    # 构造损失函数
    if(signmoid):
        loss_list = tf.nn.sigmoid_cross_entropy_with_logits(labels=y_true, logits=y_predict)
    else: loss_list = tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict)
    loss = tf.reduce_mean(loss_list)

    # 优化损失
    optimizer = None
    if adamoptimizer:
        optimizer = tf.train.AdamOptimizer(learningrate).minimize(loss)
    else:
        optimizer = tf.train.GradientDescentOptimizer(learningrate).minimize(loss)

    # 准确率
    equal_list = tf.reduce_all(
        tf.equal(tf.argmax(tf.reshape(y_predict, shape=[-1, recognizenum, type]),axis=2),
                 tf.argmax(tf.reshape(y_true, shape=[-1, recognizenum, type]),axis=2)),axis=1)
    accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))
    run_web(imagevalue, labelnplist, recognizenum, type, model, optimizer, loss, accuracy, y_true, x, learingtimes,keep_prob,keep_probtf,readmodel,reset,notexistsavemodel,savemodel)
    return recognizenum, type, model, optimizer, loss, accuracy, y_true, x, learingtimes,keep_prob,keep_probtf


def run_web(imagevalue, labelnplist, recognizenum, type, model, optimizer, loss, accuracy, y_true, x,
                           learingtimes,keep_prob=None,keep_probtf=None, readmodel=False, reset=True,notexistsavemodel=True,savemodel=False):
    # 初始化变量
    init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
    # 开启会话
    with tf.Session() as sess:
        sess.run(init)
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        if (readmodel):
            tf.train.Saver().restore(sess, model)
        labels_result = tf.reshape(tf.one_hot(labelnplist, depth=type), [-1, recognizenum * type]).eval()
        # print(labels_result)
        for two in range(learingtimes):
            if not keep_prob:
                _, error, acc = sess.run([optimizer, loss, accuracy], feed_dict={x: imagevalue, y_true: labels_result})
            else:
                _, error, acc = sess.run([optimizer, loss, accuracy], feed_dict={x: imagevalue, y_true: labels_result,keep_probtf:keep_prob})
            print("第%d次训练 损失:%f 准确率:%f" % (two + 1, error, acc))
        if not savemodel:
            if not (os.path.exists(os.getcwd()+"/"+model)):
                if (notexistsavemodel):
                    save_model(model, sess)
        else:
            save_model(model, sess)
        coord.request_stop()
        coord.join(threads)
    if (reset):
        tf.reset_default_graph()



def start_cnn_train_model_with_point(imagevalue, labelnplist, recognizenum, type, width, height, model, channel=3,
                          learningrate=0.01,
                          pacc=1.0,
                          ploss=0.01,
                          outputchannel=None,
                          adamoptimizer=True,
                          filter=None,
                          ride=None,
                          signmoid=True,
                          readmodel=False,
                          reset=True,
                          notexistsavemodel=True,
                          savemodel=False,
                          keep_prob=None,
                          middlechannel=1024
                          ):
    if not outputchannel:
        outputchannel=[32,64]
    if not filter:
        filter=[5,5]
    if not ride:
        ride=[2,2]
    # 准备输入数据
    x = tf.placeholder(tf.float32, shape=[None, height, width, channel])
    y_true = tf.placeholder(tf.float32, shape=[None, recognizenum * type])

    keep_probtf = None
    if (keep_prob):
        keep_probtf = tf.placeholder(tf.float32)
    y_predict = create_cnn_model(x, width, height, channel, recognizenum, type, outputchannel=outputchannel,
                                 filter=filter, ride=ride, keep_prob=keep_prob, middlechannel=middlechannel)

    # 构造损失函数
    if(signmoid):
        loss_list = tf.nn.sigmoid_cross_entropy_with_logits(labels=y_true, logits=y_predict)
    else: loss_list = tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict)
    loss = tf.reduce_mean(loss_list)

    # 优化损失
    if adamoptimizer:
        optimizer = tf.train.AdamOptimizer(learningrate).minimize(loss)
    else:
        optimizer = tf.train.GradientDescentOptimizer(learningrate).minimize(loss)

    # 准确率
    equal_list = tf.reduce_all(
        tf.equal(tf.argmax(tf.reshape(y_predict, shape=[-1, recognizenum, type]),axis=2),
                 tf.argmax(tf.reshape(y_true, shape=[-1, recognizenum, type]),axis=2)),axis=1)
    accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))
    run_web_with_point(imagevalue,labelnplist, recognizenum, type,model,optimizer, loss, accuracy,y_true,x,pacc,ploss,keep_prob,keep_probtf,readmodel,reset,notexistsavemodel,savemodel)
    return recognizenum, type,model,optimizer, loss, accuracy,y_true,x,pacc,ploss,keep_prob,keep_probtf


def run_web_with_point(imagevalue,labelnplist, recognizenum, type,model,optimizer, loss, accuracy,y_true,x,pacc=1.0,ploss=0.01,keep_prob=None,keep_probtf=None,readmodel=True,reset=True,notexistsavemodel=True,savemodel=False):
    # 初始化变量
    init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
    # 开启会话
    with tf.Session() as sess:
        sess.run(init)
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        if readmodel:
            tf.train.Saver().restore(sess,model)
        labels_result = tf.reshape(tf.one_hot(labelnplist, depth=type), [-1, recognizenum * type]).eval()
        # print(labels_result)
        two=0
        acc=0.0
        error=1.0
        while(pacc>acc or ploss<error):
            if not keep_prob:
                _, error, acc = sess.run([optimizer, loss, accuracy], feed_dict={x: imagevalue, y_true: labels_result})
            else:
                _, error, acc = sess.run([optimizer, loss, accuracy], feed_dict={x: imagevalue, y_true: labels_result,keep_probtf:keep_prob})
            print("第%d次训练 损失:%f 准确率:%f" % (two + 1, error, acc))
            two+=1
        if not savemodel:
            if not (os.path.exists(os.getcwd()+"/"+model)):
                if(notexistsavemodel):
                    save_model(model, sess)
        else:
            save_model(model, sess)
        coord.request_stop()
        coord.join(threads)
    if(reset):
        tf.reset_default_graph()


def save_model(dirpath, sess):
    tf.train.Saver().save(sess, save_path=dirpath)

def save_model_without_sess(dirpath):
    with tf.Session() as sess:
        tf.train.Saver().save(sess, save_path=dirpath)


def load_model(dirpath, sess):
    tf.train.Saver().restore(sess, save_path=dirpath)



def predict_info_with_point(imagevalue,labelnplist, recognizenum, type,model,optimizer, loss, accuracy,y_true,x,pacc=1.0,ploss=0.01,keep_prob=None,keep_probtf=None,bestacc=0.0,readmodel=True,reset=True,savemodel=False,maxerror=0.15):
    # 初始化变量
    init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
    # 开启会话
    with tf.Session() as sess:
        sess.run(init)
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        if(readmodel):
            tf.train.Saver().restore(sess,model)
        labels_result = tf.reshape(tf.one_hot(labelnplist, depth=type), [-1, recognizenum * type]).eval()
        if not (keep_prob):
            acc = sess.run(accuracy, feed_dict={x: imagevalue, y_true: labels_result})
        else:
            acc = sess.run(accuracy, feed_dict={x: imagevalue, y_true: labels_result, keep_probtf: keep_prob})
        if(bestacc-acc<maxerror or savemodel):
            save_model(model,sess)
        coord.request_stop()
        coord.join(threads)
    if(reset):
        tf.reset_default_graph()
    return acc


def predict_info_with_nopoint(imagevalue, labelnplist, recognizenum, type, model, optimizer, loss, accuracy, y_true, x,
                           learingtimes,keep_prob=None,keep_probtf=None,bestacc=0.0, readmodel=False, reset=True,savemodel=False,maxerror=0.15):
    # 初始化变量
    init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
    # 开启会话
    with tf.Session() as sess:
        sess.run(init)
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        if(readmodel):
            tf.train.Saver().restore(sess,model)
        labels_result = tf.reshape(tf.one_hot(labelnplist, depth=type), [-1, recognizenum * type]).eval()
        if not (keep_prob):
            acc = sess.run(accuracy, feed_dict={x: imagevalue, y_true: labels_result})
        else:
            acc= sess.run(accuracy,feed_dict={x:imagevalue,y_true:labels_result,keep_probtf:keep_prob})
        if(bestacc-acc<maxerror or savemodel):
            save_model(model,sess)
        coord.request_stop()
        coord.join(threads)
    if(reset):
        tf.reset_default_graph()
    return acc



def predict_info(imagevalue, recognizenum, type, width, height, model,
                 channel=3, sigmiod=True, outputchannel=None,
                          filter=None,
                          ride=None,
                          keep_prob=None,
                          middlechannel=1024,realProb=False,reset=False):
    if (reset):
        tf.reset_default_graph()
    if not outputchannel:
        outputchannel=[32,64]
    if not filter:
        filter=[5,5]
    if not ride:
        ride=[2,2]
    # 准备输入数据
    x = tf.placeholder(tf.float32, shape=[None, height, width, channel])
    keep_probtf = None
    if (keep_prob):
        keep_probtf = tf.placeholder(tf.float32)
    y_predict = create_cnn_model(x, width, height, channel, recognizenum, type, outputchannel=outputchannel,
                                 filter=filter, ride=ride, keep_prob=keep_prob, middlechannel=middlechannel)
    print("ok start predict.")
    # signmoid多值 softmax单值求解
    if sigmiod:
        fx = tf.nn.sigmoid(y_predict)
    else:
        fx = tf.nn.softmax(y_predict)
    predict = tf.argmax(tf.reshape(y_predict, shape=[-1, recognizenum, type]),axis=2)

    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        tf.train.Saver().restore(sess, save_path=model)
        if not (keep_prob):
            probabilities, _ = sess.run([predict, fx], feed_dict={x: imagevalue})
        else:
            probabilities, _ = sess.run([predict, fx], feed_dict={x: imagevalue,keep_probtf:keep_prob})
        coord.request_stop()
        coord.join(threads)
        if not realProb:
            return probabilities
        else:
            resultprob=[]
            for j in range(len(probabilities)):
                realProblist = []
                for k in range(len(probabilities[j])):
                    realProblist.append(_[j][probabilities[j][k]])
                resultprob.append(realProblist)
            return probabilities,resultprob

