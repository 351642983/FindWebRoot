#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/10 8:32
# @Author: hdq
# @File  : tfhandle.py
import os

import tensorflow as tf


# import stringhandle as sh
# from PIL import Image
# import shutil


# def read_binary_final(filelist, height=32, width=32, channel=3, batch_size=100, capacity=100, num_threads=2):
#     """
#     读取二进制文件
#     :return:
#     """
#     filemap=[]
#     shutil.rmtree('./temp/')
#     os.mkdir('./temp/')
#     for i in range(len(filelist)):
#         one = filelist[i]
#         if one.startswith(".") or one.startswith("/") is False:
#             shutil.copyfile(one, r"./temp/%d" % i)  # 复制文件/文件夹，复制 old 为 new（new是文件，若不存在，即新建），复制 old 为至 new 文件夹（文件夹已存在）
#             filelist[i] = r"./temp/%d" % i
#             filemap.append(one)
#
#     file_queue = tf.train.string_input_producer(filelist)
#     print(filelist)
#     # 2、读取与解码
#     # 读取
#     reader = tf.WholeFileReader()
#     # key文件名 value样本
#     filename, value = reader.read(file_queue)
#     # 解码
#     decoded = tf.decode_raw(value, tf.uint8)
#     # 切片操作
#     decoded=tf.reshape(decoded,[height,width,channel])
#
#     # 3、构造批处理队列
#     filename_batch,image_batch = tf.train.batch([filename, decoded], batch_size=batch_size, num_threads=num_threads,
#                                               capacity=capacity)
#
#     # 开启会话
#     with tf.Session() as sess:
#         # 开启线程
#         coord = tf.train.Coordinator()
#         threads = tf.train.start_queue_runners(sess=sess, coord=coord)
#
#         filename_value,image_value = sess.run([filename_batch,image_batch])
#
#         coord.request_stop()
#         coord.join(threads)
#
#     filename_value=[sh.getstringexep(r"b'./temp\\\\(.*?)") for init in filename_value]
#     filename_value=[filemap[int(sf)] for sf in filename_value]
#     return filename_value,image_value


# def read_tfrecords(tfrecordname, height, width, channel):
#     """
#     读取TFRecords文件
#     :return:
#     """
#     # 1、构造文件名队列
#     file_queue = tf.train.string_input_producer([tfrecordname])
#
#     # 2、读取与解码
#     # 读取
#     reader = tf.TFRecordReader()
#     key, value = reader.read(file_queue)
#
#     # 解析example
#     feature = tf.parse_single_example(value, features={
#         "image": tf.FixedLenFeature([], tf.string),
#         "label": tf.FixedLenFeature([], tf.int64)
#     })
#     image = feature["image"]
#     label = feature["label"]
#     print("read_tf_image:\n", image)
#     print("read_tf_label:\n", label)
#
#     # 解码
#     image_decoded = tf.decode_raw(image, tf.uint8)
#     print("image_decoded:\n", image_decoded)
#     # 图像形状调整
#     image_reshaped = tf.reshape(image_decoded, [height, width, channel])
#     print("image_reshaped:\n", image_reshaped)
#
#     # 3、构造批处理队列
#     image_batch, label_batch = tf.train.batch([image_reshaped, label], batch_size=100, num_threads=2, capacity=100)
#     print("image_batch:\n", image_batch)
#     print("label_batch:\n", label_batch)
#
#     # 开启会话
#     with tf.Session() as sess:
#         # 开启线程
#         coord = tf.train.Coordinator()
#         threads = tf.train.start_queue_runners(sess=sess, coord=coord)
#
#         image_value, label_value = sess.run([image_batch, label_batch])
#         print("image_value:\n", image_value)
#         print("label_value:\n", label_value)
#
#         # 回收资源
#         coord.request_stop()
#         coord.join(threads)
#
#     return None
#
#
# def save_tfrecords(tfrecordname, image_batch, label_batch):
#     """
#     将样本的特征值和目标值一起写入tfrecords文件
#     :param image:
#     :param label:
#     :return:
#     """
#     with tf.python_io.TFRecordWriter(tfrecordname) as writer:
#         # 循环构造example对象，并序列化写入文件
#         size = len(image_batch)
#         for i in range(size):
#             image = image_batch[i].tostring()
#             label = label_batch[i][0]
#             # print("tfrecords_image:\n", image)
#             # print("tfrecords_label:\n", label)
#             example = tf.train.Example(features=tf.train.Features(feature={
#                 "image": tf.train.Feature(bytes_list=tf.train.BytesList(value=[image])),
#                 "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
#             }))
#             # example.SerializeToString()
#             # 将序列化后的example写入文件
#             writer.write(example.SerializeToString())
#     return None


