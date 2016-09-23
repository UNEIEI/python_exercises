# coding=utf-8
import socket, sys

HOST = '127.0.0.1'
PORT = 3214

s = socket.socket()

try: 
    s.connect((HOST,PORT))    
    data = u'你好！'
    while data:
        s.sendall(data.encode('utf-8'))
        data = s.recv(1024)
        print 'Receive from Server:\n', data.decode('utf-8')
        # 把输入的 string -> unicode
        data = raw_input('Please input an info:\n').decode(sys.stdin.encoding)
except socket.error as err:
    print err
finally:
    s.close()