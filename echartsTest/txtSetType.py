#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/12 11:58
#@Author: zhangtao
#@File  : txtSetType.py
# !D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : TFIDF_naive_bayes_wy.py
# @Author: WangYe
# @Date  : 2019/5/29
# @Software: PyCharm
# 机器学习之文本分类

import jieba_fast as jieba
from numpy import *
import pickle  # 持久化
import os
from sklearn.feature_extraction.text import TfidfTransformer  # TF-IDF向量转换类
from sklearn.feature_extraction.text import TfidfVectorizer  # TF_IDF向量生成类
import numpy as np
from sklearn.naive_bayes import MultinomialNB  # 多项式贝叶斯算法
from sklearn.utils import Bunch
import filehandle as fh

def readFile(path,encoding="utf-8"):
    with open(path, 'r', errors='ignore',encoding=encoding) as file:  # 文档中编码有些问题，所有用errors过滤错误
        content = file.read()
        file.close()
        return content


def saveFile(path, result,encoding="utf-8"):
    with open(path, 'w', errors='ignore',encoding=encoding) as file:
        file.write(result)
        file.close()


def segText(inputPath, resultPath):
    fatherLists = os.listdir(inputPath)  # 主目录
    for eachDir in fatherLists:  # 遍历主目录中各个文件夹
        eachPath = inputPath + eachDir + "/"  # 保存主目录中每个文件夹目录，便于遍历二级文件
        each_resultPath = resultPath + eachDir + "/"  # 分词结果文件存入的目录
        if not os.path.exists(each_resultPath):
            os.makedirs(each_resultPath)
        childLists = os.listdir(eachPath)  # 获取每个文件夹中的各个文件
        for eachFile in childLists:  # 遍历每个文件夹中的子文件
            eachPathFile = eachPath + eachFile  # 获得每个文件路径
            #  print(eachFile)
            content = readFile(eachPathFile)  # 调用上面函数读取内容
            # content = str(content)
            result = (str(content)).replace("\r\n", "").strip()  # 删除多余空行与空格
            # result = content.replace("\r\n","").strip()

            cutResult = jieba.cut(result)  # 默认方式分词，分词结果用空格隔开
            saveFile(each_resultPath + eachFile, " ".join(cutResult))  # 调用上面函数保存文件

def segTextByTxtAndResult(strlist,resultlist, resultPath):
    # eachPath = inputPath + eachDir + "/"  # 保存主目录中每个文件夹目录，便于遍历二级文件
    # childLists = os.listdir(eachPath)  # 获取每个文件夹中的各个文件
    i=0
    for one in range(len(strlist)):  # 遍历每个文件夹中的子文件
        each_resultPath = resultPath + str(resultlist[one]) + "/"  # 分词结果文件存入的目录
        if not os.path.exists(each_resultPath):
            os.makedirs(each_resultPath)
        # eachPathFile = eachPath + eachFile  # 获得每个文件路径
        #  print(eachFile)
        content = strlist[one]  # 调用上面函数读取内容
        # content = str(content)
        result = (str(content)).replace("\r\n", "").strip()  # 删除多余空行与空格
        # result = content.replace("\r\n","").strip()
        cutResult = jieba.cut(result)  # 默认方式分词，分词结果用空格隔开
        saveFile(each_resultPath + str(i)+".txt", " ".join(cutResult))  # 调用上面函数保存文件
        i+=1

def segTextByTxt(strlist, resultPath):
    # eachPath = inputPath + eachDir + "/"  # 保存主目录中每个文件夹目录，便于遍历二级文件
    each_resultPath = resultPath + str("temp") + "/"  # 分词结果文件存入的目录
    if not os.path.exists(each_resultPath):
        os.makedirs(each_resultPath)
    # childLists = os.listdir(eachPath)  # 获取每个文件夹中的各个文件
    i=0
    for one in strlist:  # 遍历每个文件夹中的子文件
        # eachPathFile = eachPath + eachFile  # 获得每个文件路径
        #  print(eachFile)
        content = one  # 调用上面函数读取内容
        # content = str(content)
        result = (str(content)).replace("\r\n", "").strip()  # 删除多余空行与空格
        # result = content.replace("\r\n","").strip()
        cutResult = jieba.cut(result)  # 默认方式分词，分词结果用空格隔开
        saveFile(each_resultPath + str(i)+".txt", " ".join(cutResult))  # 调用上面函数保存文件
        i+=1