# 几个值,值的分类[4,26]:验证码4位,每个验证码有26种字母的可能
# [4*26] softmax+交叉熵 衡量损失 训练值-->一个问题独立且不相互影响单分类问题
# 计算预测值:sigmoid交叉熵 -> 一个样本计算多分类问题 损失
# 准确率计算:对比真实值和预测值所在位置，求平均
# 例子y_predict[None,10] 单tf.argmax(y_predict,axis=1)
# y_predict[None,4,26] 多tf.argmax(y_predict,axis=2/-1)
# [True,True,True,False]-> tf.reduce_all() ->False
#
# 流程 特征值，目标值--模型
# 特征值图片--对应目标值
# 读取图片数据,queue reader
# 建立key索引label list 如[[2,1,3,4],[1,2,3,4]]
# 根据文件名查表
# 2卷积 1全连接
# 构建卷积神经网络 == y_predict
# 计算sigmod交叉熵损失
# 优化
# 计算准确率
# 开启会话，模型训练

# # read_pic 返回元组 key,value--文件名和样本内容 key索引目标值label
# def read_pic_from_firstsize(file_list, channel=3,
#                             num_threads=2,
#                             batch_size=32, capacity=64):
#     file_queue = tf.train.string_input_producer(file_list)
#     reader = tf.WholeFileReader()
#     filename, value = reader.read(file_queue)
#     image = tf.image.decode_jpeg(value)
#     img = Image.open(file_list[0])
#     image.set_shape([img.height, img.width, channel])
#     filename_batch, image_batch = tf.train.batch([filename, image], batch_size=batch_size, num_threads=num_threads,
#                                                  capacity=capacity)
#     return filename_batch, image_batch


def read_and_decode(file_list, width, height, channel=3,
                    num_threads=2,
                    batch_size=100, capacity=100):
    """
    读取二进制文件
    :return:
    """
    # 1、构造文件队列
    image_bytes = width * height * channel
    file_queue = tf.train.string_input_producer(file_list)

    # 2、构造二进制文件读取器，读取内容, 每个样本的字节数
    reader = tf.FixedLengthRecordReader(width * height * channel)
    key, value = reader.read(file_queue)
    # print("value", value)

    # 3、解码内容, 二进制文件内容的解码
    label_image = tf.decode_raw(value, tf.uint8)
    # print("label_image", label_image)

    # 4、分割出图片和标签数据，切除特征值和目标值
    # label = tf.slice(label_image, [0], [label_bytes])
    # label = tf.cast(label, tf.int32)
    image = tf.slice(label_image, [0], [image_bytes])
    # print("label", label)
    # print("image", image)

    # 5、可以对图片的特征数据进行形状的改变 [3072] --> [32, 32, 3]
    image_reshape = tf.reshape(image, [height, width, channel])
    # print("image_reshape", image_reshape)

    # 6、批处理数据,总样本数为10000 *5 = 50000，为了节省运行时间，我改为100
    filename_batch, image_batch = tf.train.batch([key, image_reshape], batch_size=batch_size, num_threads=num_threads,
                                                 capacity=capacity)
    # print("image_batch:", image_batch, "\nlabel_batch:", label_batch)
    return filename_batch, image_batch


def read_pic(file_list, width, height, channel=3,
             num_threads=2,
             batch_size=100, capacity=100):
    file_queue = tf.train.string_input_producer(file_list)
    reader = tf.WholeFileReader()
    filename, value = reader.read(file_queue)
    image = tf.image.decode_image(value)
    image.set_shape([height, width, channel])

    filename_batch, image_batch = tf.train.batch([filename, image], batch_size=batch_size, num_threads=num_threads,
                                                 capacity=capacity)
    return filename_batch, image_batch


