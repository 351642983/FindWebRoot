#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/9 17:30
# @Author: hdq
# @File  : stringhandle.py
import re


# 获得字符串中所有符合正则表达式的字符串
def getstringexep(exep, str):
    return re.findall(exep, str)
# example
# str = "a123b244"
# print(getstringexep(r"(?<=a).*?(?=b)",str))


#判断字符串是否符合正则表达式
def judgesuitexep(exep,str):
    an = re.search("^"+exep+"$", str)
    if an:
        return True
    else:
        return False
# example
# str = "a123b244"
# print(judgesuitexep(r".*",str))

#
# from PIL import Image  # 导入画布
#
# #10进制转其他进制，从地位到高位输出结果
# def conversion(n, d):
#     result=[]
#     while(n//d >= 1):
#         result.append(n%d)
#         n = n//d
#     if(n%d !=0):
#         result.append(n%d)
#     return result
#
#
# def string_to_imagepixel(str,outpath,width=40,hnum=None):
#     strlen=len(str)         #获得字符长度
#     if(hnum==None):
#         height=strlen//width+1     #计算获得图片高度
#     else:
#         height=hnum
#     # strfill=(strlen%width)  #计算获得图片黑色区域填充大小
#     # if strfill!=0:
#     #     height+=1           #若有填充区域则高度加一
#     bgcolor = (255 ,255, 255)   #设置图片背景颜色为黑色
#     img = Image.new(mode='RGB', size=(width, height), color=bgcolor) #创建一个画板
#     # print(width," ",height)
#     for i in range(len(str)):
#         x=i%width
#         y=i//width
#         pointvalues=conversion(ord(str[i]),256)    #获得汉字的表示颜色
#         if(len(pointvalues)==2):
#             color1 = (pointvalues[0], pointvalues[1],0)
#         elif(len(pointvalues)==3):
#             color1 = (pointvalues[0], pointvalues[1], pointvalues[2])
#         elif (len(pointvalues) == 1):
#             color1 = (pointvalues[0], 255, 255)
#         else:
#             color1 = (255, 255, 255)
#         # print(x, " ", y)
#         img.putpixel((x,y),color1)  #设置画布对应点的颜色
#     img.save(outpath)  # 保存
#     return img
#
#
#
# #将list中label同名结果进行替换操作
# def replace_stringlist_to_tfable(strlist):
#     mininfos=set(strlist)
#     strhandle="\\".join(strlist)
#     num=len(mininfos)
#     for i in range(num):
#         strhandle=strhandle.replace(mininfos.pop(),chr(i+ord("A")))
#     return strhandle.split("\\")
#
# #将list中的数据套上一层壳
# def list_to_post(list):
#     return [[one] for one in list]
