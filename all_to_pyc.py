# -*- coding: utf-8 -*-
import sys
#python 27
#python之模块py_compile用法(将py文件转换为pyc文件)；二进制文件，是由py文件经过编译后，生成的文件.
 
#办法一：
import py_compile
#加r前缀进行转义
#py_compile.compile(r'D:\test.py')#py文件完整的路径.

import compileall


#sys.path[:] = ['s1', 's2']
#print('s1'+'s2')
#compileall.compile_dir(r'C:\Users\jufan\Documents\Workspace\pythons\logserver')
compileall.compile_dir(r'.')

'''
要过滤不必要的目录，可以使用rx参数提供一个正则表达式来排除不需要的目录。

import compileall
import re
 
compileall.compile_dir('examples', 
rx=re.compile(r'/\.svn'))
$ python compileall_exclude_dirs.py
Listing examples ...
Compiling examples/a.py ...
Listing examples/subdir ...
Compiling examples/subdir/b.py ...
————————————————
'''

#命令行形式.bat
#python -m py_compile xxx.py
# 注： 其中-m参数 就相当于py脚本中的import
# 这里的 -m py_compile 相当于上面的 import py_compile

input()