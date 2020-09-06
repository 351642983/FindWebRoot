#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/30 14:39
#@Author: hdq
#@File  : unittest.py



import unittest
import rulegetter as rg
import copy

import os
os.chdir("../")

# 执行测试的类
class TestCase(unittest.TestCase):
    def setUp(self):
        self.tool = rg
    def tearDown(self):
        self.tool = None
    #下面写测试函数 用assertEqual等进行断言
    def test_load_rules_pointer(self):
        t = self.tool.load_rules_pointer()
        self.assertTrue(t)

    def test_get_warninginfo_node(self):
        t = self.tool.get_warninginfo_node("node_77 单元测试")
        self.assertTrue(t!=-1)

    def test_get_csv_baseinfo(self):
        t = self.tool.get_csv_baseinfo(["./train/1.csv","./train/2.csv"],False)
        self.assertTrue(t!=None)

    #将csv训练文件中的数据标准化为可处理化的数据（训练模型中的一部分)
    def test_handle_csvinfo_tostandard(self):
        csvinfos, labels, warningsnum = self.tool.get_traininfos("./train", spilttype=40)
        self.tool.load_rules_pointer()
        t = self.tool.handle_csvinfo_tostandard(csvinfos, warningsnum)
        self.assertTrue(t != None)

    # 测试训练模型是否正常
    def test_train_model(self):
        t=self.tool.train_models(0)
        self.assertTrue(t)


    #测试获取训练数据
    def test_get_traininfos(self):
        t = self.tool.get_traininfos("./train",40)
        self.assertTrue(t!=0)

    #b,c列表根据a列表序号排序
    def test_dlist_sort_byidlist(self):
        t=self.tool.dlist_sort_byidlist([2,1,0,3],[2,3,2,1],[4,2,3,2])
        self.assertEqual(t[0][0] , 2)
        self.assertEqual(t[0][1] , 3)
        self.assertEqual(t[1][0] , 3)
        self.assertEqual(t[1][1] , 2)
        self.assertEqual(t[2][0] , 2)
        self.assertEqual(t[2][1] , 4)
        self.assertEqual(t[3][0] , 1)
        self.assertEqual(t[3][1] , 2)


    def test_get_rule_descript(self):
        t=self.tool.get_rule_descript()
        print(t)
        self.assertTrue(t!=None)

    #修复一个bug，关于idlist在排序的时候错误的问题，单元测试
    def test_get_rule_total(self):
        #初始化数据
        self.tool.get_rule_descript()
        t=self.tool.get_rule_total()
        print(t)
        self.assertTrue(t!=None)

    def test_ishave_index(self):
        t=self.tool.ishave_index([1,2,3],1)
        self.assertEqual(t,0)

    #测试预测模型
    def test_predict_csv(self):
        # 初始化数据
        self.tool.load_rules_pointer()
        t=self.tool.predict_csv("./train/0.csv",0.5,0)
        print(t)
        self.assertEqual(t[0][1],60)

    def test_get_csv_root(self):
        t=self.tool.get_csv_root("./train/0.csv")
        self.assertEqual(t,60)

    def test_predict_to_csv(self):
        self.tool.load_rules_pointer()
        t=self.tool.predict_to_csv("./test/1.csv","./unittest",0.5,0)
        self.assertTrue(t)
    #按照先来先到读取警告出现次序信息
    def test_csv_waringinfos_fcfs(self):
        t=self.tool.csv_waringinfos_fcfs("./test/0.csv")
        #判断有信息
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))

    def test_get_enmin_csv_infos(self):
        t=self.tool.get_enmin_csv_infos("./test/0.csv")
        #判断有信息
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))







if __name__ == "__main__":
    unittest.main()