def bunchSave(inputFile, outputFile):
    catelist = os.listdir(inputFile)
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)  # 将类别保存到Bunch对象中
    for eachDir in catelist:
        eachPath = inputFile + eachDir + "/"
        fileList = os.listdir(eachPath)
        for eachFile in fileList:  # 二级目录中的每个子文件
            fullName = eachPath + eachFile  # 二级目录子文件全路径
            bunch.label.append(eachDir)  # 当前分类标签
            bunch.filenames.append(fullName)  # 保存当前文件的路径
            bunch.contents.append(readFile(fullName).strip())  # 保存文件词向量
    with open(outputFile, 'wb') as file_obj:  # 持久化必须用二进制访问模式打开
        pickle.dump(bunch, file_obj)
        # pickle.dump(obj, file, [,protocol])函数的功能：将obj对象序列化存入已经打开的file中。
        # obj：想要序列化的obj对象。
        # file:文件名称。
        # protocol：序列化使用的协议。如果该项省略，则默认为0。如果为负值或HIGHEST_PROTOCOL，则使用最高的协议版本


def readBunch(path):
    with open(path, 'rb') as file:
        bunch = pickle.load(file)
        # pickle.load(file)
        # 函数的功能：将file中的对象序列化读出。
    return bunch


def writeBunch(path, bunchFile):
    with open(path, 'wb') as file:
        pickle.dump(bunchFile, file)


def getStopWord(inputFile):
    stopWordList = readFile(inputFile).splitlines()
    return stopWordList


def getTFIDFMat(inputPath, stopWordList, outputPath,
                tftfidfspace_path, tfidfspace_arr_path, tfidfspace_vocabulary_path):  # 求得TF-IDF向量
    bunch = readBunch(inputPath)
    tfidfspace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[],
                       vocabulary={})
    '''读取tfidfspace'''
    tfidfspace_out = str(tfidfspace)
    saveFile(tftfidfspace_path, tfidfspace_out)
    # 初始化向量空间
    vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5)
    transformer = TfidfTransformer()  # 该类会统计每个词语的TF-IDF权值
    # 文本转化为词频矩阵，单独保存字典文件
    tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
    tfidfspace_arr = str(vectorizer.fit_transform(bunch.contents))
    saveFile(tfidfspace_arr_path, tfidfspace_arr)
    tfidfspace.vocabulary = vectorizer.vocabulary_  # 获取词汇
    tfidfspace_vocabulary = str(vectorizer.vocabulary_)
    saveFile(tfidfspace_vocabulary_path, tfidfspace_vocabulary)
    '''over'''
    writeBunch(outputPath, tfidfspace)


def getTestSpace(testSetPath, trainSpacePath, stopWordList, testSpacePath,
                 testSpace_path, testSpace_arr_path, trainbunch_vocabulary_path):
    bunch = readBunch(testSetPath)
    # 构建测试集TF-IDF向量空间
    testSpace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[],
                      vocabulary={})
    '''
       读取testSpace
       '''
    testSpace_out = str(testSpace)
    saveFile(testSpace_path, testSpace_out)
    # 导入训练集的词袋
    trainbunch = readBunch(trainSpacePath)
    # 使用TfidfVectorizer初始化向量空间模型  使用训练集词袋向量
    vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5,
                                 vocabulary=trainbunch.vocabulary)
    transformer = TfidfTransformer()
    testSpace.tdm = vectorizer.fit_transform(bunch.contents)
    testSpace.vocabulary = trainbunch.vocabulary
    testSpace_arr = str(testSpace.tdm)
    trainbunch_vocabulary = str(trainbunch.vocabulary)
    saveFile(testSpace_arr_path, testSpace_arr)
    saveFile(trainbunch_vocabulary_path, trainbunch_vocabulary)
    # 持久化
    writeBunch(testSpacePath, testSpace)


