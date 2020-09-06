#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/30 14:39
#@Author: hdq
#@File  : unittest.py

import unittest
import splitwordtype as swt


# 执行测试的类
class TestCase(unittest.TestCase):
    def setUp(self):
        self.tool = swt
    def tearDown(self):
        self.tool = None
    #下面写测试函数 用assertEqual等进行断言

    def test_kmeans_spiltouttxtfile(self):
        t=self.tool.kmeans_spiltouttxtfile("../tempspilt.txt",2,"../stop_words_ch.txt")
        self.assertTrue(t!=None)

    def test_kmeans_spiltoutbystr(self):
        t=self.tool.kmeans_spiltoutbystr(["数字1","数字2","字母a","字母b"],2,"../stop_words_ch.txt")
        self.assertTrue(t != None)

if __name__ == "__main__":
    unittest.main()