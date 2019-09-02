#!/usr/bin/python
#coding=utf8
"""
# File Name: replaceContent.py
# Description:
1.允许用户按以下爱方式执行时，即可以对指定文件内容进行全局替换
python3 yourScripts.py old.str new.str filename
2.替换完毕后打印替换了多少行内容
"""


import sys 
import os

# 添加统计功能
count = 0

oldStr = sys.argv[1]  # 老字符串
newStr = sys.argv[2]  # 新字符串

filename = sys.argv[3]  # 文件名
newFileName = '%s.new'%filename  # 新文件名，用来覆盖用

f = open(filename,mode = 'r+',encoding='utf-8')  # 以读写模式打开文件
f_new = open(newFileName,mode = 'w+',encoding='utf-8')  #读模式打开新文件，注意：w和w+会把以前的内容清空掉

data = f.readlines()  # 逐行读取文件  
for line in data:
    if oldStr in line:  # 如果oldStr存在在本行中
        count += 1
        new_line = line.replace(oldStr,newStr)  # 替换
    else:
        new_line = line
    f_new.write(new_line)

f.close()
f_new.close()

os.rename(newFileName,filename)  # 文件覆盖操作
print("一共替换了%d处"%count)
