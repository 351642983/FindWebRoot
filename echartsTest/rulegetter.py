#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/23 21:11
#@Author: hdq
#@File  : rulegetter.py


import lightgbmDemo as lgb
import timegetter as tg
import numpy as np
import splitwordtype as swt #1
import arraychanger as ac
import filehandle as fh
import unrelation as ur
import txtSetType as tst
import networkhandle as nh
import networkx as nx
import re
import pandas as pd
import bidirectional_rnn as brnn
import cnnweb
import tfhandle as th

#predict_csv和train_model中的type属性作为选择算法的种类
#ptype值含义  0表示使用梯度上升算法gbdt(以直方图算法的决策树为基础) 1表示使用BRNN神经网络 2表示使用CNN网络
#全局控制使用算法类型
#经过测试的 对应的算法准确性和速度的排名 决策树>CNN>BRNN
ptype=0

#总开关（False则为单元测试模式，True为预测模式）
power=True

#测试集F1值：F1=2*准确率*召回率/(准确率+召回率)，其中准确率=准确定位根因的组数/定位根因的组数,召回率=准确定位根因的组数/实际存在根因的组数
#是否是第一次运行 第一次运行的时候将这个参数改为True 是否训练模型
trainmodel=False
#当trainmodel为True时，是否以开发者测试模式开启训练模型,Fasle表示训练标准模型(开发者使用，平常预测请吧下面的onlytest设置为true)
#表示训练（除了范围starttest至starttest+testnum)的数据，同时预测（范围starttest至starttest+testnum)的数据到predict.csv中
testmode=False
#当trainmodel为False时，是否依旧开启测试,当testmode为True时，则表示预测全部数据
onlytest=False
#开始预测位置，starttest之后开始预测（范围starttest至starttest+testnum)
starttest=0
#预测个数
testnum=20
#训练时训练分类模型
typemodel=False
#设置训练数据的地址
train_data=r"./train"
#设置测试集数据的地址
test_data=r"./test"
#语义切割类别 一般来说类别越多 预测相对越准确 但太大会过拟合
splitcount=29
#节点json所在文件夹
pointfile=r"./topology"
#停用词表
stopwords=r"./stop_words_ch.txt"
#输出训练集预测概率文件
outpredictcsv=r"./predict.csv"

#根因对应表参数设置区域
#是否开启对应表完全根因表检测
rootpointercheck=True
#完全根因表检测阈值
rootpointernum=3


#决策树参数设置区域
#决策树模型路径
lgb_models="./lightgbmmodels.txt"
#训练模型的时候开启GridCV搜索，交叉验证
gridcvsearch=False
#若使用决策树模型，对应决策树训练次数
echos=150
#决策树参数
params = {
        'task': 'train',
        'boosting_type': 'gbdt',  # GBDT算法为基础
        'objective': 'binary',
        'metric': 'auc',  # 评判指标
        'max_bin': 255,  # 大会有更准的效果,更慢的速度
        'learning_rate': 0.03,  # 学习率
        'num_leaves': 13,  # 大会更准,但可能过拟合
        'max_depth': 6,  # 小数据集下限制最大深度可防止过拟合,小于0表示无限制
        'feature_fraction': 0.9,  # 防止过拟合
        'bagging_freq': 25,  # 防止过拟合
        'bagging_fraction': 0.7,  # 防止过拟合
        'min_data_in_leaf': 10,  # 防止过拟合
        'min_split_gain': 0.0,
        'lambda_l2': 0.1,
        'lambda_l1': 0.1,
        'is_unbalance': False,
        # 'min_sum_hessian_in_leaf': 0.5,  # 防止过拟合
        'header': False  # 数据集是否带表头
    }


#BRNN参数设置区域
#BRNN模型存储位置
brnn_model="brnn/predictweb"
#BRNN模型numhidden
brnn_numhidden=1024
#BRNN模型每次训练的batch
brnn_batch=1024
#BRNN训练次数
brnn_echo=20000
#BRNN每训练轮回显示准确度和损失
brnn_show=100

