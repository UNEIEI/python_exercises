# coding=utf-8
import SocketServer

# 定义请求处理器类
class MyHdl(SocketServer.DatagramRequestHandler):
    def handle(self):
            data,socket = self.request # DatagramRequestHandler类中request代表从客户端收到的数据与socket对象组成的元组
            print u'收到数据：', data.decode('utf-8')
            socket.sendto(data,self.client_address)            
        
if __name__ == '__main__':
    HOST = ''
    PORT = 3214
    s = SocketServer.UDPServer((HOST,PORT),MyHdl)
    s.serve_forever()