#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/9 19:15
# @Author: zhangtao
# @File  : arraychanger.py
import pandas as pd
import numpy as np


def list_from_pdframe(pdlist):
    return pdlist.values


def list_add_list(*param):
    return np.c_[param]

#解开内序列
def out_init_list(list):
    result=[]
    for one in list:
        result.append(*one)
    return result


# #拼接二维数组列内元素
# def list_double_add_row(list1,list2):
#     list3=[]
#     for one in range(len(list1)):
#         list3.append([*list1[one],*list2[one]])
#     return list3
# def list_single_add_row(list1,list2):
#     list3=[]
#     for one in range(len(list1)):
#         list3.append([list1[one],*list2[one]])
#     return list3

# # train info:pdframe
# def list_pdframe_get_range(pdlist, start, end):
#     return pdlist.iloc[:, start:end].values

#读取csv并设置对应的值
def pd_get_from_label(csvpath,indexcols,title=None,dtype=np.str):
    return pd.read_csv(csvpath,index_col=indexcols,names=title,dtype=dtype)


# # 去除csv重复项
# def csv_remove_repeat(csvpath, rowlist, outpath, header=True, index=False, keep='last', encoding='utf-8',
#                       replace=False):
#     frame = pd.read_csv(csvpath, engine='python')
#     data = frame.drop_duplicates(subset=rowlist, keep=keep, inplace=replace)
#     data.to_csv(outpath, encoding=encoding, header=header, index=index)


def pdframe_readcsv(csvpath,header,low_memory=False,encoding="utf-8"):
    return pd.read_csv(csvpath, header=header,low_memory=low_memory,encoding=encoding)


# 获得csv文件的第几列到第几列的list数据
def list_csv_reader_range(csvpath,  start=None, end=None,header=0,returnpd=False,encoding="utf-8"):
    dataset = pdframe_readcsv(csvpath,header=header,encoding=encoding)
    if not returnpd:
        return dataset.iloc[:, start:end].values
    else:
        return dataset.iloc[:, start:end]


# 获得csv文件的对应标签的数据list
def list_csv_reader_label(csvpath, str,header=0):
    dataset = pdframe_readcsv(csvpath,header=header)
    return dataset[str].values

# 获得csv文件的对应标签的数据list
def list_csv_reader_label_post(csvpath, str,header=0):
    dataset = pdframe_readcsv(csvpath,header=header)[str].values
    result=[[one] for one in dataset]
    return result




# # 将对应pdframe中的范围数据转化为list
# def list_pdframe_range(pdlist,start,end):
#     return pdlist.iloc[:,start:end].values


# # 将对应pdframe中的对应label数据转化为list
# def list_pdframe_label(pdlist,str):
#     return pdlist[str].values
#
# import  filehandle as fh
# # 返回对应标签对应的元素集合
# def list_pdframe_map_value(keylist,pdlist,labels,IntAble=True):
#     num=len(keylist)
#     if(IntAble):
#         return [pdlist.loc[int(keylist[one]),labels] for one in range(num)]
#     else:
#         print([keylist[one] for one in range(num) if keylist[one] not in pdlist.index])
#         return [pdlist.loc[keylist[one],labels] for one in range(num) if keylist[one] in pdlist.index]

# #降维度
#
# from tkinter import _flatten
#
# def min_drop_list(strlist):
#     return list(_flatten(strlist))
#
# #根据csv文件读取对应list信息 第一行默认为key
# def list_label_from_csvcols(file_list,pointcsvpath,handleTobase=True,IntAble=True):
#     if(handleTobase):
#         labelkeys=[fh.get_path_file_basename(one) for one in file_list]
#     else:
#         labelkeys=file_list
#     labelsmap = pd_get_from_label(pointcsvpath, 'id', ['id', 'str'])
#     return list_pdframe_map_value(labelkeys, labelsmap, 'str',IntAble=IntAble)
#
# import random
# #获得随机排序序号
# def get_random_ids(list):
#     shuffle=random.sample(list,len(list))
#     return [list.index(one) for one in shuffle]
# #根据序号获得对应列表值
# def get_lists_by_ids(lists,ids):
#     result=[]
#     for one in lists:
#         subresult=[]
#         for two in ids:
#             subresult.append(one[two])
#         result.append(subresult)
#     return result

