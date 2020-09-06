#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/30 14:39
#@Author: hdq
#@File  : unittest.py

import unittest
import datacenter as dc
import copy

# 执行测试的类
class TestCase(unittest.TestCase):
    def setUp(self):
        self.tool = dc
    def tearDown(self):
        self.tool = None
    #下面写测试函数 用assertEqual等进行断言
    def test_get_basedata(self):
        t = self.tool.get_basedata("../topology")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))

    def test_get_every_weekday_roots(self):
        t = self.tool.get_every_weekday_roots("../topology")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))

    def test_get_csv_warninginfo(self):
        t = self.tool.get_csv_warninginfo("../train/0.csv")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))

    def test_get_csv_nodesys(self):
        t = self.tool.get_csv_nodesys("../train/0.csv")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))


if __name__ == "__main__":
    unittest.main()