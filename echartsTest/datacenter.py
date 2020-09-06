#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/5/8 13:21
#@Author: hdq
#@File  : datacenter.py
#数据处理中心，对csv中的数据进行处理之后得出统计信息。

#对应的训练集存储位置
import filehandle as fh
import numpy as np
import timegetter as tg

#获得对应训练集中所有数据
def get_basedata(basefiledir):
    allinfo=[]
    csvfilelist=fh.get_files_by_types(basefiledir,".csv")
    for i in csvfilelist:
        #去重
        tempinfo = fh.csv_remove_repeat(i,['sysEname',"triggername"])
        allinfo+=np.array(tempinfo).tolist()
    return allinfo

#获得对应告警文件文件夹中星期的根因告警数量
def get_every_weekday_roots(basefiledir):
    numlist=[]
    infos=get_basedata(basefiledir)
    for one in infos:
        if one[4]==1:
            numlist.append(tg.get_timestr_to_week(one[2],"%Y-%m-%d %H:%M:%S"))
    return list(map(numlist.count,set(numlist)))

#获得对应csv中节点和告警信息的字典
def get_csv_warninginfo(csvfile):
    infos=fh.csv_remove_repeat(csvfile,['sysEname',"triggername"])
    warninglist=infos["triggername"].tolist()
    splitlist=[one.split(" ",1) for one in warninglist]
    result={one[0][2:]:one[1] for one in splitlist}
    return result

#获得对应csv中节点和告警信息的字典
def get_csv_nodesys(csvfile):
    infos=fh.csv_remove_repeat(csvfile,['sysEname',"triggername"])
    warninglist=infos["triggername"].tolist()
    nodelist=[one.split(" ",1)[0][2:] for one in warninglist]
    syslist=infos["sysEname"].tolist()
    result={nodelist[i]:syslist[i] for i in range(len(nodelist))}
    return result