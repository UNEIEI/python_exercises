# coding=utf-8
import random

x1=random.random()      #随机0和1之间的浮点数
print 'x1=',x1

x2=random.uniform(1,10)     #随机1和10之间的浮点数
print 'x2=',x2

x3=random.randint(10,100)       #随机10和100之间的整数
print 'x3=',x3

x4=random.randrange(0,101,2)        #随机0和101之间的偶数
print 'x4=',x4

x5=random.choice('abcdefg%#&^*f')       #随机选取字符
print 'x5=',x5

x6=random.choice(['apple','pear','peach','orange','lemon']) #随机选取字符串
print 'x6=',x6

p=['Python','is','powerful','simple','and so on...']        
random.shuffle(p)       #随机打乱列表中的元素
print p
