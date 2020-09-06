#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/10 20:09
#@Author: hdq
#@File  : echartsTest.py
#输出echarts对应的json信息(此部分代码弃用)

#输出地址
pointfile=r"./topology"

import filehandle as fh
import networkhandle as nh
import networkx as nx


def get_nodedata(pdir=pointfile):
    #获得对应json节点文件的echarts代码。
    seinfos=fh.json_get_infos(pdir+r"/sys_and_nodes.json","utf-8")
    sinfos=fh.json_get_infos(pdir+r"/topology_edges_sys.json","utf-8")
    einfos=fh.json_get_infos(pdir+r"/topology_edges_node.json","utf-8")
    count=[]
    nodedict={}
    strc=""
    strc+="{\"data\":[\n"
    i=0
    for one in seinfos:
        strc+="{\"name\":\""+str(one)+"\","
        strc+="\"category\":"+str(11)+","
        strc+="\"target\":["
        for two in range(len(seinfos[one])):
            strc+="{\"name\":\""+seinfos[one][two]+"\","
            if not (nodedict.get(seinfos[one][two])):
                nodedict[seinfos[one][two]]=one[4:]
            strc+="\"value\":\"系统连接节点\"}"
            strc+=","
        for three in range(len(sinfos[one])):
            strc += "{\"name\":\"" + str(sinfos[one][three]) + "\","
            strc += "\"value\":\"系统连接系统\"}"
            if (three != len(sinfos[one]) - 1):
                strc += ","
        strc+="]}"
        # if (i != len(seinfos) - 1):
        strc += ",\n"
        # for two in range(len(seinfos[one])):
        #     strc += "{name:\"" + seinfos[one][two] + "\","
        #     strc += "category:" + str(2) + ","
        #     strc += "target:["
        #     strc+="{name:\""+str(one)+"\","
        #     strc+="value:\"节点连接系统\"}"
        #     strc += "]}"
        #     # if (i != len(seinfos) - 1) or (two != len(seinfos[one]) - 1):
        #     strc += ",\n"
        i += 1
    i=0
    for one in einfos:
        count.append(one)
        strc+="{\"name\":\""+str(one)+"\","
        strc+="\"category\":"+str(nodedict[str(one)])+","
        strc+="\"target\":["
        for two in range(len(einfos[one])):
            strc+="{\"name\":\""+einfos[one][two]+"\","
            strc+="\"value\":\"边缘连接边缘\"}"
            if(two!=len(einfos[one])-1):
                strc+=","
        strc+="]}"
        if (i != len(einfos) - 1):
            strc+=",\n"
        i+=1
    strc+="]}\n"
    return strc
    # fh.outfile(outdir,strc)
    # json=eval(strc)
    # print(len(count))
    # print(len(set(count)))
    # print(json)
import datacenter as dc
def get_csv_nodedata(csvfile,pointnode,pdir=pointfile):
    allnodelist=nh.get_every_point(pdir)
    csvweb = nh.create_digraph_bydir(pdir)
    tempinfo = fh.csv_remove_repeat(csvfile, ['sysEname', "triggername"])
    tempinfo.sort_index()
    trechargerinfo = tempinfo.iloc[:, 1:4].values.T
    csvweb.remove_nodes_from(list(set(allnodelist) - set(trechargerinfo[0]) - set([one.split(" ", 1)[0][2:] for one in trechargerinfo[2]])))
    warningdict=dc.get_csv_warninginfo(csvfile)

    predecessors=list(csvweb.predecessors(pointnode))
    successors=list(csvweb.successors(pointnode))
    strc = ""
    strc += "{\"data\":[\n"
    for i in allnodelist:
        type=-1
        if i not in csvweb.nodes():
            type=3
        strc += "{\"name\":\"" + i + "\","
        typelist=['系统','告警涉及节点','根因节点','当前无关节点','根因相连前驱节点','根因相连后继节点']
        if(type!=3):
            if(i[:3]=="SYS"):
                type=0
            elif i in predecessors:
                type=4
            elif i in successors:
                type=5
            elif i!=pointnode:
                type=1
            else:
                type = 2
        strc += "\"category\":" + str(type) + ","
        if i in csvweb.nodes() and i[:3]!="SYS":
            strc += "\"value\":[\"" + typelist[type]+","+warningdict[i] + "\"],"
        else:
            strc += "\"value\":[\"" + typelist[type] + "\"],"
        strc += "\"target\":["
        if(type!=3):
            subnodelist=list(csvweb.successors(i))
        else:
            subnodelist = []
        for j in subnodelist:
            strc += "{\"name\":\"" + j + "\","
            strc += "\"value\":\""+typelist[type]+"\""
            strc+="}"
            if(j!=subnodelist[-1]):
                strc += ","
        strc += "]}"
        if(i!=allnodelist[-1]):
            strc+=","
    strc+="]}\n"
    return strc

#返回csv文件的前驱节点 对应前驱系统 后继节点 对应后驱系统号
def get_csv_nodeinfo_general(csvfile,pointnode,pdir=pointfile):
    allnodelist = nh.get_every_point(pdir)
    csvweb = nh.create_digraph_bydir(pdir)
    tempinfo = fh.csv_remove_repeat(csvfile, ['sysEname', "triggername"])
    tempinfo.sort_index()
    trechargerinfo = tempinfo.iloc[:, 1:4].values.T
    csvweb.remove_nodes_from(
        list(set(allnodelist) - set(trechargerinfo[0]) - set([one.split(" ", 1)[0][2:] for one in trechargerinfo[2]])))
    nodesys=dc.get_csv_nodesys(csvfile)
    predecessors = [one for one in list(csvweb.predecessors(pointnode)) if one[:3]!="SYS"]
    successors = [one for one in list(csvweb.successors(pointnode)) if one[:3]!="SYS"]
    presys=[nodesys[one] for one in predecessors]
    sucsys=[nodesys[one] for one in successors]
    return predecessors,presys,successors,sucsys