#CNN参数设置区域
#CNN模型保存位置
cnn_model="cnn/predictweb"
#CNN网络训练次数
cnn_echo=700
#CNN网络通道
cnn_channel=[32,64,128]
#CNN的Dropout设置
cnn_dropout=0.7
#CNN的学习率
cnn_learningrate=0.001
#CNN使用sigmoid函数 否的话使用softmax
cnn_sigmoid=False
#CNN步长
cnn_ride=[1,1,1]
#CNN卷积大小
cnn_filter=[1,1,1]





#加载根因节点对应表
def load_rules_pointer():
    global des_warnings, des_root, des_unroot, relation,node_list,node_root,node_unroot,sys_list,sys_root,sys_unroot
    print("获取具体根因对应表")
    des_warnings, des_root, des_unroot,node_list,node_root,node_unroot,sys_list,sys_root,sys_unroot = get_rule_descript()
    print("获取具体根因对应表加载成功")
    print("获取笼统根因对应表")
    relation = get_rule_total()
    print("获取笼统根因对应表加载成功")
    return True

#获取告警信息对应的节点值，若无则返回-1
def get_warninginfo_node(warninginfo):
    matcher=re.search(r"(node_\d*)",warninginfo)
    if(matcher):
        return matcher.group(0)
    else:
        return -1

#------------------------------------------传入数据修改区域-------------------------

#分析得到csv文件的基本信息
def get_csv_baseinfo(csvfilelist,returnlabels=False):
    resultcsvinfos=[]
    labels = []
    allnodelist=nh.get_every_point(pointfile)

    for i in csvfilelist:
        tempinfo=ac.pdframe_readcsv(i,0)
        # pd.Series(tempinfo["triggername"].value_counts(), index=[''])
        counters=tempinfo["triggername"].value_counts()
        #去重
        tempinfo = fh.csv_remove_repeat(i,['sysEname',"triggername"])
        tempinfo.sort_index()
        trechargerinfo=tempinfo.iloc[:,1:4].values.T
        csvweb=nh.create_digraph_bydir(pointfile)
        # print(i,list(set(nh.get_every_point(pointfile))-set(trechargerinfo[0])-set([one.split(" ",1)[0][2:] for one in trechargerinfo[2]])))
        csvweb.remove_nodes_from(list(set(allnodelist)-set(trechargerinfo[0])-set([one.split(" ",1)[0][2:] for one in trechargerinfo[2]])))
        if(returnlabels):
            labels += tempinfo.loc[:,"is_root"].values.tolist()
        nowinfo= tempinfo.iloc[:,1:4].values.tolist()



        for i,one in enumerate(nowinfo):
            splittempinfo=one[2].split(" ", 1)
            #one[0][4:] 系统
            #splittempinfo[0][7:] 主机号
            #splittempinfo[1] 告警信息


            node=get_warninginfo_node(splittempinfo[1])
            pnode=-1
            minlen=0
            if(node!=-1):
                pnode=int(node[5:])
                minlen=nx.dijkstra_path_length(csvweb, source=splittempinfo[0][2:], target=node)
            # print(splittempinfo[1]+":"+str(node))#测试
            resultcsvinfos.append(
                [
                    one[0][4:],#one[0][4:]
                    splittempinfo[0][7:],
                    tg.change_time_format(one[1], "%Y-%m-%d %H:%M:%S", "%H"),
                    splittempinfo[1],
                    pnode,
                    minlen,
                    csvweb.out_degree(splittempinfo[0][2:]),
                    csvweb.in_degree(splittempinfo[0][2:]),
                    tg.get_timestr_to_week(one[1],"%Y-%m-%d %H:%M:%S"),
                    tg.change_time_format(one[1], "%Y-%m-%d %H:%M:%S", "%d"),
                    pd.Series(counters, index=[one[2]]),
                    one[1],
                    i,
                ])

    resultcsvinfos=np.asarray(resultcsvinfos)
    if(returnlabels):
        return resultcsvinfos,labels
    else:
        return resultcsvinfos


