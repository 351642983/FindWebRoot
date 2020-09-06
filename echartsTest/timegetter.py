#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/9 19:45
# @Author: zhangtao
# @File  : timegetter.py
import time
import datetime


# 获得当前时间戳
def get_nowtimeticks():
    return time.time();


# 获得当前时间,未转化
def get_noformat_localtime():
    localtime = time.localtime(time.time())
    return localtime


# 获得当前的时间，标准化
def get_standard_localtime():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime


# 获得格式化的当前时间 格式化成2016-03-20 11:45:39形式 %Y-%m-%d %H:%M:%S
def get_format_localtime(format):
    return time.strftime(format, time.localtime())


# 将时间的格式由一种形式转化为另外一种形式
def change_time_format(timestr, oldformat, newformat):
    return datetime.datetime.strptime(timestr, oldformat).strftime(newformat)


# 获得时间戳
def get_timeticks(timestr, format):
    return time.mktime(time.strptime(timestr, format))


# 将时间戳转换为日期
def get_ticks_to_date(ticks, format):
    return time.strftime(format, time.localtime(ticks))


#获得日期字符串的week
def get_timestr_to_week(timestr,format="%Y-%m-%d"):
    return datetime.datetime.strptime(timestr,format).weekday()+1


#获得日期字符串的datetime
def get_timestr_to_timestamp(timestr,format="%Y-%m-%d"):
    return datetime.datetime.strptime(timestr,format)


#得到两个时间之差的天数
def datetime_minus_days(time1,time2,format="%Y-%m-%d %H:%M:%S"):
    return (string_to_datetime(time1,format)-string_to_datetime(time2,format)).days


#得到两个时间之差的秒数
def datetime_minus_seconds(time1,time2,format="%Y-%m-%d %H:%M:%S"):
    return (string_to_datetime(time1,format)-string_to_datetime(time2,format)).seconds


#得到两个时间之差的datime
def datetime_minus_datime(time1,time2,format="%Y-%m-%d %H:%M:%S"):
    return (string_to_datetime(time1,format)-string_to_datetime(time2,format))


#将字符串转化为datetime
def string_to_datetime(str,format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.strptime(str,format)