def get_file_batchlist(filename_batch, image_batch):
    # if not (tf.is_nan):
    #     tf.reset_default_graph()
    #     tf.get_variable_scope().reuse_variables()
    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        filename, image = sess.run([filename_batch, image_batch])
        coord.request_stop()
        coord.join(threads)
        filename = [str(one) for one in filename]
        return filename, image


import stringhandle as sh
import filehandle as fh


def auto_read_picture_move_to_standard(file_list, width, height, labellist, outdir=r'./temp', channel=3, num_threads=2,
                                       stay=1, type=".jpg",default=None,nodefault=False):
    filelabelmap = dict(zip([fh.get_path_file_basename(one) for one in file_list], labellist))

    if (os.path.exists(outdir)) is False:
        os.makedirs(outdir)
    for one in file_list:
        fh.image_change_to(one, outdir + "/" + fh.get_path_file_basename(one) + type, width, height)

    train_listtest = fh.get_files_by_types(outdir, '')
    # print(train_listtest)
    # print(file_list)
    filename_batch, image_batch = read_pic(train_listtest, width, height, channel, num_threads, len(train_listtest),
                                           len(train_listtest))
    filename, image = get_file_batchlist(filename_batch, image_batch)
    filenamebatchlist = [fh.get_path_file_basename(sh.getstringexep(r"'(.*?)'", one)[0]) for one
                         in filename]
    finallabel = [filelabelmap.get(one,default) for one in filenamebatchlist if(not filelabelmap.get(one,default)) and nodefault]

    if (stay == 0):
        fh.finish_files_toproject()
    tf.reset_default_graph()
    return filenamebatchlist, image, finallabel


def auto_read_sound_move_to_standard(file_list, width, height, labellist, outdir=r'./temp', channel=3, num_threads=2,
                                     stay=1, type=".jpg"):
    filelabelmap = dict(zip([fh.get_path_file_basename(one) for one in file_list], labellist))

    if (os.path.exists(outdir)) is False:
        os.makedirs(outdir)
    for one in file_list:
        fh.sound_to_image(one, outdir + "/" + fh.get_path_file_basename(one) + "_" + ".png")
        fh.image_change_to(outdir + "/" + fh.get_path_file_basename(one) + "_" + ".png",
                           outdir + "/" + fh.get_path_file_basename(one) + type, width, height)
        if (os.path.exists(outdir + "/" + fh.get_path_file_basename(one) + "_" + ".png")):
            os.remove(outdir + "/" + fh.get_path_file_basename(one) + "_" + ".png")

    train_listtest = fh.get_files_by_types(outdir, '')
    # print(train_listtest)
    # print(file_list)
    filename_batch, image_batch = read_pic(train_listtest, width, height, channel, num_threads, len(train_listtest),
                                           len(train_listtest))
    filename, image = get_file_batchlist(filename_batch, image_batch)
    filenamebatchlist = [fh.get_path_file_basename(sh.getstringexep(r"'(.*?)'", one)[0]) for one
                         in filename]

    finallabel = [filelabelmap[one] for one in filenamebatchlist]

    if (stay == 0):
        fh.finish_files_toproject()
    return filenamebatchlist, image, finallabel


def auto_read_sound_move_to_standard_without_label(file_list, width, height, outdir=r'./temp', channel=3, num_threads=2,
                                                   stay=1, type=".jpg"):
    if (os.path.exists(outdir)) is False:
        os.makedirs(outdir)
    for one in file_list:
        fh.sound_to_image(one, outdir + "/" + fh.get_path_file_basename(one) + "_" + ".png")
        fh.image_change_to(outdir + "/" + fh.get_path_file_basename(one) + "_" + ".png",
                           outdir + "/" + fh.get_path_file_basename(one) + type, width, height)
        if (os.path.exists(outdir + "/" + fh.get_path_file_basename(one) + "_" + ".png")):
            os.remove(outdir + "/" + fh.get_path_file_basename(one) + "_" + ".png")

    train_listtest = fh.get_files_by_types(outdir, '')
    filename_batch, image_batch = read_pic(train_listtest, width, height, channel, num_threads, len(train_listtest),
                                           len(train_listtest))
    filename, image = get_file_batchlist(filename_batch, image_batch)
    filenamebatchlist = [fh.get_path_file_basename(sh.getstringexep(r"'(.*?)'", one)[0]) for one
                         in filename]
    if (stay == 0):
        fh.finish_files_toproject()
    return filenamebatchlist, image


