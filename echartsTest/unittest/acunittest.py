#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/30 10:12
#@Author: hdq
#@File  : acunittest.py
import arraychanger as testunit
import pandas as pd
import copy
import unittest

# 执行测试的类
class TestCase(unittest.TestCase):
    def setUp(self):
        self.tool = testunit
    def tearDown(self):
        self.tool = None

    #pd转化list
    def test_list_from_pdframe(self):
        t=self.tool.list_from_pdframe(pd.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]}))
        for one in t:
            self.assertSequenceEqual(one.tolist(),copy.deepcopy(one).tolist())

    #list转化为np
    def test_list_add_list(self):
        t = self.tool.list_add_list([[1,2,3],[4,5,6]])
        self.assertTrue((t==[[1,2,3],[4,5,6]]).all)

    #解开内序列
    def test_out_init_list(self):
        t=self.tool.out_init_list([[[1,2]]])
        self.assertTrue(t==[[1,2]])

    #获得标签
    def test_list_csv_reader_label(self):
        t=self.tool.list_csv_reader_label("../train/0.csv", "is_root")
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))

    # 获得标签,加括号
    def test_list_csv_reader_label_post(self):
        t = self.tool.list_csv_reader_label_post("../train/0.csv", "is_root")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))

    #读取csv
    def test_pdframe_readcsv(self):
        t=self.tool.pdframe_readcsv("../train/0.csv",0)
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))




if __name__ == "__main__":
    unittest.main()