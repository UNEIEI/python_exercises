# coding=utf-8
import random
import math

def main():
    print 'Please input the number of iterations:'
    n=int(raw_input())    #get the number of iterations
    total=0
    for i in xrange(n):
        x,y=random.random(),random.random()
        if math.sqrt(x**2+y**2)<1.0:
            total +=1

    mypi=4.0*total/n
    print 'Estimating pi with ', n, 'iterations:', mypi
    print 'Value of math.pi is ', math.pi
    print 'Error is ', abs(math.pi-mypi)/math.pi

main()
