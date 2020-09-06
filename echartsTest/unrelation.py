#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/23 10:14
#@Author: hdq
#@File  : unrelation.py
#构建根因 非根因节点出现次数字典

import filehandle as fh
def create_keypointcsv(dir):

    nodetempsilit=[]
    systempsplit=[]
    tempsplit=[]
    labels=[]
    for i in fh.get_files_by_types(dir,".csv"):
        pdframe=fh.csv_remove_repeat(i,['sysEname',"triggername","is_root"])
        tempsplit+=[one.split(" ",1)[1] for one in pdframe.loc[:,"triggername"].values]
        systempsplit+=[one[4:] for one in pdframe.loc[:,"sysEname"].values]
        nodetempsilit+=[one.split(" ",1)[0][7:] for one in pdframe.loc[:,"triggername"].values]
        labels+=pdframe.loc[:,"is_root"].values.tolist()

#系统根因表
    sysalldict = {one: 0 for one in set(systempsplit)}
    sysunrootcounts = {one: 0 for one in set(systempsplit)}

    for i in range(len(systempsplit)):
        init=systempsplit[i]
        root=labels[i]
        sysalldict[init]=sysalldict[init]+1
        if root == 0 :
            sysunrootcounts[init]=sysunrootcounts[init]+1
    sysunrootlist = []
    sysrootlist = []
    sysunrelation = []

    for init in sysalldict:
        if sysalldict[init] == sysunrootcounts[init]:
            sysunrootlist.append(init + "|0|" + str(sysunrootcounts[init]))
        elif sysunrootcounts[init] == 0:
            sysrootlist.append(init + "|" + str(sysalldict[init]) + "|0")
        else:
            sysunrelation.append(init + "|" + str(sysalldict[init] - sysunrootcounts[init]) + "|" + str(sysunrootcounts[init]))

#主机根因表
    nodealldict = {one: 0 for one in set(nodetempsilit)}
    nodeunrootcounts = {one: 0 for one in set(nodetempsilit)}

    for i in range(len(nodetempsilit)):
        init=nodetempsilit[i]
        root=labels[i]
        nodealldict[init]=nodealldict[init]+1
        if root == 0 :
            nodeunrootcounts[init]=nodeunrootcounts[init]+1
    nodeunrootlist = []
    noderootlist = []
    nodeunrelation = []

    for init in nodealldict:
        if nodealldict[init] == nodeunrootcounts[init]:
            nodeunrootlist.append(init + "|0|" + str(nodeunrootcounts[init]))
        elif nodeunrootcounts[init] == 0:
            noderootlist.append(init + "|" + str(nodealldict[init]) + "|0")
        else:
            nodeunrelation.append(init + "|" + str(nodealldict[init] - nodeunrootcounts[init]) + "|" + str(nodeunrootcounts[init]))

#警告信息根因表
    alldict={one:0 for one in set(tempsplit)}
    unrootcounts={one:0 for one in set(tempsplit)}

    for i in range(len(tempsplit)):
        init=tempsplit[i]
        root=labels[i]
        alldict[init]=alldict[init]+1
        if root == 0 :
            unrootcounts[init]=unrootcounts[init]+1

    unrootlist=[]
    rootlist=[]
    unrelation=[]
    for init in alldict:
        if alldict[init]== unrootcounts[init]:
            unrootlist.append(init+"|0|"+str(unrootcounts[init]))
        elif unrootcounts[init]==0:
            rootlist.append(init+"|"+str(alldict[init])+"|0")
        else:
            unrelation.append(init+"|"+str(alldict[init]-unrootcounts[init])+"|"+str(unrootcounts[init]))
    return rootlist,unrootlist,unrelation,noderootlist,nodeunrootlist,nodeunrelation,sysrootlist,sysunrootlist,sysunrelation

def create_keypointcsv_onlywarning(dir):
    tempsplit = []
    labels = []
    for i in fh.get_files_by_types(dir, ".csv"):
        pdframe = fh.csv_remove_repeat(i, ['sysEname', "triggername", "is_root"])
        tempsplit += [one.split(" ", 1)[1] for one in pdframe.loc[:,"triggername"].values]
        labels += pdframe.loc[:,"is_root"].values.tolist()

    # 警告信息根因表
    alldict = {one: 0 for one in set(tempsplit)}
    unrootcounts = {one: 0 for one in set(tempsplit)}

    for i in range(len(tempsplit)):
        init = tempsplit[i]
        root = labels[i]
        alldict[init] = alldict[init] + 1
        if root == 0:
            unrootcounts[init] = unrootcounts[init] + 1

    unrootlist = []
    rootlist = []
    unrelation = []
    for init in alldict:
        if alldict[init] == unrootcounts[init]:
            unrootlist.append(init + "|0|" + str(unrootcounts[init]))
        elif unrootcounts[init] == 0:
            rootlist.append(init + "|" + str(alldict[init]) + "|0")
        else:
            unrelation.append(init + "|" + str(alldict[init] - unrootcounts[init]) + "|" + str(unrootcounts[init]))
    return rootlist, unrootlist, unrelation

# rootpath=r"C:\Users\Halo\Desktop\软件杯\data_release\root.txt"
# unrootpath=r"C:\Users\Halo\Desktop\软件杯\data_release\unroot.txt"
# unrealationpath=r"C:\Users\Halo\Desktop\软件杯\data_release\unrelation.txt"
# root,unroot,unrealation,a,b,c=create_keypointcsv(r"C:\Users\Halo\Desktop\软件杯\data_release\train")
# print(a,b,c)
#
# fh.remove_file(rootpath)
# fh.remove_file(unrootpath)
# fh.remove_file(unrealationpath)
# for i in root:
#     fh.appendfile(rootpath,i,"\n")
# for i in unroot:
#     fh.appendfile(unrootpath, i,"\n")
# for i in unrealation:
#     fh.appendfile(unrealationpath, i,"\n")
