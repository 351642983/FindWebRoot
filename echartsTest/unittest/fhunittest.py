#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/30 14:39
#@Author: hdq
#@File  : unittest.py

import unittest
import filehandle as fh
import copy

# 执行测试的类
class TestCase(unittest.TestCase):
    def setUp(self):
        self.tool = fh
    def tearDown(self):
        self.tool = None
    #下面写测试函数 用assertEqual等进行断言

    def test_createDir(self):
        t=self.tool.createDir('./testdir')
        self.assertTrue(t)

    def test_getfilelines(self):
        t = self.tool.getfilelines("../train/0.csv")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))

    def test_getfileinfos(self):
        t=self.tool.getfileinfos("../train/0.csv")
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))
    #获得文件名
    def test_get_path_file_basename(self):
        t = self.tool.get_path_file_basename("../train/0.csv")
        self.assertEqual(t,'0')

    def test_get_path_file_append(self):
        t = self.tool.get_path_file_append("../train/0.csv")
        self.assertEqual(t,'.csv')
    #添加内容到文件里面
    def test_appendfile(self):
        t = self.tool.appendfile("./appendtest.txt","test")
        self.assertTrue(t)
    #输出内容
    def test_outfile(self):
        t = self.tool.outfile("./outtest.txt","test")
        self.assertTrue(t)

    def test_get_all_files(self):
        t = self.tool.get_all_files("../train")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))

    def test_get_all_dirs(self):
        t = self.tool.get_all_dirs("../")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))

    def test_csv_remove_repeat(self):
        t = self.tool.csv_remove_repeat('../train/0.csv',['sysEname',"triggername"])
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))
    #测试文件读取中的csv读取功能
    def test_csv_reader(self):
        t=self.tool.csv_reader("../train/0.csv")
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))
    #测试获取文件夹信息功能
    def test_get_dir_infos(self):
        t=self.tool.get_dir_infos("../train")
        for one in t:
            self.assertEqual(one, copy.deepcopy(one))

    #测试删除文件夹及其以下的说是有文件
    def test_remove_point_dirs(self):
        t=self.tool.remove_point_dirs("./testdir")
        self.assertTrue(t)

    #测试文件处理中的删除文件的函数
    def test_remove_file(self):
        t=self.tool.remove_file("./outtest.txt")
        self.assertTrue(t)
        t1 = self.tool.remove_file("./appendtest.txt")
        self.assertTrue(t1)

    #测试删除文件夹里面的文件的操作
    def test_remove_in_dirs(self):
        t=self.tool.remove_in_dirs("./testdirs")
        self.assertTrue(t)

    #测试能否获取文件夹中全部后缀名的文件列表
    def test_get_files_by_types(self):
        t=self.tool.get_files_by_types("../",".py")
        for one in t:
            self.assertEqual(one,copy.deepcopy(one))


    def test_get_path_file_completebasename(self):
        t=self.tool.get_path_file_completebasename("./test/0.csv")
        self.assertEqual(t,"0.csv")


    def test_get_path_file_subpath(self):
        t=self.tool.get_path_file_subpath("./test/0.csv")
        print(t)
        self.assertEqual(t, "./test")






if __name__ == "__main__":
    unittest.main()