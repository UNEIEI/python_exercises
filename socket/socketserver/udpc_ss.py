# coding=utf-8
import socket, sys

HOST = '127.0.0.1'
PORT = 3214

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = u'你好！'

s.sendto(data.encode('utf-8'),(HOST,PORT))
while data != 'bye':
    dat = b''
    while len(dat) == 0:
        dat,addr = s.recvfrom(1024)
    print u'收到数据：', dat.decode('utf-8')
    data = raw_input(u'输入要发送的信息：'.encode('gbk')).decode(sys.stdin.encoding)
    if data == '':
        data = 'bye'
    s.sendto(data.encode('utf-8'),(HOST,PORT))
s.close()