def bayesAlgorithmDirs(trainPath, testPath, tfidfspace_out_arr_path,
                   tfidfspace_out_word_path, testspace_out_arr_path,
                   testspace_out_word_apth):
    trainSet = readBunch(trainPath)
    testSet = readBunch(testPath)
    clf = MultinomialNB(alpha=0.001).fit(trainSet.tdm, trainSet.label)
    # alpha:0.001 alpha 越小，迭代次数越多，精度越高
    # print(shape(trainSet.tdm))  #输出单词矩阵的类型
    # print(shape(testSet.tdm))
    '''处理bat文件'''
    tfidfspace_out_arr = str(trainSet.tdm)  # 处理
    tfidfspace_out_word = str(trainSet)
    saveFile(tfidfspace_out_arr_path, tfidfspace_out_arr)  # 矩阵形式的train_set.txt
    saveFile(tfidfspace_out_word_path, tfidfspace_out_word)  # 文本形式的train_set.txt

    testspace_out_arr = str(testSet)
    testspace_out_word = str(testSet.label)
    saveFile(testspace_out_arr_path, testspace_out_arr)
    saveFile(testspace_out_word_apth, testspace_out_word)

    '''处理结束'''
    predicted = clf.predict(testSet.tdm)
    total = len(predicted)
    rate = 0
    for flabel, fileName, expct_cate in zip(testSet.label, testSet.filenames, predicted):
        if flabel != expct_cate:
            rate += 1
            #print(fileName, ":实际类别：", flabel, "-->预测类别：", expct_cate)
        print(fileName, ":实际类别：", flabel, "-->预测类别：", expct_cate)
    print("erroe rate:", float(rate) * 100 / float(total), "%")
    return predicted

def bayesAlgorithm(trainPath, testPath, tfidfspace_out_arr_path,
                   tfidfspace_out_word_path, testspace_out_arr_path,
                   testspace_out_word_apth):
    trainSet = readBunch(trainPath)
    testSet = readBunch(testPath)
    clf = MultinomialNB(alpha=0.001).fit(trainSet.tdm, trainSet.label)
    # alpha:0.001 alpha 越小，迭代次数越多，精度越高
    # print(shape(trainSet.tdm))  #输出单词矩阵的类型
    # print(shape(testSet.tdm))
    '''处理bat文件'''
    tfidfspace_out_arr = str(trainSet.tdm)  # 处理
    tfidfspace_out_word = str(trainSet)
    saveFile(tfidfspace_out_arr_path, tfidfspace_out_arr)  # 矩阵形式的train_set.txt
    saveFile(tfidfspace_out_word_path, tfidfspace_out_word)  # 文本形式的train_set.txt

    testspace_out_arr = str(testSet)
    testspace_out_word = str(testSet.label)
    saveFile(testspace_out_arr_path, testspace_out_arr)
    saveFile(testspace_out_word_apth, testspace_out_word)

    '''处理结束'''
    predicted = clf.predict(testSet.tdm)
    # total = len(predicted)
    # rate = 0
    numlist=[]
    for flabel, fileName, expct_cate in zip(testSet.label, testSet.filenames, predicted):
        # if flabel != expct_cate:
        #     rate += 1
            #print(fileName, ":实际类别：", flabel, "-->预测类别：", expct_cate)
        # print(fileName, "-->预测类别：", expct_cate)
        numlist.append(int(fh.get_path_file_basename(fileName)))
    # print("erroe rate:", float(rate) * 100 / float(total), "%")
    return [predicted[one] for one in np.argsort(numlist)]

# 分词，第一个是分词输入，第二个参数是结果保存的路径