def auto_read_picture_move_to_standard_without_label(file_list, width, height, outdir=r'./temp', channel=3,
                                                     num_threads=2, stay=1):
    if (os.path.exists(outdir)) is False:
        os.makedirs(outdir)
    for one in file_list:
        fh.image_change_to(one, outdir + "/" + fh.get_path_file_basename(one) + ".png", width, height)

    train_listtest = fh.get_files_by_types(outdir, '')
    filename_batch, image_batch = read_pic(train_listtest, width, height, channel, num_threads, len(train_listtest),
                                           len(train_listtest))
    filename, image = get_file_batchlist(filename_batch, image_batch)
    filenamebatchlist = [fh.get_path_file_basename(sh.getstringexep(r"'(.*?)'", one)[0]) for one
                         in filename]
    if (stay == 0):
        fh.finish_files_toproject()
    return filenamebatchlist, image


# 返回 文件名list,image值,对应label标签信息
def auto_read_picture(file_list, width, height, labellist, channel=3, num_threads=2):
    filelabelmap = dict(zip(file_list, labellist))
    filename_batch, image_batch = read_pic(file_list, width, height, channel, num_threads, len(file_list),
                                           len(file_list))
    filename, image = get_file_batchlist(filename_batch, image_batch)
    filenamebatchlist = [fh.get_path_file_basename(sh.getstringexep(r"'(.*?)'", one)[0]) for one
                         in filename]
    finallabel = [filelabelmap[one] for one in filenamebatchlist]
    return filenamebatchlist, image, finallabel


import arraychanger as ac
import numpy as np


# 获取标签值列表
def read_picture_label_nplist(labelcsvpath, strlist):
    list = ac.list_csv_reader_label(labelcsvpath, strlist)
    relist = [[one] for one in list]
    return np.array(relist)


# print(read_picture_label(r"C:\Users\Halo\Desktop\数据\大数据数据\train_label.csv",'Label'))

# list获取标签
def read_label_list(labelcsvpath, strlist):
    list = ac.list_csv_reader_label(labelcsvpath, strlist)
    relist = [[one] for one in list]
    return relist


# 将标签转化为可tf运算标签
def change_label_to_tfable(labellist, typenum):
    result = []
    for one in labellist:
        templistout = []
        for two in one:
            templist = []
            for num in range(typenum):
                if two != num:
                    templist.append(0)
                else:
                    templist.append(1)
            templistout.append(templist)
        result.append(templistout)
    return np.array(result)


# 将标签转化为可tf运算标签
def change_label_to_tfable_pre(labellist, typenum):
    result = []
    for one in labellist:
        # templistout = []
        for two in one:
            templist = []
            for num in range(typenum):
                if two != num:
                    templist.append(0)
                else:
                    templist.append(1)
            result.append(templist)
        # result.append(templistout)
    return np.array(result)


# 将标签英文列，转化为对应字母序号表
def change_label_words_to_num(label_words,szchar='A'):
    result = []
    for one in label_words:
        temp = []
        for two in one:
            temp.append(ord(two) - ord(szchar))
        result.append(temp)
    return result


def change_onehot_to_label(onehotlist):
    maxlen = len(onehotlist[0])
    result = []
    for one in onehotlist:
        for init in range(maxlen):
            if (one[init] == 1):
                result.append(init)
                break
    return result


def change_data_to_cnnable(list, width, height, channel=1):
    num = 0
    result = []
    for one in list:
        tlen = len(one)
        if (tlen % (width * height * channel) != 0):
            return
        heightc = []
        widthc = []
        cha=[]
        for inone in one:
            num += 1
            cha.append(inone)
            if (num % channel == 0):
                widthc.append(cha)
                cha = []
            if (len(widthc) == width):
                heightc.append(widthc)
                widthc = []
        result.append(heightc)
    return result


from PIL import Image, ImageDraw, ImageFont  # 引入绘图模块
import random  # 引入随机函数模块

def get_random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

