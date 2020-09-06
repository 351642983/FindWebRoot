#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/5/3 18:44
#@Author: hdq
#@File  : server.py
#将接口以服务器的方式暴露以提供给Java调用缩短调用时间

import rulegetter
import socket
import echartsTest as et

import config_group



#对绑定qq群发出告警信息
def cl_send_warning_to_group(file,node,warning,time):
    if(config_group.call_type==2):
        import coolq_pyapi as cp
        bindgroup= config_group.bind_group
        cp.send_longmsg(bindgroup,"网络拓扑根因告警提醒：\n   文件:"+file+"\n   节点"+str(node)+"疑似为根因告警\n"+"   告警原因:"+warning+"\n   发现时间:"+time,cp.send_group_msg)
    elif(config_group.call_type==1):
        import emailtool
        bindemails=config_group.bind_email
        emailtool.send_email(bindemails,
                             "经过检测系统分析后，服务器上的告警信息上有疑似告警根因。具体信息如下。\n   文件:"+file+"\n   节点"+str(node)+"疑似为根因告警\n"+"   告警原因:"+warning+"\n   发现时间:"+time,
                             "网络拓扑根因故障告警提醒",
                             "根因告警绑定邮箱")
    return 'True'

#发送自定义信息
def cl_send_group_info(info):
    import coolq_pyapi as cp
    bindgroup = config_group.bind_group
    cp.send_longmsg(bindgroup,info,cp.send_group_msg)
    return 'True'


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while 1:
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    if not data: break
    method=str(data)[2]
    subdata=str(data.decode('gbk'))[1:]
    if(method=="1"):
        params = subdata.split("|")
        conn.sendall((str(list(rulegetter.predict_csv(params[0],0.5,int(params[1]))))[1:-1]).encode())
    elif(method=="2"):
        conn.sendall((str(et.get_nodedata())).encode())
    elif (method == "3"):
        params=subdata.split("|")
        conn.sendall((str(et.get_csv_nodedata(params[0],params[1]))).encode())
    elif (method == "4"):
        params=subdata.split("|")
        conn.sendall((str(et.get_csv_nodeinfo_general(params[0],params[1]))).encode())
    elif (method == "5"):
        params=subdata.split("|")
        if(rulegetter.predict_to_csv(params[0],params[1],0.5,int(params[2]))):
            conn.sendall(str("True").encode())
        else:
            conn.sendall(str("False").encode())
    elif (method == "6"):
        conn.sendall((str(list(rulegetter.get_enmin_csv_infos(subdata)))[1:-1]).encode())
    elif (method == "7"):
        rulegetter.init_load(True)
    elif (method == "8"):
        params=subdata.split("|")
        conn.sendall((str(cl_send_group_info(params[0]))).encode())
    elif (method == "9"):
        params=subdata.split("|")
        conn.sendall((str(cl_send_warning_to_group(params[0],params[1],params[2],params[3]))).encode())
    # update plot
    conn.close()
