#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/30 14:39
#@Author: hdq
#@File  : unittest.py

import unittest
import stringhandle as sh

# 执行测试的类
class TestCase(unittest.TestCase):
    def setUp(self):
        self.tool = sh
    def tearDown(self):
        self.tool = None
    #下面写测试函数 用assertEqual等进行断言
    def test_getstringexep(self):
        t=self.tool.getstringexep(r"\d+","这是数字1235234，这也是是数字4664747")
        print(t)
        self.assertEqual(t[0],"1235234")
        self.assertEqual(t[1], "4664747")

    def test_judgesuitexep(self):
        t=self.tool.judgesuitexep("[0-9]{5,6}","12345")
        self.assertTrue(t)
        t1=self.tool.judgesuitexep("[a-z]+","1adfc")
        self.assertFalse(t1)

if __name__ == "__main__":
    unittest.main()