def verification_code(weight,height,output,type=".png",spilt=4,bgcolor=None,ctcolor=None):
    namelist=[]
    pointlist=[]
    pathlist=[]
    spilt_x=weight/spilt
    spilt_y=height/spilt
    for i in range(spilt):
        # 1.1 定义变量，宽，高，背景颜色
        if not (bgcolor):
            background_color = get_random_color()
        else:
            background_color=bgcolor
        # 1.2 创建画布对象
        image = Image.new('RGB', (weight, height), background_color)
        # 1.3 创建画笔对象
        draw = ImageDraw.Draw(image)
        if not (ctcolor):
            recolor = get_random_color()
        else:
            recolor = ctcolor
        draw.ellipse((i*spilt_x,i*spilt_y,(i+1)*spilt_x,(i+1)*spilt_y),recolor,recolor)
        pointlist.append([i,i,(i+1),(i+1)])
        namelist.append("l"+str(i))
        image.save(output+"/l"+str(i)+type)
        pathlist.append(output+"/l"+str(i)+type)
    for j in range(spilt,0,-1):
        i=j-1
        # 1.1 定义变量，宽，高，背景颜色
        if not (bgcolor):
            background_color = get_random_color()
        else:
            background_color = bgcolor
        # 1.2 创建画布对象
        image = Image.new('RGB', (weight, height), background_color)
        # 1.3 创建画笔对象
        draw = ImageDraw.Draw(image)
        if not (ctcolor):
            recolor = get_random_color()
        else:
            recolor = ctcolor
        draw.ellipse((i*spilt_x,(spilt-i-1)*spilt_y,(i+1)*spilt_x,(spilt-i)*spilt_y),recolor,recolor)
        pointlist.append([i, (spilt-i-1), (i + 1), (spilt-i)])
        namelist.append("r" + str(i))
        image.save(output + "/r" + str(i) + type)
        pathlist.append(output + "/r" + str(i) + type)
    return namelist,pointlist,pathlist

#生成圆坐标图
def verification_code_sub(weight,height,outputpath,x,y,spilt=4,bgcolor=None,ctcolor=None):
    spilt_x = weight / spilt
    spilt_y = height / spilt
    if not (bgcolor):
        background_color = get_random_color()
    else:
        background_color = bgcolor
    # 1.2 创建画布对象
    image = Image.new('RGB', (weight, height), background_color)
    # 1.3 创建画笔对象
    draw = ImageDraw.Draw(image)
    if not (ctcolor):
        recolor = get_random_color()
    else:
        recolor = ctcolor
    draw.ellipse((x*spilt_x,y*spilt_y,(x+1)*spilt_x,(y+1)*spilt_y),recolor,recolor)
    image.save(outputpath)

#将对应json labelme文件转化为,label 矩形坐标点
def read_labelme_wh(jsonpath,encoding='UTF-8'):
    init=fh.json_get_infos(jsonpath,encoding)
    label=  ""
    xlist = []
    ylist = []
    for one in init['shapes']:
        label=one['label']
        for thesub in one['points']:
            xlist.append(int(thesub[0]))
            ylist.append(int(thesub[1]))
    return label,[min(xlist),min(ylist),max(xlist),max(ylist)],fh.get_path_file_completebasename(init['imagePath']),[int(init['imageWidth']),int(init['imageHeight'])]

#获取json中的所有边框信息和标签
def read_labelmelist(pathdir,pointdir="pic/"):
    jsonlist=fh.get_files_by_types(pathdir,".json")
    predir=pathdir[:-len(fh.get_path_file_completebasename(pathdir))]+pointdir
    labellist,whlist,pathlist,rwhlist=[],[],[],[]
    for one in jsonlist:
        label,wh,path,rwh=read_labelme_wh(one)
        labellist.append(label)
        whlist.append(wh)
        pathlist.append(predir+path[:])
        rwhlist.append(rwh)
    return labellist,whlist,pathlist,rwhlist

#获得是在整数列表中的哪个位置之中
def get_in_range_step(value,numlist):
    for i in range(len(numlist)-1):
        if(numlist[i]<=value<=numlist[i+1]):
            return i

