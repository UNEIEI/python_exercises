# coding=utf-8
import socket, sys

HOST = '127.0.0.1'
PORT = 3214

s = socket.socket()
s.connect((HOST,PORT))
data = u'你好！'
while data:
    s.sendall(data.encode('utf-8'))
    if data == 'bye':
        break
    data = s.recv(1024)
    print u'收到数据：', data.decode('utf-8')
    data = raw_input(u'输入要发送的信息：'.encode('gbk')).decode(sys.stdin.encoding)
'''
# 使用 rfile
while data:
    data += '\n'
    s.sendall(data.encode('utf-8'))
    if data == 'bye':
        break
    data = s.recv(1024)
    print u'收到数据：', data.decode('utf-8').strip('\n')
    data = raw_input(u'输入要发送的信息：'.encode('gbk')).decode(sys.stdin.encoding)
'''
s.close()