#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/19 8:00
#@Author: hdq
#@File  : splitwordtype.py

import jieba_fast as jieba
import filehandle as fh

#无监督根据文本txt切割成N个类别
def kmeans_spiltouttxtfile(needspiltfile,spilttype=10,stopwords=r"./stop_words_ch.txt"):
    f1=open(needspiltfile,"r",encoding='utf-8',errors='ignore')
    middlespiltfilt=fh.get_path_file_subpath(needspiltfile)+"/"+fh.get_path_file_completebasename(needspiltfile)+"temp"
    f2=open(middlespiltfilt,'w',encoding='utf-8',errors='ignore')
    for line in f1:
        seg_list = jieba.cut(line, cut_all=False)
        w=(" ".join(seg_list)).replace("\t\t\t","\t")
        f2.write(w)
        # print(w)
    f1.close()
    f2.close()
    #取需要分词的内容
    titles=open(middlespiltfilt,encoding='utf-8',errors='ignore').read().split('\n')
    #查看内容，这里是一个list,list里面每个原素是分好的标题，查看下长度看有没有错误
    #titles
    #len(titles)
    #构建停词函数，停词表是自己在网上搜的
    def get_custom_stopwords(stop_words_file):
        with open(stop_words_file,encoding='utf-8')as f:
            stopwords=f.read()
        stopwords_list=stopwords.split('\n')
        custom_stopwords_list=[i for i in stopwords_list]
        return custom_stopwords_list
    #停用词函数调用
    stop_words_file=stopwords
    stopwords=get_custom_stopwords(stop_words_file)
    # print(stopwords)
    #查看停用词，也是list格式
    #stopwords
    #构建词向量，也就是把分好的次去除停词转化成kmeans可以接受的形式
    from sklearn.feature_extraction.text import CountVectorizer
    count_vec=CountVectorizer(stop_words=stopwords)
    km_matrix= count_vec.fit_transform(titles)
    # print(km_matrix.shape)
    #查看词向量
    #print(km_matrix.toarray())
    #开始聚类啦
    from sklearn.cluster import KMeans
    num_clusters = spilttype #聚为四类，可根据需要修改
    km = KMeans(n_clusters=num_clusters)
    km.fit(km_matrix)
    clusters = km.labels_.tolist()
    #查看聚类的结果，是list,这里省略，看看长度是不是和title一样就行啦
    #len(clusters)
    #最后把聚类结果写在一个新的txt里面
    return clusters


#无监督根据字符串切割成N个类别
def kmeans_spiltoutbystr(strlist,spilttype=10,stopwords=r"./stop_words_ch.txt"):
    f1=strlist
    middlespiltfilt="./tempspilt.txt"
    f2=open(middlespiltfilt,'w',encoding='utf-8',errors='ignore')
    for one in range(len(f1)):
        line=f1[one]
        seg_list = jieba.cut(line, cut_all=False)
        w=(" ".join(seg_list)).replace("\t\t\t","\t")
        f2.write(w)
        if(one!=len(f1)-1):
            f2.write("\n")
        # print(w)
    f2.close()
    #取需要分词的内容
    titles=open(middlespiltfilt,encoding='utf-8',errors='ignore').read().split('\n')
    #查看内容，这里是一个list,list里面每个原素是分好的标题，查看下长度看有没有错误
    #titles
    #len(titles)
    #构建停词函数，停词表是自己在网上搜的
    def get_custom_stopwords(stop_words_file):
        with open(stop_words_file,encoding='utf-8')as f:
            stopwords=f.read()
        stopwords_list=stopwords.split('\n')
        custom_stopwords_list=[i for i in stopwords_list]
        return custom_stopwords_list
    #停用词函数调用
    stop_words_file=stopwords
    stopwords=get_custom_stopwords(stop_words_file)
    # print(stopwords)
    #查看停用词，也是list格式
    #stopwords
    #构建词向量，也就是把分好的次去除停词转化成kmeans可以接受的形式
    from sklearn.feature_extraction.text import CountVectorizer
    count_vec=CountVectorizer(stop_words=stopwords)
    km_matrix= count_vec.fit_transform(titles)
    # print(km_matrix.shape)
    #查看词向量
    #print(km_matrix.toarray())
    #开始聚类啦
    from sklearn.cluster import KMeans
    num_clusters = spilttype #聚为四类，可根据需要修改
    km = KMeans(n_clusters=num_clusters)
    km.fit(km_matrix)
    clusters = km.labels_.tolist()
    #查看聚类的结果，是list,这里省略，看看长度是不是和title一样就行啦
    #len(clusters)
    #最后把聚类结果写在一个新的txt里面
    return clusters

# import fenci as fc
# import wordvec as wv
# import knnweb
# def form_a_type_b(bseglist,aseglist,aresultlist,stopwords=r"I:\查阅\python\文本分类\Before\stop_words_ch.txt"):
#     lines = fc.cutlines(aseglist, stopwordfile=stopwords)
#     model = wv.train_model(lines)
#     ve1 = wv.get_vector(model)
#     blines = fc.cutlines(bseglist, stopwordfile=stopwords)
#     model2 = wv.train_model(blines)
#     ve2 = wv.get_vector(model2)
#     result = knnweb.knn(ve1, aresultlist, ve2)
#     return result