#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/30 14:26
#@Author: hdq
#@File  : clientunittest.py
import unittest
import client
import copy

# 执行测试的类
class TestCase(unittest.TestCase):
    def setUp(self):
        self.tool = client
    def tearDown(self):
        self.tool = None
    #下面写测试函数 用assertEqual等进行断言
    def test_cl_predict_csv(self):
        t=self.tool.cl_predict_csv("./train/1.csv",0)
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))

    def test_cl_get_nodedata(self):
        t = self.tool.cl_get_nodedata()
        for one in t:
            self.assertEqual(one , copy.deepcopy(one))

    def test_cl_get_csv_nodedata(self):
        t=self.tool.cl_get_csv_nodedata("./train/0.csv","node_60")
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))


    def test_cl_get_csv_nodesys(self):
        t=self.tool.cl_get_csv_nodesys("./train/0.csv","node_60")
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))

    def test_cl_predict_to_csv(self):
        t=self.tool.cl_predict_to_csv("./test/0.csv","./result/test.csv")
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))

    def test_cl_get_emin_csvinfo(self):
        t=self.tool.cl_get_emin_csvinfo("./test/0.csv")
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))


if __name__ == "__main__":
    unittest.main()