#将对应列表图片大小转换为split表示
def change_wh_tosplittype(wh,width,height,spilt):
    result=[]
    rangex=[]
    rangey=[]
    x_spilt=width/spilt
    y_spilt=height/spilt
    xp,yp=0,0
    for i in range(spilt):
        if(i==0):
            xp=x_spilt/2
            yp=y_spilt/2
            rangex.append(0)
            rangex.append(x_spilt/2)
            rangey.append(0)
            rangey.append(y_spilt / 2)
        elif(i==spilt-1):
            xp += x_spilt
            yp += y_spilt
            rangex.append(xp)
            rangey.append(yp)
            rangex.append(width)
            rangey.append(height)
        else:
            xp += x_spilt
            yp += y_spilt
            rangex.append(xp)
            rangey.append(yp)
    result.append(get_in_range_step(wh[0],rangex))
    result.append(get_in_range_step(wh[1], rangey))
    result.append(get_in_range_step(wh[2], rangex))
    result.append(get_in_range_step(wh[3], rangey))
    return result



#将对应列表图片大小转换为split表示
def change_whlist_tosplittype(whlist,widheilist,spilt):
    resultlist=[]
    for one in range(len(whlist)):
        resultlist.append(change_wh_tosplittype(whlist[one],widheilist[one][0],widheilist[one][1],spilt))
    return resultlist


#获取对应图片列表的坐标
def get_labelmelist_labelwh(pathlist,jsondir,verpathlist=[],verlaellist=[],spilt=10):
    plabelresult=[]
    # print(pathlist,verpathlist)
    namelist, whlist, plist, rwhlist = read_labelmelist(jsondir)
    # plist = [fh.get_path_file_completebasename(one) for one in plist]
    plist=fh.get_paths_file_basename(plist)
    pathlist=fh.get_paths_file_basename(pathlist)
    print(pathlist)
    print("labelme列表:", plist)
    for one in pathlist:
        if(plist.index(one)>=0):
            # labelresult.append(whlist[plist.index(fh.get_path_file_completebasename(one))])
            plabelresult.append(change_wh_tosplittype(whlist[plist.index(one)],rwhlist[plist.index(one)][0],rwhlist[plist.index(one)][1],spilt))
        elif(one in verpathlist):
            plabelresult.append(verlaellist[verpathlist.index(one)])
        else:
            print("名字标签对应 Error:label未找到但path列表中有对应的文件信息 ",one)

    return plabelresult


#得到预测结果列表
def get_probablities_resultslist(probabilities,pz=None):
    resultlist=[]
    for i in range(len(probabilities)):
        strp = "["
        for k in range(len(probabilities[i])):
            z=probabilities[i][k]
            if not (pz):
                strp += str(z)
            else:
                strp += "'"+chr(z+ord(pz))+"'"
            if(k!=len(probabilities[i])-1):
                strp+=","
        strp+="]"
        resultlist.append(eval(strp))

    return resultlist

#获得预测结果字典
def get_probablities_resultsdict(filenamelist,probabilities,pz=None):
    resultlist=get_probablities_resultslist(probabilities,pz)
    return dict(zip(filenamelist,resultlist))

#将读取的cnnable数据转化为tfable
def change_cnndata_to_tfable(infolist):
    result=[]
    for one in infolist:
        subtemp=[]
        for two in one:
            for three in two:
                for four in three:
                    subtemp.append(four)
        result.append(subtemp)
    return result



#将cnn里面最里层的数据抽出来
def out_cnn_pre(lists):
    result=[]
    for one in lists:
        temp1=[]
        for two in one:
            temp2=[]
            for three in two:
                temp2.append(*three)
            temp1.append(temp2)
        result.append(temp1)
    return result

#将cnn里面最里层的数据增加一层
def add_cnn_post(lists):
    result=[]
    for one in lists:
        temp1=[]
        for two in one:
            temp2=[]
            for three in two:
                temp2.append([three])
            temp1.append(temp2)
        result.append(temp1)
    return result

#将图片里面最里层的数据增加一层
def add_booleanimage_post(lists):
    result=[]
    for one in lists:
        temp1=[]
        for two in one:
            temp1.append([two])
        result.append(temp1)
    return result

#将图片里面最里层的数据增加一层
def out_booleanimage_pre(lists):
    result=[]
    for one in lists:
        temp1=[]
        for two in one:
            temp1.append(*two)
        result.append(temp1)
    return result