#设置重要程度列名
headers=[
    '系统号',  #1
    '主机号',  #2
    # '时间-时', #3
    "告警信息分类号", #4
    "告警根因数",  #5
    # "告警非根因数", #6
    # "主机根因数",  #7
    # "主机非根因数", #8
    # "目标主机",   #9
    # "最短距离", #10
    # "当前出度数",#11
    # "当前入度数", #12
    "时间-星期",    #13
    # "时间-号", #14
    # "系统跟因数",#15
    # "系统非根因数",#16
    "节点csv出现次数", #17
    # "文件中首次出现位置",#18
]
#将读取的csv文件所有信息进行二次处理，例如添加信息，标准化信息--信息拓展
def handle_csvinfo_tostandard(csvinfos,warninginfos_num):
    #告警信息 根因次数 根因次数 笼统根因关系 节点列表 节点根因次数 节点非根因次数 系统 系统根因数 系统非根因数
    global des_warnings, des_root, des_unroot, relation,node_list,node_root,node_unroot,sys_list,sys_root,sys_unroot

    totaladd=np.c_[csvinfos,warninginfos_num]
    warninginfos_nump=len(csvinfos[0])
    result=[
        list(map(int, [
            one[0], #1
            one[1],#2
            # one[2],#3
            one[warninginfos_nump],#4
            des_root[ishave_index(des_warnings,one[3])],#5
            # des_unroot[ishave_index(des_warnings,one[3])],#6
            # node_root[node_list.index(int(one[1]))],#7
            # node_unroot[node_list.index(int(one[1]))],#8
            # one[4],#9
            # one[5],#10
            # one[6],#11
            # one[7],#12
            one[8],#13
            # one[9],#14
            # sys_root[sys_list.index(int(one[0]))],#15
            # sys_unroot[sys_list.index(int(one[0]))],#16
            one[10],#17
            # one[12], #18
        ]))
        if (ishave_index(des_warnings, one[3]) != -1) else
        # if (ishave_index(des_warnings, one[3]) == -2) else
        list(map(int, [
            one[0],#1
            one[1],#2
            # one[2],#3
            one[warninginfos_nump],#4
            relation[int(one[warninginfos_nump])][0],#5
            # relation[int(one[warninginfos_nump])][1],#6
            # node_root[node_list.index(int(one[1]))],#7
            # node_unroot[node_list.index(int(one[1]))],#8
            # one[4],#9
            # one[5],#10
            # one[6],#11
            # one[7],#12
            one[8],#13
            # one[9],#14
            # sys_root[sys_list.index(int(one[0]))],#15
            # sys_unroot[sys_list.index(int(one[0]))],#16
            one[10],#17
            # one[12],#18

        ]))
        for one in totaladd
    ]
    return result

