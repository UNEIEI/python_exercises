# coding=utf-8

u = u'中文'
s = '哈哈'
print type(s) # str
print type(u) # unicode
# print s ,输出为乱码
print s.decode('utf-8') #把str解码为unicode, 输出正常
print unicode(s,'utf-8') #同decode方法
print u

#如果变量是raw_input进来的，则该变量是一个str类型的对象
s2 = raw_input('Input:')
print type(s2) #str
print s2, len(s2) #len(s2='测试')为4

import sys

u2 = raw_input(u'输入:'.encode('gbk')).decode(sys.stdin.encoding) # 或者 unicode(变量,sys.stdin.encoding)
print type(u2) #unicode
print u2, len(u2) #len(u2='测试')为2

'''使用字符串(如 s,s2)作为函数调用的参数时，需要先转换为unicode对象
例如 ..\socket\tcpc.py'''

'''文件处理。文件str_unicode.txt 内容为 'abc中文'
print open('test_unicode.txt').read() ，中文输出为乱码'''
print open('test_unicode.txt').read().decode('utf-8') 



