#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/19 10:35
#@Author: hdq
#@File  : coolq_pyapi.py
import _thread
import sys

import requests
import time

server_url="175.24.20.175:5700"




#发送私人消息
def send_private_msg(qqid,info):
    data = {
        'user_id':qqid,
        'message':info,
        'auto_escape':False
    }

    api_url = 'http://'+server_url+'/send_private_msg'
    #酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url,data=data)
    return eval(r.text)


#发送群消息
def send_group_msg(groupid,info):
    data = {
        'group_id':groupid,
        'message':info,
        'auto_escape':False
    }
    api_url = 'http://'+server_url+'/send_group_msg'
    #酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url,data=data)
    return eval(r.text)


#分批发送消息,字符串超出长度时
def send_longmsg(id,info,function=send_private_msg,perlen=400,sleep=0.1):
    # num=int(sys.getsizeof(info)/perlen)+1
    sznum=len(info)/sys.getsizeof(info)
    sum=0
    szpian=0
    i=0
    rlist=[]
    while(sum<len(info)-1):
        if(i==0):
            sinfo=info[int(i * perlen * sznum):int((i + 1) * perlen * sznum)].split("\n")
        else:
            sinfo = info[int(i * perlen * sznum)-szpian:int((i + 1) * perlen * sznum)-szpian].split("\n")
        if (len(sinfo) > 1):
            rinfo = "\n".join(sinfo[:-1])
        else:
            rinfo = "\n".join(sinfo)
        sum +=len(rinfo)+1
        szpian+=len(sinfo[-1])
        rlist.append(function(id,rinfo))
        i+=1
        # print(sum,len(info),"\n"+rinfo)
        time.sleep(sleep)
    return rlist
def set_group_add_request(flag,type,reason=None,approve=True):
    data = {
        'flag': flag,
        'type': type,
        'approve': approve,
        'reason': reason
    }
    api_url = 'http://' + server_url + '/set_group_add_request'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    requests.post(api_url, data=data)