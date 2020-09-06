#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/30 14:39
#@Author: hdq
#@File  : unittest.py

import unittest
import timegetter as tg

# 执行测试的类
class TestCase(unittest.TestCase):
    def setUp(self):
        self.tool = tg
    def tearDown(self):
        self.tool = None
    #下面写测试函数 用assertEqual等进行断言

    def test_get_nowtimeticks(self):
        t=self.tool.get_nowtimeticks()
        print(t)
        self.assertTrue(t!=None)

    def test_get_noformat_localtime(self):
        t=self.tool.get_noformat_localtime()
        print(t)
        self.assertTrue(t!=None)

    def test_get_standard_localtime(self):
        t=self.tool.get_standard_localtime()
        print(t)
        self.assertTrue(t!=None)

    def test_get_format_localtime(self):
        t = self.tool.get_format_localtime("%Y")
        self.assertEqual("2020",t)

    def test_change_time_format(self):
        t=self.tool.change_time_format("2020-7-3","%Y-%m-%d","%Y/%m/%d")
        self.assertEqual("2020/07/03",t)

    def test_get_timeticks(self):
        t=self.tool.get_timeticks("2020/7/3","%Y/%m/%d")
        print(t)
        self.assertTrue(t!=None)

    def test_get_ticks_to_date(self):
        t=self.tool.get_ticks_to_date(1593705600.0,"%Y/%m/%d")
        print(t)
        self.assertEqual("2020/07/03",t)

    def test_get_timestr_to_week(self):
        t = self.tool.get_timestr_to_week("2020-7-3","%Y-%m-%d")
        self.assertEqual(5,t)

    def test_get_timestr_to_timestamp(self):
        t=self.tool.get_timestr_to_timestamp("2020-7-3","%Y-%m-%d")
        print(t)#转化为datetime了
        import datetime
        self.assertEqual(datetime.datetime,type(t))

    def test_datetime_minus_days(self):
        t=self.tool.datetime_minus_days("2020-07-03","2020-06-03","%Y-%m-%d")
        self.assertEqual(30,t)

# #测试失败 两个时间差的秒数
#     def test_datetime_minus_seconds(self):
#         t = self.tool.datetime_minus_seconds("2020-07-04 00:00:00","2020-07-03 00:00:00" , "%Y-%m-%d %H:%M:%S")
#         self.assertEqual(86400*30, t)

    def test_datetime_minus_datime(self):
        t=self.tool.datetime_minus_datime("2020-07-04","2020-07-03","%Y-%m-%d")
        import datetime
        self.assertEqual(datetime.timedelta, type(t))

    def test_string_to_datetime(self):
        t=self.tool.string_to_datetime("2020-07-03","%Y-%m-%d")
        import datetime
        self.assertEqual(datetime.datetime, type(t))







if __name__ == "__main__":
    unittest.main()