#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/27 10:30
#@Author: hdq
#@File  : networkhandle.py
#有向图处理文件

import networkx as nx
import filehandle as fh

#创建有向图
def create_digraph():
    return nx.DiGraph()

#根据有向图对象，导入json文件
def add_json(dgraph,jsonpath):
    pinfos = fh.json_get_infos(jsonpath, "utf-8")
    for one in pinfos:
        for two in pinfos[one]:
            dgraph.add_edge(one,two)
    return dgraph

#根据文件夹创建一个有向图网络
def create_digraph_bydir(dir,append=".json"):
    flist=fh.get_files_by_types(dir,append)
    web = None
    for i in range(len(flist)):
        nowfile=flist[i]
        if(i==0):
            web=add_json(create_digraph(),nowfile)
        else:
            web = add_json(web, nowfile)
    return web

#获得dir对应json中所有的节点
def get_every_point(dir, append=".json"):
    flist = fh.get_files_by_types(dir, append)
    result=[]
    for jsonpath in flist:
        pinfos = fh.json_get_infos(jsonpath, "utf-8")
        for one in pinfos:
            result.append(one)
            for two in pinfos[one]:
                result.append(two)
    return list(set(result))

# print(get_every_point(r"C:\Users\Halo\Desktop\软件杯\topology"))

# web=create_digraph_bydir(r"C:\Users\Halo\Desktop\软件杯\topology")
# print(web.out_degree("SYS_8"))
# web.remove_node("node_88")
# print(web.out_degree("SYS_8"))