#type 0为决策树(梯度上升学习框架，直方图算法) 1为brnn(前后关联神经网络) 2为卷积神经网络
#训练模型
def train_models(type=ptype):
    # from imblearn.under_sampling import ClusterCentroids
    from imblearn.over_sampling import RandomOverSampler
    from imblearn.under_sampling import RandomUnderSampler
    # from imblearn.over_sampling import ADASYN

    # # 数据平衡操作
    # def data_balance(imagelists, labelists, over_sampling=True):
    #     if not over_sampling:
    #         return ADASYN().fit_sample(imagelists, labelists)
    #     else:
    #         cc = ClusterCentroids(random_state=0)
    #         return cc.fit_sample(imagelists, labelists)

    # 数据朴素平衡
    def data_balance_ps(imagelists, labelists, over_sampling=True):
        if (over_sampling):
            ros = RandomOverSampler(random_state=0)
            return ros.fit_sample(imagelists, labelists)
        else:
            ros = RandomUnderSampler(random_state=0)
            return ros.fit_sample(imagelists, labelists)

    csvinfos,labels,warningsnum=get_traininfos(train_data,spilttype=splitcount)
    load_rules_pointer()
    filterinfo=handle_csvinfo_tostandard(csvinfos,warningsnum)
    print("原数据长：",len(labels))
    filterinfo,labels=data_balance_ps(filterinfo,labels,True)    #非朴素上采样
    # 训练结果
    if type==0:
        bst,lgb_train= lgb.train_predict_model(
            np.asarray(filterinfo),
            np.asarray(labels),
            params,
            train_times=echos)
        print("保存lgb模型")
        lgb.save_models(bst,lgb_models)

        print("训练数据长:",len(filterinfo))
        print("标签数据长:",len(labels))
        #获得特征重要性
        important=lgb.plot_feature_importance(headers,bst)
        print("模型特征重要性:",important)
        if(gridcvsearch):
            bestparams=lgb.select_suit_parameter(lgb_train,params)
            print(bestparams)
    elif type==1:
        brnn.birnnweb(filterinfo,labels,savemodel=brnn_model,num_classes=2,num_input=1,timestep=len(headers),num_hidden=brnn_numhidden,batch_size=brnn_batch,training_step=brnn_echo,display_step=brnn_show)
        brnn.tf.reset_default_graph()
    elif type == 2:
        cnnweb.start_cnn_train_model(th.change_data_to_cnnable(filterinfo, len(headers), 1,1),
                                     [[one] for one in labels],
                                     1, 2, len(headers), 1,
                                     cnn_model,
                                     learningrate=0.001,
                                     learingtimes=cnn_echo,
                                     keep_prob=cnn_dropout,
                                     channel=1,
                                     signmoid=cnn_sigmoid,
                                     outputchannel=cnn_channel,
                                     filter=cnn_filter,
                                     ride=cnn_ride)
    return True

#-------------------------------------------------------------------

#获得训练数据 返回数据集和标签和警告信息类别
def get_traininfos(dir,spilttype):
    # csvinfos,labels=None,None
    if(testmode):
        # +fh.get_files_by_types(dir,".csv")[90:]
        csvinfos,labels=get_csv_baseinfo(fh.get_files_by_types(dir,".csv")[:starttest]+fh.get_files_by_types(dir,".csv")[starttest+testnum:],True)
    else:
        csvinfos, labels = get_csv_baseinfo(fh.get_files_by_types(dir, ".csv"), True)
    if typemodel:
        # 训练分类模型，开启这部分区域训练分类模型
        warninginfos_num=swt.kmeans_spiltoutbystr(csvinfos.T[3],spilttype=spilttype)    #Kmeans分类
        tst.save_tfidfmodel(csvinfos.T[3],warninginfos_num,stopwords=stopwords)         #保存分类模型
    else:
        warninginfos_num=tst.predict_strlist_only(csvinfos.T[3],stopwords=stopwords)
    return csvinfos,labels,warninginfos_num

#获得测试数据，用于此后的分类预测任务 返回数据集和警告信息类别
def get_testinfos(dir):
    csvinfos = get_csv_baseinfo(fh.get_files_by_types(dir,".csv"))
    warninginfos_num=tst.predict_strlist_only(csvinfos.T[3],stopwords=stopwords)    #根据分类模型预测类别
    return csvinfos,warninginfos_num


#根据list的当前位置序号，从小到大，相加对应位置list
def dlist_sort_byidlist(idlist,blist,clist):
    indexlist=np.argsort(idlist,axis=0)
    resultlist=[[0,0] for one in range(max(idlist)+1)]

    for one in range(len(indexlist)):
        i=indexlist[one]
        resultlist[idlist[i]][0]+=blist[i]
        resultlist[idlist[i]][1]+=clist[i]
    # print(blist)
    # print(clist)
    # print(resultlist)
    return resultlist