def predict_file_by_dirs(datapath,test_path,stopwords=r"I:\查阅\python\文本分类\Before\stop_words_ch.txt"):
    stopWord_path = stopwords
    '''
    以上三个文件路径是已存在的文件路径，下面的文件是运行代码之后生成的文件路径
    dat文件是为了读取方便做的，txt文件是为了给大家展示做的，所以想查看分词，词频矩阵
    词向量的详细信息请查看txt文件，dat文件是通过正常方式打不开的
    '''
    if (os.path.exists("./txttypeset/")):
        fh.remove_point_dirs("./txttypeset/")
    test_split_dat_path = "./txttypeset/test_set.dat"  # 测试集分词bat文件路径
    testspace_dat_path = "./txttypeset/testspace.dat"  # 测试集输出空间矩阵dat文件
    train_dat_path = "./txttypeset/train_set.dat"  # 读取分词数据之后的词向量并保存为二进制文件
    tfidfspace_dat_path = "./txttypeset/tfidfspace.dat"  # tf-idf词频空间向量的dat文件
    '''
    以上四个为dat文件路径，是为了存储信息做的，不要打开
    '''
    test_split_path = './txttypeset/split/test_split/'  # 测试集分词路径
    split_datapath = "./txttypeset/split/split_data/"  # 对原始数据分词之后的数据路径
    '''
    以上两个路径是分词之后的文件路径，大家可以生成之后自行打开查阅学习
    '''
    tfidfspace_path = "./txttypeset/tfidfspace.txt"  # 将TF-IDF词向量保存为txt，方便查看
    tfidfspace_arr_path = "./txttypeset/tfidfspace_arr.txt"  # 将TF-IDF词频矩阵保存为txt，方便查看
    tfidfspace_vocabulary_path = "./txttypeset/tfidfspace_vocabulary.txt"  # 将分词的词汇统计信息保存为txt，方便查看
    testSpace_path = "./txttypeset/testSpace.txt"  # 测试集分词信息
    testSpace_arr_path = "./txttypeset/testSpace_arr.txt"  # 测试集词频矩阵信息
    trainbunch_vocabulary_path = "./txttypeset/trainbunch_vocabulary.txt"  # 所有分词词频信息
    tfidfspace_out_arr_path = "./txttypeset/tfidfspace_out_arr.txt"  # tfidf输出矩阵信息
    tfidfspace_out_word_path = "./txttypeset/tfidfspace_out_word.txt"  # 单词形式的txt
    testspace_out_arr_path = "./txttypeset/testspace_out_arr.txt"  # 测试集输出矩阵信息
    testspace_out_word_apth = "./txttypeset/testspace_out_word.txt"  # 测试界单词信息
    '''
    以上10个文件是dat文件转化为txt文件，大家可以查询信息，这是NLP（自然语言处理）非常珍贵的资源
    '''
    stopWordList = getStopWord(stopWord_path)  # 获取停用词表

    # 输入训练集
    segText(datapath,  # 读入数据
            split_datapath)  # 输出分词结果
    bunchSave(split_datapath,  # 读入分词结果
              train_dat_path)  # 输出分词向量
    getTFIDFMat(train_dat_path,  # 读入分词的词向量
                stopWordList,  # 获取停用词表
                tfidfspace_dat_path,  # tf-idf词频空间向量的dat文件
                tfidfspace_path,  # 输出词频信息txt文件
                tfidfspace_arr_path,  # 输出词频矩阵txt文件
                tfidfspace_vocabulary_path)  # 输出单词txt文件
    '''
    测试集的每个函数的参数信息请对照上面的各个信息，是基本相同的
    '''
    # # 输入测试集
    segText(test_path,
            test_split_path)  # 对测试集读入文件，输出分词结果
    bunchSave(test_split_path,
              test_split_dat_path)  #
    getTestSpace(test_split_dat_path,
                 tfidfspace_dat_path,
                 stopWordList,
                 testspace_dat_path,
                 testSpace_path,
                 testSpace_arr_path,
                 trainbunch_vocabulary_path)  # 输入分词文件，停用词，词向量，输出特征空间(txt,dat文件都有)
    return bayesAlgorithmDirs(tfidfspace_dat_path,
                   testspace_dat_path,
                   tfidfspace_out_arr_path,
                   tfidfspace_out_word_path,
                   testspace_out_arr_path,
                   testspace_out_word_apth)



def save_tfidfmodel(astrlist,aresultlist,stopwords=r"I:\查阅\python\文本分类\Before\stop_words_ch.txt"):
    stopWord_path = stopwords
    if (os.path.exists("./txttypeset/")):
        fh.remove_point_dirs("./txttypeset/")
    train_dat_path = "./txttypeset/train_set.dat"  # 读取分词数据之后的词向量并保存为二进制文件
    tfidfspace_dat_path = "./txttypeset/tfidfspace.dat"  # tf-idf词频空间向量的dat文件
    split_datapath = "./txttypeset/split/split_data/"  # 对原始数据分词之后的数据路径
    tfidfspace_path = "./txttypeset/tfidfspace.txt"  # 将TF-IDF词向量保存为txt，方便查看
    tfidfspace_arr_path = "./txttypeset/tfidfspace_arr.txt"  # 将TF-IDF词频矩阵保存为txt，方便查看
    tfidfspace_vocabulary_path = "./txttypeset/tfidfspace_vocabulary.txt"  # 将分词的词汇统计信息保存为txt，方便查看
    stopWordList = getStopWord(stopWord_path)  # 获取停用词表
    # 输入训练集
    segTextByTxtAndResult(astrlist,  # 读入数据
                          aresultlist,
                          split_datapath)  # 输出分词结果
    bunchSave(split_datapath,  # 读入分词结果
              train_dat_path)  # 输出分词向量
    getTFIDFMat(train_dat_path,  # 读入分词的词向量
                stopWordList,  # 获取停用词表
                tfidfspace_dat_path,  # tf-idf词频空间向量的dat文件
                tfidfspace_path,  # 输出词频信息txt文件
                tfidfspace_arr_path,  # 输出词频矩阵txt文件
                tfidfspace_vocabulary_path)  # 输出单词txt文件






