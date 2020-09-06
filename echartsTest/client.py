#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/5/3 18:47
#@Author: hdq
#@File  : client.py
#调用服务端接口客户端，以缩短调用时间

import socket

HOST = '127.0.0.1'  # The remote host
PORT = 50007  # The same port as used by the server

#调用服务端接口 0表示使用决策树算法预测 1表示使用BRNN算法预测 2表示使用卷积神经网络预测
def cl_predict_csv(filename,type=0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall((str(1)+filename+"|"+str(type)).encode())

    data = []
    while True:
        subdata = s.recv(20480)
        if not subdata: break
        data.append(str(subdata, encoding='utf-8'))
    data = ''.join(data)

    s.close()
    return data

#调用服务端接口
def cl_get_nodedata():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall((str(2)).encode())
    data = []
    while True:
        subdata = s.recv(20480)
        if not subdata: break
        data.append(str(subdata, encoding='utf-8'))
    data= ''.join(data)

    s.close()
    return data

#调用服务端接口
def cl_get_csv_nodedata(csvfile,pointnode):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall((str(3)+csvfile+"|"+pointnode).encode())
    data = []
    while True:
        subdata = s.recv(20480)
        if not subdata: break
        data.append(str(subdata, encoding='utf-8'))
    data= ''.join(data)

    s.close()
    return data

#调用服务端接口 获取前驱后继
def cl_get_csv_nodesys(csvfile,pointnode):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall((str(4)+csvfile+"|"+pointnode).encode())
    data = []
    while True:
        subdata = s.recv(20480)
        if not subdata: break
        data.append(str(subdata, encoding='utf-8'))
    data= ''.join(data)

    s.close()
    return data

#预测并输出一个csv文件，注意：不能预测训练文件，仅能预测测试文件
def cl_predict_to_csv(filename,outfilename,type=0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall((str(5)+filename+"|"+outfilename+"|"+str(type)).encode())

    data = []
    while True:
        subdata = s.recv(20480)
        if not subdata: break
        data.append(str(subdata, encoding='utf-8'))
    data = ''.join(data)

    s.close()
    return data

#获得去重后的csv信息包括告警信息出现次序
def cl_get_emin_csvinfo(filename):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall((str(6)+filename).encode())

    data = []
    while True:
        subdata = s.recv(20480)
        if not subdata: break
        data.append(str(subdata, encoding='utf-8'))
    data = ''.join(data)

    s.close()
    return data


#预测测试数据,可以在Server的控制台中看到对应信息
def cl_predict_test():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall((str(7)+"predict_test").encode())
#展示文件的预测速度
    s.close()

def test_speed():
    import time
    import filehandle as fh
    for one in fh.get_files_by_types("./test",".csv"):
        oldtime=time.time()
        print("文件:",one,"\t预测结果:",cl_predict_csv(one).split("]")[0][1:],"\t|\t预测时间:",time.time()-oldtime,"秒")


# #开启Server.py后，取消下面注释可以查看预测速度
# test_speed()





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


# cl_send_warning_to_group("1.csv","node_60","告警提醒","2020/8/3")

# cl_send_group_info("停运了- -")
#预测训练文件
# #将训练文件的预测结果以csv文件的形式存放到result中
# import filehandle as fh
# fh.remove_in_dirs("./result")
# flist=fh.get_files_by_types("./test",".csv")
# for i in flist:
#     print(i)
#     print(cl_predict_to_csv(i,"./result"))