#得到笼统规则根因出现数
def get_rule_total():
    global root, unroot, unrealation
    # root, unroot, unrealation = ur.create_keypointcsv_onlywarning(train_data)
    strlist=[]
    roottimes=[]
    unroottimes=[]

    for one in root:
        tempsplit=one.split("|")
        strlist.append(tempsplit[0])
        roottimes.append(int(tempsplit[1]))
        unroottimes.append(int(tempsplit[2]))
    for one in unroot:
        tempsplit=one.split("|")
        strlist.append(tempsplit[0])
        roottimes.append(int(tempsplit[1]))
        unroottimes.append(int(tempsplit[2]))
    for one in unrealation:
        tempsplit=one.split("|")
        strlist.append(tempsplit[0])
        roottimes.append(int(tempsplit[1]))
        unroottimes.append(int(tempsplit[2]))
    numresult=tst.predict_strlist_only(strlist,stopwords=stopwords)
    # print(numresult)
    result=dlist_sort_byidlist(list(map(int,numresult)),roottimes,unroottimes)

    return result


#得到具体规则根因出现数
def get_rule_descript():
    global root, unroot, unrealation
    root, unroot, unrealation,noderoot,nodeunroot,nodeunrelation,sysroot,sysunroot,sysunrelation = ur.create_keypointcsv(train_data)

    syslist = []
    sysroottimes = []
    sysunroottimes = []
    for one in sysroot:
        tempsplit = one.split("|")
        syslist.append(int(tempsplit[0]))
        sysroottimes.append(int(tempsplit[1]))
        sysunroottimes.append(int(tempsplit[2]))
    for one in sysunroot:
        tempsplit = one.split("|")
        syslist.append(int(tempsplit[0]))
        sysroottimes.append(int(tempsplit[1]))
        sysunroottimes.append(int(tempsplit[2]))
    for one in sysunrelation:
        tempsplit = one.split("|")
        syslist.append(int(tempsplit[0]))
        sysroottimes.append(int(tempsplit[1]))
        sysunroottimes.append(int(tempsplit[2]))

    nodelist = []
    noderoottimes = []
    nodeunroottimes = []
    for one in noderoot:
        tempsplit = one.split("|")
        nodelist.append(int(tempsplit[0]))
        noderoottimes.append(int(tempsplit[1]))
        nodeunroottimes.append(int(tempsplit[2]))
    for one in nodeunroot:
        tempsplit = one.split("|")
        nodelist.append(int(tempsplit[0]))
        noderoottimes.append(int(tempsplit[1]))
        nodeunroottimes.append(int(tempsplit[2]))
    for one in nodeunrelation:
        tempsplit = one.split("|")
        nodelist.append(int(tempsplit[0]))
        noderoottimes.append(int(tempsplit[1]))
        nodeunroottimes.append(int(tempsplit[2]))

    strlist = []
    roottimes = []
    unroottimes = []
    for one in root:
        tempsplit = one.split("|")
        strlist.append(tempsplit[0])
        roottimes.append(int(tempsplit[1]))
        unroottimes.append(int(tempsplit[2]))
    for one in unroot:
        tempsplit = one.split("|")
        strlist.append(tempsplit[0])
        roottimes.append(int(tempsplit[1]))
        unroottimes.append(int(tempsplit[2]))
    for one in unrealation:
        tempsplit = one.split("|")
        strlist.append(tempsplit[0])
        roottimes.append(int(tempsplit[1]))
        unroottimes.append(int(tempsplit[2]))

    return strlist,roottimes,unroottimes,nodelist,noderoottimes,nodeunroottimes,syslist,sysroottimes,sysunroottimes




#是否有对应的标号
def ishave_index(list,ele):
    try:
        return list.index(ele)
    except ValueError:
        return -1


