#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/9 16:03
# @Author: zhangtao
# @File  : filehandle.py
import os
import csv
import shutil

from PIL import Image
import pandas as pd


# 创建文件夹
def createDir(dirpath):
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
        return True
    return False


# 获得文件内容以行数呈递
def getfilelines(filepath, encoding="utf-8",replaceEnd=True):
    f = open(filepath, "r", encoding=encoding)
    str = f.readlines()
    f.close()
    if(replaceEnd):
        str=[one.replace("\n","") for one in str]
    return str


# 获得文件的所有内容，返回字符串
def getfileinfos(filepath, encoding="utf-8"):
    f = open(filepath, "r", encoding=encoding)
    str = f.read()
    f.close()
    return str

# 获得路径的文件名
def get_path_file_basename(path):
    return os.path.basename(path).replace(os.path.splitext(path)[1], "")


# 获得路径的后缀名
def get_path_file_append(path):
    return os.path.splitext(path)[1]

# 添加内容到文件里面
def appendfile(filepath, info, startchar="", encoding="utf-8"):
    i=0
    with open(filepath, 'a', encoding=encoding) as file_obj:
        file_obj.write(startchar)
        file_obj.write(info)
        return True



# 输出文件内容
def outfile(filepath, info, encoding="utf-8"):
    with open(filepath, 'w', encoding=encoding) as file_obj:
        file_obj.write(info)
        return True