def predict_strlist(astrlist,aresultlist,predictlist,stopwords=r"I:\查阅\python\文本分类\Before\stop_words_ch.txt"):
    stopWord_path = stopwords
    '''
    以上三个文件路径是已存在的文件路径，下面的文件是运行代码之后生成的文件路径
    dat文件是为了读取方便做的，txt文件是为了给大家展示做的，所以想查看分词，词频矩阵
    词向量的详细信息请查看txt文件，dat文件是通过正常方式打不开的
    '''
    if(os.path.exists("./txttypeset/")):
        fh.remove_point_dirs("./txttypeset/")
    test_split_dat_path = "./txttypeset/test_set.dat"  # 测试集分词bat文件路径
    testspace_dat_path = "./txttypeset/testspace.dat"  # 测试集输出空间矩阵dat文件
    train_dat_path = "./txttypeset/train_set.dat"  # 读取分词数据之后的词向量并保存为二进制文件
    tfidfspace_dat_path = "./txttypeset/tfidfspace.dat"  # tf-idf词频空间向量的dat文件
    '''
    以上四个为dat文件路径，是为了存储信息做的，不要打开
    '''
    test_split_path = './txttypeset/split/test_split/'  # 测试集分词路径
    split_datapath = "./txttypeset/split/split_data/"  # 对原始数据分词之后的数据路径
    '''
    以上两个路径是分词之后的文件路径，大家可以生成之后自行打开查阅学习
    '''
    tfidfspace_path = "./txttypeset/tfidfspace.txt"  # 将TF-IDF词向量保存为txt，方便查看
    tfidfspace_arr_path = "./txttypeset/tfidfspace_arr.txt"  # 将TF-IDF词频矩阵保存为txt，方便查看
    tfidfspace_vocabulary_path = "./txttypeset/tfidfspace_vocabulary.txt"  # 将分词的词汇统计信息保存为txt，方便查看
    testSpace_path = "./txttypeset/testSpace.txt"  # 测试集分词信息
    testSpace_arr_path = "./txttypeset/testSpace_arr.txt"  # 测试集词频矩阵信息
    trainbunch_vocabulary_path = "./txttypeset/trainbunch_vocabulary.txt"  # 所有分词词频信息
    tfidfspace_out_arr_path = "./txttypeset/tfidfspace_out_arr.txt"  # tfidf输出矩阵信息
    tfidfspace_out_word_path = "./txttypeset/tfidfspace_out_word.txt"  # 单词形式的txt
    testspace_out_arr_path = "./txttypeset/testspace_out_arr.txt"  # 测试集输出矩阵信息
    testspace_out_word_apth = "./txttypeset/testspace_out_word.txt"  # 测试界单词信息
    '''
    以上10个文件是dat文件转化为txt文件，大家可以查询信息，这是NLP（自然语言处理）非常珍贵的资源
    '''
    stopWordList = getStopWord(stopWord_path)  # 获取停用词表

    # 输入训练集
    segTextByTxtAndResult(astrlist,  # 读入数据
            aresultlist,
            split_datapath)  # 输出分词结果
    bunchSave(split_datapath,  # 读入分词结果
              train_dat_path)  # 输出分词向量
    getTFIDFMat(train_dat_path,  # 读入分词的词向量
                stopWordList,  # 获取停用词表
                tfidfspace_dat_path,  # tf-idf词频空间向量的dat文件
                tfidfspace_path,  # 输出词频信息txt文件
                tfidfspace_arr_path,  # 输出词频矩阵txt文件
                tfidfspace_vocabulary_path)  # 输出单词txt文件
    '''
    测试集的每个函数的参数信息请对照上面的各个信息，是基本相同的
    '''
    # # 输入测试集
    segTextByTxt(predictlist,
            test_split_path)  # 对测试集读入文件，输出分词结果
    bunchSave(test_split_path,
              test_split_dat_path)  #
    getTestSpace(test_split_dat_path,
                 tfidfspace_dat_path,
                 stopWordList,
                 testspace_dat_path,
                 testSpace_path,
                 testSpace_arr_path,
                 trainbunch_vocabulary_path)  # 输入分词文件，停用词，词向量，输出特征空间(txt,dat文件都有)
    return bayesAlgorithm(tfidfspace_dat_path,
                   testspace_dat_path,
                   tfidfspace_out_arr_path,
                   tfidfspace_out_word_path,
                   testspace_out_arr_path,
                   testspace_out_word_apth)
