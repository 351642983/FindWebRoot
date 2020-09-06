#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/3 9:28
#@Author: hdq
#@File  : emailtool.py

# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '351642983@qq.com'
password = 'QQ 邮箱授权码'#这里请更换成你的qq邮箱和对应的授权码
# 发信服务器
smtp_server = 'smtp.qq.com'


def send_email(to_addr,info,title,receiver=None):
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(info, 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    if not receiver:
        msg['To'] = Header(title)
    else:
        msg['To'] = Header(receiver)

    msg['Subject'] = Header(title)

    # 开启发信服务，这里使用的是加密传输
    server=smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    try:
        server.sendmail(from_addr, to_addr, msg.as_string())
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
    # 关闭服务器
    server.quit()

# send_email("578095023@qq.com","内容Python测试","测试")