# #预测测试集数据
# def predict_test(is_root=False):
#     csvinfos, warningsnum = get_testinfos(test_data)
#     labels = []
#     if (is_root):
#         for i in fh.get_files_by_types(test_data, ".csv"):
#             labels += ac.out_init_list(ac.list_csv_reader_label_post(i, "is_root"))
#
#     filterinfo = handle_csvinfo_tostandard(csvinfos, warningsnum)
#     # 模型加载
#     bst=lgb.load_model(lgb_models)
#     # 预测数据
#     result=lgb.predict_label(bst,filterinfo)
#     print("预测结果长:",len(result))
#     print("预测中请稍后")
#     fh.remove_file(outpredictcsv)
#     if not (is_root):
#         fh.csv_out_onerow(outpredictcsv,["predict"])
#     else:
#         fh.csv_out_onerow(outpredictcsv, ["predict","is_root"])
#     for i in range(len(result)):
#         pred=result[i]
#         if(i!=0):
#             if(is_root):
#                 fh.appendfile(outpredictcsv,str(pred)+","+str(labels[i]),"\n")
#             else:
#                 fh.appendfile(outpredictcsv, (str(pred)), "\n")
#         else:
#             if (is_root):
#                 fh.appendfile(outpredictcsv, str(pred)+","+str(labels[i]))
#             else:
#                 fh.appendfile(outpredictcsv, (str(pred)))
#     print("预测完成")


if(power):
    # #训练模型
    if(trainmodel):
        train_models()
    else:
        load_rules_pointer()



# #根据测试数据得出根因概率
# predict_test()


#--------------------------------------------接口函数----------------------------------------

# #单个信息的预测准确率极低，未配合CSV文件，请用predict_csv来预测根因，predict_one很难达到效果
# #预测一个告警信息可能是根因的概率，返回 系统号 主机号 告警信息 概率值
# #例子：predict_one("SYS_5","2019-06-04 01:15:35","主机node_60 端口80通信异常")
# def predict_one(sys,time,nodeandwarninginfo):
#     splittempinfo = nodeandwarninginfo.split(" ", 1)
#     csvweb=nh.create_digraph_bydir(pointfile)
#     node = get_warninginfo_node(splittempinfo[1])
#     pnode = -1
#     minlen = 0
#     if (node != -1):
#         pnode = int(node[5:])
#         minlen = nx.dijkstra_path_length(csvweb, source=splittempinfo[0][2:], target=node)
#     csvinfos =[
#         sys[4:],
#         splittempinfo[0][7:],
#         tg.change_time_format(time, "%Y-%m-%d %H:%M:%S", "%H"),
#         splittempinfo[1],
#         pnode,
#         minlen,
#         csvweb.out_degree(splittempinfo[0][2:]),
#         csvweb.in_degree(splittempinfo[0][2:]),
#         tg.get_timestr_to_week(time, "%Y-%m-%d %H:%M:%S"),
#         tg.change_time_format(time, "%Y-%m-%d %H:%M:%S", "%d"),
#         20
#     ]
#     # one[0][4:] 系统
#     # splittempinfo[0][7:] 主机号
#     # splittempinfo[1] 告警信息
#
#     warninginfos_num = tst.predict_strlist_only([csvinfos[3]], stopwords=stopwords)
#     filterinfo = handle_csvinfo_tostandard([csvinfos], warninginfos_num)
#     # print(filterinfo)
#     # 模型加载
#     bst = lgb.load_model(lgb_models)
#     # 预测数据
#     result = lgb.predict_label(bst, filterinfo)
#     #系统号 主机号 告警信息 概率值
#     return filterinfo[0][0],filterinfo[0][1],csvinfos[3],result[0]

