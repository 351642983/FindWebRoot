#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/19 12:06
#@Author: hdq
#@File  : receiver.py

from flask import Flask,request
from json import loads

import coolq_pyapi as cp

bot_server = Flask(__name__)
import config_group

bind_group= config_group.bind_group
check_dir= config_group.check_dir
watchlog= config_group.wathclog

import filehandle as fh
import rulegetter as rg
import os
global type
type=0
lists=['告警简略信息','监控日志操作信息','检测文件']

@bot_server.route('/api/message',methods=['POST'])
#路径是你在酷Q配置文件里自定义的
def server():
    data = request.get_data().decode('utf-8')
    data = loads(data)
    print(data)
    global type
    #以下写执行函数
    try:
        if(int(data["group_id"])==bind_group or bind_group==0):
            msg=data["message"]

            # cp.send_group_msg(bind_group,data["message"])
            if(msg in ['指令','帮助','菜单','功能','列表']):
                cp.send_group_msg(int(data['group_id']), "[CQ:at,qq="+str(data['user_id'])+"] \n网络拓扑根因寻找帮助菜单\n"+"\n".join(["#"+str(i+1)+"."+lists[i] for i in range(len(lists))]))
                type=0
            if(type==0):
                if(msg in ["#"+str(i+1) for i in range(len(lists))]):
                    type=int(msg[1:])
                    print(type)
                    if(type==1):
                        rootlogs=[ one.split("|")[0]+"\t"+one.split("|")[2]+"\t"+one.split("|")[3] for one in fh.getfilelines(check_dir+"/rootlog.txt")[::-1]]
                        result="[CQ:at,qq="+str(data['user_id'])+"] \n当前告警信息(位置,节点号,告警原因)：\n"+"\n".join(rootlogs).replace('\'','').replace("\\","/")
                        print(result)
                        cp.send_longmsg(int(data['group_id']),result,cp.send_group_msg)
                        # cp.send_longmsg(int(data['group_id']), "[CQ:at,qq=351642983]", cp.send_group_msg)
                    elif(type==2):
                        watchlogs = fh.getfilelines(watchlog)[::-1]
                        result = "[CQ:at,qq="+str(data['user_id'])+"] \n最新的监控操作：\n" + "\n".join([one[30:] for one in watchlogs]).replace('\'','')
                        print(result)
                        cp.send_longmsg(int(data['group_id']), result,cp.send_group_msg)

                    elif(type==3):
                        cp.send_group_msg(int(data['group_id']), "[CQ:at,qq="+str(data['user_id'])+"] \n请输入服务器上要检测的文件路径。")
                        type=4
                    if(type!=4):
                        type=0
                elif msg[:1]=="#":
                    cp.send_group_msg(int(data['group_id']), "[CQ:at,qq="+str(data['user_id'])+"] \n输入指令错误请重新输入,当前指令有:"+",".join(["#"+str(i+1) for i in range(len(lists))]))
            elif (type == 4):
                if (os.path.exists(msg)):
                    try:
                        preresult=rg.predict_csv(msg)
                        if(len(preresult)>0):
                            result = list(map(str,preresult[0]))
                            cp.send_group_msg(int(data['group_id']), "[CQ:at,qq="+str(data['user_id'])+"] \n文件:"+msg+"\n所属系统:"+result[0]+"\n节点:"+result[1]+"\n告警信息:"+result[2]+"\n告警时间:"+result[3]+"\n置信度:"+result[4])
                        else:
                            cp.send_group_msg(int(data['group_id']), "[CQ:at,qq="+str(data['user_id'])+"] \n文件"+msg+"没有发现根因节点告警")
                    except Exception:
                        cp.send_group_msg(int(data['group_id']), "[CQ:at,qq="+str(data['user_id'])+"] \n文件扫描出错，请检查对应文件是否为测试文件")
                else:
                    cp.send_group_msg(int(data['group_id']), "[CQ:at,qq="+str(data['user_id'])+"] \n服务器中查无此文件，请检查文件存在再进行预测")
                type = 0


    except Exception:
        try:
            if (data['post_type'] == "request"):
                if (data['request_type'] == "group"):
                    cp.set_group_add_request(int(data['flag']), data['sub_type'])
        finally:
            pass
        pass
    return ''


if __name__ == '__main__':
    bot_server.run(port=5701,host="192.168.123.144")
    #端口也是你在酷Q配置文件里自定义的