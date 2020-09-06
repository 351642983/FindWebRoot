#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/8 21:54
#@Author: hdq
#@File  : bidirectional_rnn.py

from __future__ import print_function
import tensorflow as tf
from tensorflow.contrib import rnn
# from tensorflow.examples.tutorials.mnist import input_data
import os
from keras.utils import to_categorical
import tfhandle as th
import numpy as np
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
# mnist = input_data.read_data_sets("./mnist_data/", one_hot=True)

def birnnweb(imagevalues,labels,
# Traning Parameters
learning_rate = 0.001,
training_step = 10000,
batch_size = 128,
display_step = 400,
# Network Parmeters
num_input = 28,
timestep = 28,
num_hidden = 128,
num_classes = 10,
savemodel=None):
    labels=to_categorical(labels)
    th.prepare_cnninfo([],imagevalues,labels)
    # tf Graph input
    X = tf.placeholder("float32", [None, timestep, num_input])
    Y = tf.placeholder("float32", [None, num_classes])

    # Define weights
    weights = {
        'out': tf.Variable(tf.random_normal([2 * num_hidden, num_classes]))
    }
    biases = {
        'out': tf.Variable(tf.random_normal([num_classes]))
    }


    def BiRNN(X, weights, biases):
        x = tf.unstack(X, timestep, 1)

        # define lstm cells with tensorflow
        # Forward direction cell
        lstm_fw_cell = rnn.BasicLSTMCell(num_hidden, forget_bias=1.0)
        # Backward direction cell
        lstm_bw_cell = rnn.BasicLSTMCell(num_hidden, forget_bias=1.0)

        # Get lstm cell output
        try:
            outputs, _, _ = rnn.static_bidirectional_rnn(lstm_fw_cell, lstm_bw_cell, x, dtype=tf.float32)
        except Exception:
            outputs = rnn.static_bidirectional_rnn(lstm_fw_cell, lstm_bw_cell, x, dtype=tf.float32)

            # Linaer activation,using rnn inner loop last output
        return tf.matmul(outputs[-1], weights['out']) + biases['out']


    logits = BiRNN(X, weights, biases)
    prediction = tf.nn.softmax(logits)

    # Define loss and optimizer
    loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    train_op = optimizer.minimize(loss_op)

    # Evaluate model
    correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
    resultpred=tf.argmax(prediction, 1)
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    # Initialize Variable
    init = tf.global_variables_initializer()

    # start training
    with tf.Session() as sess:
        # Run the initializer
        sess.run(init)

        for step in range(1, training_step + 1):
            batch_x, batch_y = th.get_cnninfo(batch_size)

            # Reshape data to get 28 seq of 28 elements
            batch_x = np.asarray(batch_x).reshape((batch_size, timestep, num_input))
            # Run optimizetion op
            sess.run(train_op, feed_dict={X: batch_x, Y: batch_y})
            if step % display_step == 0 or step == 1:
                # Calculate batch loss and accuracy
                loss, acc = sess.run([loss_op, accuracy], feed_dict={X: batch_x, Y: batch_y})
                print("Step " + str(step) + ",Minbatch Loss=" + "{:.4f}".format(
                    loss) + ",Training Accuracy=" + "{:.3f}".format(acc))
        print("Optimization Finished!")
        if(savemodel):
            save_model(savemodel,sess)
            print("Savemodel sucessful in"+savemodel)
        # Calculate accuracy for 128 mnist test images
        # test_len = 128
        # test_data = mnist.test.images[:test_len].reshape((-1, timestep, num_input))
        # test_label = mnist.test.labels[:test_len]
        # print("Test Accuracy:", sess.run(accuracy, feed_dict={X: test_data, Y: test_label}))
        return resultpred, timestep, num_input
        
def save_model(dirpath, sess):
    tf.train.Saver().save(sess, save_path=dirpath)


def predict(imagevalues,resultpredtf, timesteps, num_input):
    init = tf.global_variables_initializer()
    X = tf.placeholder("float", [None, timesteps, num_input])
    with tf.Session() as sess:
        # tf.reset_default_graph()
        sess.run(init)
        imagevalues=imagevalues.reshape((len(imagevalues), timesteps, num_input))
        result=sess.run(resultpredtf,feed_dict={X:imagevalues})
    return result
    
def predict_withmodel(imagevalues, num_classes ,model ,timestep=28,num_input=28,num_hidden=128,returnpro=False):
    init = tf.global_variables_initializer()
    X = tf.placeholder("float32", [None, timestep, num_input])
    # Define weights
    weights = {
        'out': tf.Variable(tf.random_normal([2 * num_hidden, num_classes]))
    }
    biases = {
        'out': tf.Variable(tf.random_normal([num_classes]))
    }


    def BiRNN(X, weights, biases):
        x = tf.unstack(X, timestep, 1)

        # define lstm cells with tensorflow
        # Forward direction cell
        lstm_fw_cell = rnn.BasicLSTMCell(num_hidden, forget_bias=1.0)
        # Backward direction cell
        lstm_bw_cell = rnn.BasicLSTMCell(num_hidden, forget_bias=1.0)

        # Get lstm cell output
        try:
            outputs, _, _ = rnn.static_bidirectional_rnn(lstm_fw_cell, lstm_bw_cell, x, dtype=tf.float32)
        except Exception:
            outputs = rnn.static_bidirectional_rnn(lstm_fw_cell, lstm_bw_cell, x, dtype=tf.float32)

            # Linaer activation,using rnn inner loop last output
        return tf.matmul(outputs[-1], weights['out']) + biases['out']
    logits = BiRNN(X, weights, biases)
    prediction = tf.nn.softmax(logits)
    resultpred=tf.argmax(prediction, 1)

    with tf.Session() as sess:
        # Run the initializer
        tf.train.Saver().restore(sess, save_path=model)
        sess.run(init)
        imagevalues=np.array(imagevalues).reshape((len(imagevalues), timestep, num_input))
        if not (returnpro):
            result=sess.run(resultpred,feed_dict={X:imagevalues})
        else:
            result,pro=sess.run([resultpred,prediction],feed_dict={X:imagevalues})
    if not returnpro:
        return result
    else:
        return result,pro