import time
#预测csv告警信息可能存在的根因，返回 有可能根因节点,概率值 以二维列表的形式返回,第一列为节点号，第二列为节点号预测值，可能存在多个 按照序号概率从大到小排列
#例子 predict=predict_csv(test_data+"/9.csv",shold=0.5)
#第一个参数为需要分析的csv文件名，第二个参数是阈值,也就是预测值超过此数的节点才被返回 0系统号 1主机号 2告警信息 3时间 4概率值
#type 0为决策树(梯度上升学习框架，直方图算法) 1为brnn(前后关联神经网络) 2为卷积神经网络预测
def predict_csv(csvfile,shold=0.5,type=ptype):
    start=time.time()
    csvinfos = get_csv_baseinfo([csvfile])
    print("文件路径："+csvfile)
    warninginfos=csvinfos.T[3]
    timeinfos=csvinfos.T[11]
    warninginfos_num = tst.predict_strlist_only(warninginfos, stopwords=stopwords)
    resultlist = []
    judgelist = []
    filterinfo = handle_csvinfo_tostandard(csvinfos, warninginfos_num)

    if rootpointercheck:
        global des_warnings, des_root, des_unroot
        for one in warninginfos:
            id=ishave_index(warninginfos.tolist(), one)
            did=ishave_index(des_warnings,one)
            if(id!= -1 and did !=-1):
                if(des_root[did]>=rootpointernum and des_unroot[did]==0):
                    if (ishave_index(judgelist, filterinfo[id][1]) == -1):
                        judgelist.append(filterinfo[id][1])
                        resultlist.append([filterinfo[id][0], filterinfo[id][1], warninginfos[id],
                                           timeinfos[id], 1.0])

    if type==0:
        # 模型加载
        bst = lgb.load_model(lgb_models)
        # 预测数据
        result = lgb.predict_label(bst, filterinfo)
        pointid=np.argsort(result)

        for subpoint in pointid[::-1]:
            if result[subpoint]<shold:
                continue
            if(ishave_index(judgelist,filterinfo[subpoint][1])==-1):
                judgelist.append(filterinfo[subpoint][1])
                resultlist.append([filterinfo[subpoint][0],filterinfo[subpoint][1],warninginfos[subpoint],timeinfos[subpoint],result[subpoint]])
                # print(filterinfo[subpoint][3]/(filterinfo[subpoint][3]+filterinfo[subpoint][4]))
                # print(filterinfo[subpoint][3],filterinfo[subpoint][4],filterinfo[subpoint][6])
    elif type==1:
        _,result=brnn.predict_withmodel(filterinfo,2,model=brnn_model,timestep=len(headers),num_input=1,num_hidden=brnn_numhidden,returnpro=True)
        result=[one[1] for one in result]
        pointid = np.argsort(result)
        for subpoint in pointid[::-1]:
            if result[subpoint] < shold:
                continue
            if (ishave_index(judgelist, filterinfo[subpoint][1]) == -1):
                judgelist.append(filterinfo[subpoint][1])
                resultlist.append([filterinfo[subpoint][0], filterinfo[subpoint][1], warninginfos[subpoint],timeinfos[subpoint], result[subpoint]])
        brnn.tf.reset_default_graph()
    elif type==2:
        _,result=cnnweb.predict_info(th.change_data_to_cnnable(filterinfo, len(headers), 1,1),
                            1, 2, len(headers), 1,
                            cnn_model,
                            keep_prob=1.0,
                            channel=1,
                            sigmiod=cnn_sigmoid,
                            outputchannel=cnn_channel,
                            filter=cnn_filter,
                            ride=cnn_ride,
                            realProb=True)
        result=[result[i][0] if _[i][0]==1 else 1.0-result[i][0] for i in range(len(result))]
        pointid = np.argsort(result)
        for subpoint in pointid[::-1]:
            if result[subpoint] < shold:
                continue
            if (ishave_index(judgelist, filterinfo[subpoint][1]) == -1):
                judgelist.append(filterinfo[subpoint][1])
                resultlist.append(
                    [filterinfo[subpoint][0], filterinfo[subpoint][1], warninginfos[subpoint], timeinfos[subpoint],
                     result[subpoint]])
        cnnweb.tf.reset_default_graph()
    spendtime =(time.time() - start)
    print("预测花费：%.2f" % spendtime, "秒 \n")
    speedlist=[spendtime] * len(resultlist)
    resultlist = np.c_[resultlist, speedlist].tolist()
    print(resultlist)
    return resultlist