def predict_strlist_only(predictlist,stopwords=r"I:\查阅\python\文本分类\Before\stop_words_ch.txt"):
    stopWord_path = stopwords
    '''
    以上三个文件路径是已存在的文件路径，下面的文件是运行代码之后生成的文件路径
    dat文件是为了读取方便做的，txt文件是为了给大家展示做的，所以想查看分词，词频矩阵
    词向量的详细信息请查看txt文件，dat文件是通过正常方式打不开的
    '''
    test_split_dat_path = "./txttypeset/test_set.dat"  # 测试集分词bat文件路径
    testspace_dat_path = "./txttypeset/testspace.dat"  # 测试集输出空间矩阵dat文件
    # train_dat_path = "./txttypeset/train_set.dat"  # 读取分词数据之后的词向量并保存为二进制文件
    tfidfspace_dat_path = "./txttypeset/tfidfspace.dat"  # tf-idf词频空间向量的dat文件
    '''
    以上四个为dat文件路径，是为了存储信息做的，不要打开
    '''
    test_split_path = './txttypeset/split/test_split/'  # 测试集分词路径
    if(os.path.exists(test_split_path)):
        fh.remove_point_dirs(test_split_path)
    # split_datapath = "./txttypeset/split/split_data/"  # 对原始数据分词之后的数据路径
    '''
    以上两个路径是分词之后的文件路径，大家可以生成之后自行打开查阅学习
    '''
    # tfidfspace_path = "./txttypeset/tfidfspace.txt"  # 将TF-IDF词向量保存为txt，方便查看
    # tfidfspace_arr_path = "./txttypeset/tfidfspace_arr.txt"  # 将TF-IDF词频矩阵保存为txt，方便查看
    # tfidfspace_vocabulary_path = "./txttypeset/tfidfspace_vocabulary.txt"  # 将分词的词汇统计信息保存为txt，方便查看
    testSpace_path = "./txttypeset/testSpace.txt"  # 测试集分词信息
    testSpace_arr_path = "./txttypeset/testSpace_arr.txt"  # 测试集词频矩阵信息
    trainbunch_vocabulary_path = "./txttypeset/trainbunch_vocabulary.txt"  # 所有分词词频信息
    tfidfspace_out_arr_path = "./txttypeset/tfidfspace_out_arr.txt"  # tfidf输出矩阵信息
    tfidfspace_out_word_path = "./txttypeset/tfidfspace_out_word.txt"  # 单词形式的txt
    testspace_out_arr_path = "./txttypeset/testspace_out_arr.txt"  # 测试集输出矩阵信息
    testspace_out_word_apth = "./txttypeset/testspace_out_word.txt"  # 测试界单词信息
    '''
    以上10个文件是dat文件转化为txt文件，大家可以查询信息，这是NLP（自然语言处理）非常珍贵的资源
    '''
    stopWordList = getStopWord(stopWord_path)  # 获取停用词表


    '''
    测试集的每个函数的参数信息请对照上面的各个信息，是基本相同的
    '''
    # # 输入测试集
    segTextByTxt(predictlist,
            test_split_path)  # 对测试集读入文件，输出分词结果
    bunchSave(test_split_path,
              test_split_dat_path)  #
    getTestSpace(test_split_dat_path,
                 tfidfspace_dat_path,
                 stopWordList,
                 testspace_dat_path,
                 testSpace_path,
                 testSpace_arr_path,
                 trainbunch_vocabulary_path)  # 输入分词文件，停用词，词向量，输出特征空间(txt,dat文件都有)
    result=bayesAlgorithm(tfidfspace_dat_path,
                   testspace_dat_path,
                   tfidfspace_out_arr_path,
                   tfidfspace_out_word_path,
                   testspace_out_arr_path,
                   testspace_out_word_apth)
    if (os.path.exists(test_split_path)):
        fh.remove_point_dirs(test_split_path)
    return result