# 获得文件夹所有文件包含子目录文件
def get_all_files(dir):
    files_ = []
    list = os.listdir(dir)
    for i in range(0, len(list)):
        path = os.path.join(dir, list[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            files_.append(path)
    return files_


def get_all_dirs(dir):
    dirs = []
    for dirpath, dirnames, filenames in os.walk(dir):
        dirs.append(dirpath)
    return dirs


# # 去除csv重复项
# def csv_remove_repeat_out(csvpath, subset, outpath, header=True, index=False, keep='last', encoding='utf-8',
#                       replace=False):
#     frame = pd.read_csv(csvpath, engine='python')
#     data = frame.drop_duplicates(subset=subset, keep=keep, inplace=replace, encoding=encoding)
#     data.to_csv(outpath, encoding=encoding, header=header, index=index)
# 去除csv重复项
def csv_remove_repeat(csvpath, subset, keep='first', encoding='utf-8',
                      replace=False,header=0):
    frame = pd.read_csv(csvpath,encoding=encoding,header=header)
    data = frame.drop_duplicates(subset=subset, keep=keep, inplace=replace)
    return data

# 读取csv文件
def csv_reader(csvpath, encoding='utf-8',header=0):
    frame = pd.read_csv(csvpath,encoding=encoding,header=header)
    return frame

#获得当前目录下的类型
def get_dir_infos(dir,type=2):
    result=[]
    for sub in os.walk(dir):
        for i in sub[type]:
            result.append(dir+"/"+i)
    return result

#删除文件夹以及下面所有文件
def remove_point_dirs(dir):
    try:
        shutil.rmtree(dir)
    except Exception:
        return False
    return True

#删除单个文件
def remove_file(path):
    if(os.path.exists(path)):
        os.remove(path)
        return True
    return False

#删除文件夹目录文件
def remove_in_dirs(dir):
    try:
        filelists=get_dir_infos(dir)
        dirslist = get_dir_infos(dir,1)
        print(dirslist)
        for one in dirslist:
            remove_point_dirs(one)
        for one in filelists:
            remove_file(one)
    except Exception:
        return False
    return True

# 获得以endtype结尾的全部文件
def get_files_by_types(dir, endtype,type=0):
    if(type==1):
        return [one for one in get_all_files(dir) if one.endswith(endtype)]
    else:
        return [one for one in get_dir_infos(dir) if one.endswith(endtype)]


#
# def csv_out_onerow(csvpath, rowinfolist, encoding='utf-8'):
#     with open(csvpath, 'w', encoding=encoding, newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(rowinfolist)
#
#
# # for row in rows:
# #     print(','.join(row))
#
#
#
# #删除文件列表
# def remove_files(lists):
#     for one in lists:
#         remove_files(one)
#

#
#
#
#
# # 准备数据到当前文件夹
# def prepare_files_toproject(file_list, subdir='./temp/'):
#     file_map = []
#     if os.path.exists(subdir):
#         shutil.rmtree(subdir)
#     os.mkdir(subdir)
#     for i in range(len(file_list)):
#         one = file_list[i]
#         shutil.copyfile(one, subdir + "%d" % i)  # 复制文件/文件夹，复制 old 为 new（new是文件，若不存在，即新建），复制 old 为至 new 文件夹（文件夹已存在）
#         file_map.append(subdir + "%d" % i)
#     return file_map, dict(zip(file_map, file_list))
#
#
# # list,map=fh.prepare_files_toproject(fh.get_files_by_types(r'C:/Users/Halo/Desktop/1.6项目开发过程', '.jpg'))
# # print(list)
# # print(map)
# # finalname=[map[sh.getstringexep(r"b'(.*?):0",ones)[0]] for ones in filenamebatch_result]
#
# # 完成准备的当前文件夹类型
# def finish_files_toproject(subdir='./temp/'):
#     if os.path.exists(subdir):
#         shutil.rmtree(subdir)
#
#
# # 获得文件的字节
# def get_file_size(path):
#     return os.path.getsize(path)
#
#
# # 将图片转化为别的格式
# def image_change_to(imgpath, outfile, Width=None, Height=None):
#     try:
#         img = Image.open(imgpath)
#         if (Width):
#             g_width = Width
#         else:
#             g_width = img.width
#         if (Height):
#             g_height = Height
#         else:
#             g_height = img.height
#         img.resize((g_width, g_height), Image.ANTIALIAS).save(outfile)
#
#     except IOError:
#         print('can not convert ', imgpath)
#
#
# # 将文件夹中的图片转化到另外一个文件夹中
# def image_dirchange_to(imgpath, expr, outdir, outtype, Width=None, Height=None):
#     file_list = get_files_by_types(imgpath, expr)
#     if (os.path.exists(outdir)) is False:
#         os.makedirs(outdir)
#     for one in file_list:
#         image_change_to(one, outdir + "/" + get_path_file_basename(one) + outtype, Width, Height)
#
#
# # 载入必要的模块
# import pygame
#
#
# def text_to_image(txt, filepath, color=(65, 83, 130), width=None, height=None):
#     # pygame初始化
#     pygame.init()
#     # 待转换文字
#     text = txt
#     # 设置字体和字号
#     font = pygame.font.SysFont('simsunnsimsun', 64)
#     # 渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
#     ftext = font.render(text, True, color, (255, 255, 255))
#     # 保存图片
#     pygame.image.save(ftext, filepath)  # 图片保存地址
#     image_change_to(filepath, filepath, width, height)
#
#
# 获得路径完整文件名
def get_path_file_completebasename(path):
    return os.path.split(path)[1]


# 获得文件名中的路径
def get_path_file_subpath(path):
    return os.path.split(path)[0]
#
#
#
#
# from pydub import AudioSegment
# import wave
# import io
# import numpy as np
# import matplotlib.pyplot as plt  # 专业绘图库
# from scipy.io import wavfile
#
# AudioSegment.converter = r"F:\ffmpeg-4.2.2-win64-static\bin\ffmpeg.exe"
# AudioSegment.ffmpeg = r"F:\ffmpeg-4.2.2-win64-static\bin\ffmpeg.exe"
# AudioSegment.ffprobe = r"F:\ffmpeg-4.2.2-win64-static\bin\ffprobe.exe"
#
#
# def sound_change_to(path, out):
#     # 先从本地获取 mp3 的 bytestring 作为数据样本
#     filename = path
#     fp = open(filename, 'rb')
#     data = fp.read()
#     fp.close()
#     # 读取
#     aud = io.BytesIO(data)
#     sound = AudioSegment.from_file(aud, format=get_path_file_append(path)[1:])
#     raw_data = sound._data
#     # 写入到文件
#     l = len(raw_data)
#     f = wave.open(out, 'wb')
#     f.setnchannels(1)
#     f.setsampwidth(2)
#     f.setframerate(16000)
#     f.setnframes(l)
#     f.writeframes(raw_data)
#     f.close()
#
#
# def sound_to_image(filename, out):
#     # 读取生成波形图
#     samplerate, data = wavfile.read(filename)
#     times = np.arange(len(data)) / float(samplerate)
#     # print(len(data), samplerate, times)
#     # 可以以寸为单位自定义宽高  frameon=False 为关闭边框
#     fig = plt.figure(figsize=(20, 5), facecolor="White")
#     # plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
#     ax = fig.add_axes([0, 0, 1, 1])
#     ax.axis('off')
#     plt.fill_between(times, data, linewidth='1', color='green')
#     plt.xticks([])
#     plt.yticks([])
#     plt.savefig(out, dpi=100, transparent=False, bbox_inches='tight', edgecolor='w')
#     plt.close(fig)
#     # plt.show()
#
#
# # image_dirchange_to(r'C:\Users\Halo\Desktop\1.6项目开发过程','.jpg',r'C:\Users\Halo\Desktop\1.6项目开发过程\test','.bmp',20,20)
#
# def sound_dirchange_to_image(wavpath, expr, outdir, outtype, Width=None, Height=None):
#     file_list = get_files_by_types(wavpath, expr)
#     if (os.path.exists(outdir)) is False:
#         os.makedirs(outdir)
#     for one in file_list:
#         sound_to_image(one, outdir + "/" + get_path_file_basename(one) + "_" + outtype)
#         image_change_to(outdir + "/" + get_path_file_basename(one) + "_" + outtype,
#                         outdir + "/" + get_path_file_basename(one) + outtype, Width, Height)
#         if (os.path.exists(outdir + "/" + get_path_file_basename(one) + "_" + outtype)):
#             os.remove(outdir + "/" + get_path_file_basename(one) + "_" + outtype)
#
#获得文件列表的前一个目录名
def get_files_pre_dir(filelist):
    preinfo = []
    for name in filelist:
        preinfo.append(get_file_pre_dir(name))
    return preinfo

#获得文件的前一个目录名
def get_file_pre_dir(filename):
    return os.path.basename(get_path_file_subpath(filename))

#获得文件列表的文件名
def get_paths_file_basename(filelist):
    basenames=[]
    for name in filelist:
        basenames.append(get_path_file_basename(name))
    return basenames
#
# #将对应tfpointlabel文件间的翻译链接上
# def get_labels_tfpointlabel_to(labelfile1,labelfile2):
#     dic1=eval(getfileinfos(labelfile1))
#     dic2 = eval(getfileinfos(labelfile2))
#     resultdic={}
#     for key,value in dic1.items():
#         for key1, value1 in dic2.items():
#             if(value==value1):
#                 resultdic[key]=key1
#                 break
#     return resultdic
#
#
# # import stringhandle as sh
# # print(sh.replace_stringlist_to_tfable(get_files_pre_dir(get_files_by_types(r"I:\查阅\python\文本分类\训练集\1\data",".txt"))))
#
# from io import BytesIO
# import matplotlib
# matplotlib.use('TkAgg')
# import cv2
#
# def aHash(img):
#     # 均值哈希算法
#     # 缩放为8*8
#     img = cv2.resize(img, (8, 8))
#     # 转换为灰度图
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # s为像素和初值为0，hash_str为hash值初值为''
#     s = 0
#     hash_str = ''
#     # 遍历累加求像素和
#     for i in range(8):
#         for j in range(8):
#             s = s + gray[i, j]
#     # 求平均灰度
#     avg = s / 64
#     # 灰度大于平均值为1相反为0生成图片的hash值
#     for i in range(8):
#         for j in range(8):
#             if gray[i, j] > avg:
#                 hash_str = hash_str + '1'
#             else:
#                 hash_str = hash_str + '0'
#     return hash_str
#
#
# def dHash(img):
#     # 差值哈希算法
#     # 缩放8*8
#     img = cv2.resize(img, (9, 8))
#     # 转换灰度图
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     hash_str = ''
#     # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
#     for i in range(8):
#         for j in range(8):
#             if gray[i, j] > gray[i, j + 1]:
#                 hash_str = hash_str + '1'
#             else:
#                 hash_str = hash_str + '0'
#     return hash_str
#
#
# def pHash(img):
#     # 感知哈希算法
#     # 缩放32*32
#     img = cv2.resize(img, (32, 32))  # , interpolation=cv2.INTER_CUBIC
#
#     # 转换为灰度图
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # 将灰度图转为浮点型，再进行dct变换
#     dct = cv2.dct(np.float32(gray))
#     # opencv实现的掩码操作
#     dct_roi = dct[0:8, 0:8]
#
#     hash = []
#     avreage = np.mean(dct_roi)
#     for i in range(dct_roi.shape[0]):
#         for j in range(dct_roi.shape[1]):
#             if dct_roi[i, j] > avreage:
#                 hash.append(1)
#             else:
#                 hash.append(0)
#     return hash
#
#
# def calculate(image1, image2):
#     # 灰度直方图算法
#     # 计算单通道的直方图的相似值
#     hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
#     hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
#     # 计算直方图的重合度
#     degree = 0
#     for i in range(len(hist1)):
#         if hist1[i] != hist2[i]:
#             degree = degree + \
#                      (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
#         else:
#             degree = degree + 1
#     degree = degree / len(hist1)
#     return degree
#
#
# def classify_hist_with_split(image1, image2, size=(256, 256)):
#     # RGB每个通道的直方图相似度
#     # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
#     image1 = cv2.resize(image1, size)
#     image2 = cv2.resize(image2, size)
#     sub_image1 = cv2.split(image1)
#     sub_image2 = cv2.split(image2)
#     sub_data = 0
#     for im1, im2 in zip(sub_image1, sub_image2):
#         sub_data += calculate(im1, im2)
#     sub_data = sub_data / 3
#     return sub_data
#
#
# def cmpHash(hash1, hash2):
#     # Hash值对比
#     # 算法中1和0顺序组合起来的即是图片的指纹hash。顺序不固定，但是比较的时候必须是相同的顺序。
#     # 对比两幅图的指纹，计算汉明距离，即两个64位的hash值有多少是不一样的，不同的位数越小，图片越相似
#     # 汉明距离：一组二进制数据变成另一组数据所需要的步骤，可以衡量两图的差异，汉明距离越小，则相似度越高。汉明距离为0，即两张图片完全一样
#     n = 0
#     # hash长度不同则返回-1代表传参出错
#     if len(hash1) != len(hash2):
#         return -1
#     # 遍历判断
#     for i in range(len(hash1)):
#         # 不相等则n计数+1，n最终为相似度
#         if hash1[i] != hash2[i]:
#             n = n + 1
#     return n
#
#
#
# def PILImageToCV():
#     # PIL Image转换成OpenCV格式
#     path = "/Users/waldenz/Documents/Work/doc/TestImages/t3.png"
#     img = Image.open(path)
#     plt.subplot(121)
#     plt.imshow(img)
#     print(isinstance(img, np.ndarray))
#     img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
#     print(isinstance(img, np.ndarray))
#     plt.subplot(122)
#     plt.imshow(img)
#     plt.show()
#
#
# def CVImageToPIL():
#     # OpenCV图片转换为PIL image
#     path = "/Users/waldenz/Documents/Work/doc/TestImages/t3.png"
#     img = cv2.imread(path)
#     # cv2.imshow("OpenCV",img)
#     plt.subplot(121)
#     plt.imshow(img)
#
#     img2 = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     plt.subplot(122)
#     plt.imshow(img2)
#     plt.show()
#
#
# def bytes_to_cvimage(filebytes):
#     # 图片字节流转换为cv image
#     image = Image.open(filebytes)
#     img = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
#     return img
#
# #获得图片的cv2 img值
# def get_cv2_img(imgpath):
#     # 通过imread方法直接读取物理路径
#     img1 = cv2.imread(imgpath)
#     return img1
#
# #获得网络图片的img值(webimgpath)
# def get_webcv2_img(webimg):
#     img1 = cv2.cvtColor(np.asarray(webimg), cv2.COLOR_RGB2BGR)
#     return img1
#
# #计算图片相似度 均值哈希
# def img_similar_ahash(imgpath1,imgpath2):
#     hash1 = aHash(get_cv2_img(imgpath1))
#     hash2 = aHash(get_cv2_img(imgpath2))
#     n1 = cmpHash(hash1, hash2)
#     return (1-float(n1/64))
#
# #计算图片相似度 差值哈希
# def img_similar_dhash(imgpath1,imgpath2):
#     hash1 = dHash(get_cv2_img(imgpath1))
#     hash2 = dHash(get_cv2_img(imgpath2))
#     n1 = cmpHash(hash1, hash2)
#     return (1-float(n1/64))
#
# #计算图片相似度 感知哈希
# def img_similar_phash(imgpath1,imgpath2):
#     hash1 = pHash(get_cv2_img(imgpath1))
#     hash2 = pHash(get_cv2_img(imgpath2))
#     n1 = cmpHash(hash1, hash2)
#     return (1-float(n1/64))
#
# #计算图片相似度 三直方图
# def img_similar_hist(imgpath1,imgpath2):
#     return classify_hist_with_split(get_cv2_img(imgpath1), get_cv2_img(imgpath2))[0]
#
# #计算图片相似度 单通道直方图
# def img_similar_single(imgpath1,imgpath2):
#     return calculate(get_cv2_img(imgpath1), get_cv2_img(imgpath2))[0]
#
import json
#获得json文件的字符串
def json_get_infos(path,encoding='utf-8'):
    return json.loads(getfileinfos(path,encoding=encoding))

#
# from PIL import Image
#
# #裁剪图片
# def image_spilt_to(path,out,fromx,tox,fromy,toy):
#     img = Image.open(path)
#     print(img.size)
#     cropped = img.crop((fromx, fromy, tox, toy))  # (left, upper, right, lower)
#     cropped.save(out)
#
# #根据whlist裁剪图片
# def image_from_labelme_spilt_to(piclist,whlist,namelist,todir):
#     for c in range(len(piclist)):
#         one=piclist[c]
#         sf=[get_path_file_basename(t) for t in namelist]
#         i=sf.index(get_path_file_basename(one))
#         image_spilt_to(one,todir+"/"+get_path_file_basename(one)+".png",whlist[i][0],whlist[i][2],whlist[i][1],whlist[i][3])
# # _,whlist,namelist,_=th.read_labelmelist(labelmejson)
# # fh.image_from_labelme_spilt_to(fh.get_files_by_types(tobooleandir,".JPG"),whlist,namelist,outputdir)
#
#
# #将图片转化为灰度图
# def image_to_gray(path,out):
#     img = Image.open(path)
#     # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
#     Img = img.convert('L')
#     Img.save(out)
#
# #将图片转化为二值化图 读取图片处理方式一,二值化转换
# def image_to_booleanvalue(path,out,threshold=200,fakethresold=0,mfilter=(10,10)):
#     # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
#     img = Image.open(path)
#     Img = img.convert('L')
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#     # 图片二值化
#     photo = Img.point(table, '1')
#     if (os.path.exists(out)):
#         os.remove(out)
#     photo.save(out)
#
#
#
# #将图片列表执行对应操作
# def image_list_handle(piclist,out,handle=image_to_booleanvalue,value=75,value2=70,mfilter=(10,10)):
#     for one in piclist:
#         handle(one,out+"/"+get_path_file_basename(one)+".png",value,value2,mfilter)
#
#
#
#
# #将图片转化为数组
# def image_to_array(picpath,cnntype=False,nptype=np.uint8,cvt=None):
#     image = Image.open(picpath) # 用PIL中的Image.open打开图像
#     if(cvt):
#         image.convert(cvt)
#     print(picpath,image)
#     image_arr = np.array(image,nptype) # 转化成numpy数组--------------------nptype
#     if(cnntype):
#         image_arr=add_booleanimage_post(image_arr)
#     return image_arr
#
# #读取图片数组
# def imagedir_to_arrays(dirpath,type,nptype=np.uint8,booleanimage=True):
#     result=[]
#     files=get_files_by_types(dirpath,type)
#     for one in files:
#         result.append(image_to_array(one,booleanimage,nptype))
#     return files,result
#
# #生成对应二值化图片并且获得对应数组值
# def imagedir_change_booleanvalues(picdir,outdir,Width,Height,inputtype=".jpg",outputtype=".png",nptype=np.uint8,booleanimage=True,value=75,value2=70,handle=image_to_booleanvalue,mfilter=(10,10)):
#     files=get_files_by_types(picdir,inputtype)
#     image_list_handle(files,outdir,handle=handle,value=value,value2=value2,mfilter=mfilter)
#     image_dirchange_to(outdir,outputtype,outdir,outputtype,Width,Height)
#     tfiles,images=imagedir_to_arrays(outdir,outputtype,nptype=nptype,booleanimage=booleanimage)
#     return tfiles,images
#
# #二值化转换
# def booleanvalues_change(booleanvalues):
#     return 1-np.array(booleanvalues)/255
#
#
# #将数组转化为图片
# def array_to_image(array,out,nptype=np.uint8,picmode="L"):
#     arrayt = np.asarray(array, dtype=nptype)
#     image = Image.fromarray(arrayt,picmode)
#     if(os.path.exists(out)):
#         os.remove(out)
#     image.save(out)
#
# #将图片数据转化为tfable
# def imagedir_to_arrays_tfable(dirpath,type,booleanimage=True,Width=None,Height=None,gaussianblur=False,mfilter=(5,5),mvalue=0.0,tonparray=True):
#     result=[]
#     dirtemp=dirpath+"/"+get_file_pre_dir(get_path_file_subpath(dirpath))+"temp"
#     if not (os.path.exists(dirtemp)):
#         createDir(dirtemp)
#     image_dirchange_to(dirpath,type,dirtemp,".png",Width=Width,Height=Height)
#     files=get_files_by_types(dirtemp,".png")
#     for one in files:
#         nowimg=image_to_array(one,booleanimage)
#         if(gaussianblur):
#             nowimg=img_array_gs(nowimg,mfilter,mvalue)
#             nowimg=add_booleanimage_post(nowimg)
#         result.append(nowimg)
#     if(tonparray):
#         return files,np.array(result,np.uint8)
#     else:
#         return files,result
#
#
# #将读取的cnnable数据转化为tfable
# def change_cnndata_to_tfable(infolist):
#     result=[]
#     for one in infolist:
#         subtemp=[]
#         for two in one:
#             for three in two:
#                 for four in three:
#                     subtemp.append(four)
#         result.append(subtemp)
#     return result
#
#
# #将cnn里面最里层的数据抽出来
# def out_cnn_pre(lists):
#     result=[]
#     for one in lists:
#         temp1=[]
#         for two in one:
#             temp2=[]
#             for three in two:
#                 temp2.append(*three)
#             temp1.append(temp2)
#         result.append(temp1)
#     return result
#
# #将cnn里面最里层的数据增加一层
# def add_cnn_post(lists):
#     result=[]
#     for one in lists:
#         temp1=[]
#         for two in one:
#             temp2=[]
#             for three in two:
#                 temp2.append([three])
#             temp1.append(temp2)
#         result.append(temp1)
#     return result
#
# #将图片里面最里层的数据增加一层
# def add_booleanimage_post(lists):
#     result=[]
#     for one in lists:
#         temp1=[]
#         for two in one:
#             temp1.append([two])
#         result.append(temp1)
#     return result
#
# #将图片里面最里层的数据增加一层
# def out_booleanimage_pre(lists):
#     result=[]
#     for one in lists:
#         temp1=[]
#         for two in one:
#             temp1.append(*two)
#         result.append(temp1)
#     return result
#
# import pyautogui
# import cv2
#
# #得到屏幕截图
# def get_screen(x1,y1,x2,y2):
#     img = pyautogui.screenshot(region=[x1,y1,x2,y2])
#     return img
#
# #得到屏幕截图并转化为数组
# def get_screen_toarray(x1,y1,x2,y2):
#     return np.asarray(get_screen(x1,y1,x2,y2))
#
# #将图片数组进行高斯模糊
# def img_array_gs(imgarray,mfilter=(5,5),value=0.0,tonparray=True):
#     if(tonparray):
#         return cv2.GaussianBlur(np.array(imgarray),mfilter,value)
#     else:
#         return cv2.GaussianBlur(imgarray, mfilter, value)
#
# #将图片数组集合进行高斯模糊
# def img_arrays_gs(imgarrays,mfilter=(5,5),value=0.0):
#     return [cv2.GaussianBlur(np.array(one),mfilter,value).tolist() for one in imgarrays]
#
# #将图片进行高斯模糊并输出
# def img_to_gs(path,output,mfilter=(5,5),value=0.0,cnnable=False,nptype=np.int8):
#     array_to_image(img_array_gs(image_to_array(path, cnnable,nptype),mfilter,value),
#                    output)
#
# #将图片数组进行转化为另外的格式
# def img_array_to_anthor_type(imgarray,changetype=cv2.COLOR_RGB2GRAY):
#     return cv2.cvtColor(imgarray,changetype)
#
#
# #边缘检测
# def img_array_canny(imgarray,start,end,mfilter=(5,5),mvalue=0.0):
#     img = img_array_gs(imgarray,mfilter,mvalue)
#     canny = cv2.Canny(img, start, end)
#     return canny
#
# # 形态学：边缘检测
# def img_array_canny_shape(imgarray, start=50, end=70, mfilter=(5, 5),gray=True,enlarge=True):
#     _,Thr_img = cv2.threshold(imgarray,start, end,cv2.THRESH_BINARY)#设定红色通道阈值210（阈值影响梯度运算效果）
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT,mfilter)         #定义矩形结构元素
#     gradient = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel) #梯度
#     if(gray):
#         gradient=img_array_to_anthor_type(gradient)
#     if(enlarge):
#         gradient=enlarge_gray(gradient)
#     return gradient
#
# #使灰度值扩大至二级分化
# def enlarge_gray(imgarray):
#     listpoint=imgarray.tolist()
#     for i in range(len(listpoint)):
#         for j in range(len(listpoint[i])):
#             if(listpoint[i][j]>0):
#                 listpoint[i][j]=0
#             else:
#                 listpoint[i][j]=1
#     return np.array(listpoint)
#
#
# #读取图片处理方式二,二值化转换
# def image_handle_boolean2(filepath,outputfile,value,endvalue=0,mfilter=(10,10)):
#     img=image_to_array(filepath)
#     array_to_image(1-img_array_canny_shape(img, value, endvalue,mfilter=mfilter,enlarge=False)/255,outputfile,nptype=np.uint8,picmode="L")
#
#
# #在数组中仅取指定范围
# def img_array_mask(imgarray,fromx,formy,tox,toy):
#     mask = np.zeros([len(imgarray), len(imgarray[0])], dtype=np.uint8)
#     mask[formy:toy, fromx:tox] = 255
#     image = cv2.add(imgarray, np.zeros(np.shape(imgarray), dtype=np.uint8), mask=mask)
#     return image
#
# #指定图片添加遮罩层
# def img_to_mask(imgpath,outpath,fromx,formy,tox,toy,picmode="RGB"):
#     array_to_image(
#     img_array_mask(image_to_array(imgpath), fromx,formy,tox,toy),
#     outpath,
#     picmode=picmode)
#
# #指定图片文件夹添加遮罩层
# def imgdir_to_mask(imgdir,outdir,whlist,type=".png",outtype=".png",picmode="RGB"):
#     fileslist=get_files_by_types(imgdir,type)
#     for one in range(len(fileslist)):
#         xyinfo=whlist[one]
#         img_to_mask(fileslist[one],outdir+"/"+get_path_file_basename(fileslist[one])+outtype,xyinfo[0],xyinfo[1],xyinfo[2],xyinfo[3],picmode=picmode)
#
# #根据遮罩层图片对图片进行遮罩
# def img_from_mask_to_binary(imgpath, maskimgpath, outputpath,readpicmode="RGB"):
#     # Add binary masks to images
#     img_path = imgpath
#     img = image_to_array(img_path)
#     mask_path = maskimgpath  # mask是.png格式的，image是.jpg格式
#     mask = image_to_array(mask_path,cvt="L")  # 将彩色mask以二值图像形式读取
#     # mask = img_array_to_anthor_type(Mask)
#     # masked = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)  #将image的相素值和mask像素值相加得到结果
#     ROI=cv2.bitwise_and(img,img,mask=mask)
#     array_to_image(ROI,outputpath,picmode=readpicmode)
#
#
# #根据遮罩图片列表对图片进行遮罩
# def imglist_form_mask_to_binary(imglist,maskpiclistdir,outdir,outtype=".png",readpicmode="RGB"):
#     for one in imglist:
#         basename=get_path_file_basename(one)
#         img_from_mask_to_binary(one,maskpiclistdir+"/"+basename+"_json/label.png",outdir+"/"+basename+outtype,readpicmode)
#
#
# #根据遮罩图片列表对图片进行遮罩
# def imgdir_form_mask_to_binary(imgdir,maskpiclistdir,outdir,inputtype=".png",outtype=".png",readpicmode="RGB"):
#     imglist = get_files_by_types(imgdir,inputtype)
#     for one in imglist:
#         basename=get_path_file_basename(one)
#         img_from_mask_to_binary(one,maskpiclistdir+"/"+basename+"_json/label.png",outdir+"/"+basename+outtype,readpicmode)
# from imblearn.under_sampling import ClusterCentroids
# from imblearn.over_sampling import RandomOverSampler
# from imblearn.under_sampling import RandomUnderSampler
# from imblearn.over_sampling import ADASYN
#
# #数据平衡操作
# def data_balance(imagelists,labelists,over_sampling=True):
#     if not over_sampling:
#         return ADASYN().fit_sample(imagelists,labelists)
#     else:
#         cc = ClusterCentroids(random_state=0)
#         return cc.fit_sample(imagelists, labelists)
# #数据朴素平衡
# def data_balance_ps(imagelists,labelists,over_sampling=True):
#     if(over_sampling):
#         ros = RandomOverSampler(random_state=0)
#         return ros.fit_sample(imagelists,labelists)
#     else:
#         ros=RandomUnderSampler(random_state=0)
#         return ros.fit_sample(imagelists,labelists)
#
#
#