#获得csv训练文件的根因节点号（非预测)
#例子：get_csv_root(train_data+"/0.csv") 返回60
def get_csv_root(csvfile):
    rootvalue=ac.out_init_list(ac.list_csv_reader_label_post(csvfile, "is_root"))
    rootid=np.argmax(rootvalue)
    warninginfos =[int(one.split(" ",1)[0][7:]) for one in ac.out_init_list(ac.list_csv_reader_range(csvfile, 3, 4).tolist())]
    if(rootvalue[rootid]==1):
        return warninginfos[rootid]
    else:
        return -1


#预测并输出一个csv文件,不能预测训练文件
def predict_to_csv(csvfile,outpredictdir,shold=0.5,type=0):
    predict=predict_csv(csvfile,shold=shold,type=type)
    # print(i, predict)
    #存储预测数据
    csvinfo=fh.csv_reader(csvfile)
    import numpy as np
    infos=np.array(csvinfo.iloc[:]).tolist()
    outpath=outpredictdir+"/" + fh.get_path_file_completebasename(csvfile)
    # fh.outfile(outpath,",".join(list(map(str,csvinfo.columns.values.tolist())))+",is_root")
    isrootinfos=[]

    print(predict)
    if(len(predict)>0):
        for one in infos:
            if int(one[3].split(" ",1)[0][7:])==predict[0][1] and predict[0][2]==one[3].split(" ",1)[1]:
                isrootinfos.append(1)
            else:
                isrootinfos.append(0)
    else:
        for one in infos:
            isrootinfos.append(0)
    csvinfo['is_root']=isrootinfos
    try:
        csvinfo.to_csv(outpath, encoding="utf_8_sig", header=True, index=False)
        return True
    except Exception:
        return False


#读取CSV的节点警告出现次序,先来先计算
def csv_waringinfos_fcfs(csvfile):
    tempinfo = fh.csv_remove_repeat(csvfile, ['sysEname', "triggername"])
    tempinfo.sort_index()
    nowinfo = tempinfo.iloc[:, 1:4].values.tolist()
    minresult=[]
    for i, one in enumerate(nowinfo):
        minresult.append([one[2],i+1])
    return minresult

#读取CSV文件的去重信息,包括出现次序
def get_enmin_csv_infos(csvfile):
    tempinfo = fh.csv_remove_repeat(csvfile, ['sysEname', "triggername"])
    nowinfo = tempinfo.iloc[:, 1:4].values.tolist()
    minresult=[]
    for i, one in enumerate(nowinfo):
        minresult.append(one+[i+1])
    return minresult

#----------------------------模型测试---------------

def init_load(ignorePar=False):
    if(testmode or onlytest or ignorePar):
        fh.remove_file(outpredictcsv)
        fileslist=None
        if onlytest or ignorePar:
            fileslist=fh.get_files_by_types(test_data,".csv")
        elif testmode:
            fileslist = fh.get_files_by_types(test_data, ".csv")[starttest:starttest + testnum]
        df = pd.DataFrame()
        filename=[]
        root_node=[]
        triggername=[]
        fileslist.sort(key=lambda elem: int(fh.get_path_file_basename(elem)))
        for subfile in fileslist:
            predict=predict_csv(subfile,0.5)
            # fh.appendfile(outpredictcsv,subfile+","+str(predict),startchar="\n")
            filename.append(fh.get_path_file_basename(subfile))
            try:
                rootname = "node_" + str(predict[0][1])
                root_node.append(rootname)
                triggername.append( "主机" + rootname + " " + predict[0][2])
            except IndexError:

                root_node.append("0")
                triggername.append("0")


        df['filename'] = filename
        df['root_node'] = root_node
        df['triggername'] = triggername
        df.to_csv(outpredictcsv, encoding="utf_8_sig", header=True, index=False)

init_load()
