#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/30 14:39
#@Author: hdq
#@File  : unittest.py

import unittest
import copy
import echartsTest as et

# 执行测试的类
class TestCase(unittest.TestCase):
    def setUp(self):
        self.tool = et
    def tearDown(self):
        self.tool = None
    #下面写测试函数 用assertEqual等进行断言
    def test_get_nodedata(self):
        t = self.tool.get_nodedata("../topology")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))

    def test_get_csv_nodedata(self):
        t = self.tool.get_csv_nodedata("../train/0.csv","node_60","../topology")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))

    def test_get_csv_nodeinfo_general(self):
        t = self.tool.get_csv_nodeinfo_general("../train/0.csv","node_60","../topology")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))


if __name__ == "__main__":
    unittest.main()