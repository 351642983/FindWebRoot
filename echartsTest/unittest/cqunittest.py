#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/30 14:39
#@Author: hdq
#@File  : unittest.py

import unittest
import coolq_pyapi as cq

# 执行测试的类
class TestCase(unittest.TestCase):
    def setUp(self):
        self.tool = cq
    def tearDown(self):
        self.tool = None
    #下面写测试函数 用assertEqual等进行断言
    def test_send_private_msg(self):
        t=self.tool.send_private_msg(351642983,"test")
        self.assertTrue(t['status']=='ok')
    def test_send_group_msg(self):
        t = self.tool.send_group_msg(1060145246, "单元测试")
        self.assertTrue(t['status'] == 'ok')

    def test_send_longmsg(self):
        t = self.tool.send_longmsg(351642983, "test" * 100)

if __name__ == "__main__":
    unittest.main()