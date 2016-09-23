# coding=utf-8
import socket

HOST = '127.0.0.1'
PORT = 3214

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST,PORT))

data = True

while data:
    data, addr = s.recvfrom(1024)
    if data == b'bye':
        break
    print 'Receive Srting:', data.decode('utf-8')
    s.sendto(data, addr)
    
s.close()
