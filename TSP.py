# coding=utf-8

#TSP问题求解

import math, sys
import random

#成本构造函数
def distcal(path, dist):
    sum_dist=0
    for j in range(0,len(path)-1):
        di=dist[int(path[j])-1][int(path[j+1])-1]    #计算路径中相邻城市间的距离
        sum_dist = sum_dist + di                     #计算距离之和
    di=dist[int(path[len(path)-1])-1][path[0]-1]     #计算最后一个城市到始发城市的距离
    sum_dist=sum_dist+di                             #计算总距离
    return sum_dist
                                      
'''
#遍历算法
#构造路径函数
def perm(l):
    if (len(l))<=1:
        return [l]                  #递归基础：只有一个城市，选择这个城市
    r=[]
    for i in range(len(l)):         #对每个城市，构造不包含这个城市的所有可能序列
        s=l[:i] + l[i+1:]
        p=perm(s)
        for x in p:
            r.append(l[i:i+1]+x)    #将序列与该城市合并，得到完整数列
        return r
    
#主函数
if __name__ =="__main__":
    city=[1,2,3,4,5]
    dist=((0,1,3,4,5),
          (1,0,1,2,3),
          (3,1,0,1,2),
          (4,2,1,0,1),
          (5,3,2,1,0))
    for i in range(0,5):
        print dist[i][:]
    print '===='

    allpath=perm(city)             #调用路径构造函数，产生所有可能路径
    #print allpath
    #print len(allpath)

    optimal=1000000                #初始化最优路径的总成本和索引号
    index=-1
    for i in range(0,len(allpath)):
        pd=distcal(allpath[i],dist)
        if pd<optimal:            #比较是否总成本更低，如果是，替换最优解
            optimal=pd
            index=i
        #print pd

    print 'The length of the optimal path is: %d' % optimal
    print 'The optimal path is:'
    print allpath[index]

'''
#随机算法
#构造路径函数
def randompath(inc):
    allcity=inc[:]
    path=[]
    loop=True
    while loop:
        if 1==len(allcity):
            tmp=random.choice(allcity)
            path.append(tmp)
            loop=False
        else:
            tmp=random.choice(allcity)     #随机选择一个城市
            path.append(tmp)               #加入路径
            allcity.remove(tmp)            #从城市列表中移除
    print path
    return path
    

#主函数
if __name__=="__main__":
    city=[1,2,3,4,5]
    dist=((0,1,3,4,5),
          (1,0,1,2,3),
          (3,1,0,1,2),
          (4,2,1,0,1),
          (5,3,2,1,0))
    for i in range(0,5):
        print dist[i][:]
    print '===='

    num=10                                 #随机路径条数

    optimal=1000000
    for i in range(0,num):
        pd=distcal(randompath(city),dist)  #调用路径构造函数产生路径，并计算总成本
        if pd<optimal:                          
            optimal=pd                     #比较是否总成本更低，如果是，替换最优解
        print pd    
    print 'The length of the optimal path is %d' % optimal