#将二值化图片缩放成对应关键信息部分
def enlarge_booleanimage_cnninfo(image,width,height):
    widthsum = []
    heightsum=[]
    for two in image:
        temp2 = []
        for three in two:
            temp2.append(three)
        widthsum.append(sum(temp2))



    for two in range(len(image[0])):
        temp1=[]
        for one in range(len(image)):
            temp1.append(image[one][two])
        heightsum.append(sum(temp1))
    iterwidsum=[]
    iter=0
    for sub in widthsum:
        iter+=sub
        iterwidsum.append(iter)

    minw=max(iterwidsum)
    wp=-1
    for i in range(len(iterwidsum)-width):
        nowrange=abs(iterwidsum[i+width]-iterwidsum[i])
        if(nowrange<minw):
            minw=nowrange
            wp=i

    iterheisum = []
    iter = 0
    for sub in heightsum:
        iter += sub
        iterheisum.append(iter)
    minh = max(iterheisum)
    hp = -1
    for i in range(len(iterheisum) - height):
        nowrange = abs(iterheisum[i+ height] - iterheisum[i ])
        if (nowrange < minh):
            minh = nowrange
            hp = i
    # print("高:",len(image))
    wpz=height/4
    if(len(image)-wp<abs(wpz)):
        wpz=len(image)-wp
    hpz = width / 4
    if (len(image[0])-hp<abs(hpz)):
        hpz =len(image[0])-hp
    print(wp,wpz,width, hp,hpz,height)
    #w高 h宽
    return np.array(image)[int(wp+hpz):int(wp+width+hpz),int(hp+wpz):int(hp+height+wpz)]

def imagebatchs_enlarge_booleanimage_cnninfo(fileslist,imagebatchs,twidth,theight,width,height,outdir=None,type=".png",picmode="L",gaussianblur=False,mfilter=(5,5),mvalue=0.0):
    if (outdir):
        pout=outdir
    else:
        pout=fh.get_path_file_subpath(fileslist[0])
    for one in range(len(fileslist)):
        fh.array_to_image(enlarge_booleanimage_cnninfo(fh.out_booleanimage_pre(np.multiply(imagebatchs[one], 255)), twidth, theight), pout+ "/"+fh.get_path_file_basename(fileslist[one])+type,picmode=picmode)
    return fh.imagedir_to_arrays_tfable(pout,type,True, width,height,gaussianblur=gaussianblur,mfilter=mfilter,mvalue=mvalue)

def isset(v):
    try:
        type(eval(v))
    except :
        return 0
    else:
        return 1

#输入数据（待处理):
def prepare_cnninfo(filelist,infovalues,labelvalues):
    global fl,ivs,lls,st
    fl,ivs,lls = filelist,infovalues,labelvalues
    st=0
def get_cnninfo(nums,returnfile=False):
    global fl, ivs, lls,st
    result1=None
    if(returnfile):
        result1 = fl[st:st + nums]
    result2=ivs[st:st+nums]
    result3 = lls[st:st + nums]
    st=st+nums
    if(len(result2)!=nums or len(ivs[st:st+1])==0):
        st = nums - len(result2)
        result2=[*result2,*ivs[0:st]]
        result3=[*result3,*lls[0:st]]

    if(returnfile):
        return result1,result2,result3
    else:
        return result2,result3

#根据labelme产生遮罩层
def labelme_mask(labelmedir,outdir,type=".png",outtype=".png"):
    _,whlist,pathlist,rwhlist= read_labelmelist(labelmedir)
    fh.imgdir_to_mask(fh.get_path_file_subpath(pathlist[0]),outdir,type,outtype)

def scale_image_from_labelme(datadir,scalewidth,scaleheight,pointmark="1",cutpicdir="/pic",cutpictype=".jpg",labelmejson="/labelme_json",Boolean=False):
    filenameplist,imagepvalue=fh.imagedir_to_arrays_tfable(datadir+cutpicdir,cutpictype,Boolean,scalewidth,scaleheight,pointmark=pointmark)
    labelslist,whlist,pathlist,rwhlist=read_labelmelist(datadir+labelmejson)
    sf_whlist1=[]
    for i in range(len(rwhlist)):
        wscale=scalewidth/rwhlist[i][0]
        hscale=scaleheight/rwhlist[i][1]
        sf_whlist1.append([int(whlist[i][0]*wscale),int(whlist[i][1]*hscale),int(whlist[i][2]*wscale),int(whlist[i][3]*hscale)])
    return filenameplist,imagepvalue,sf_whlist1