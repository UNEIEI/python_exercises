# coding=utf-8
import SocketServer
import threading

# 定义关闭服务器方法，此方法只能在线程中调用
def sd():
    if serv: 
        serv.shutdown()
# 定义请求处理器类
class MyHdl(SocketServer.StreamRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024) # StreamRequestHandler类中request代表与客户端连接的socket对象
            print u'收到数据：', data.decode('utf-8')
            if data == b'bye':
                break
            self.request.sendall(data)
        print u'本次服务结束。'
        threading.Thread(target=sd).start()

'''
# 使用 rfile 和 wfile 来收发数据
class MyHdl(SocketServer.StreamRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline() #从客户端读取数据
            if not data:
                break
            print u'收到数据：', data.decode('utf-8').strip('\n')
            self.wfile.write(data)    #发送数据到客户端    
'''
if __name__ == '__main__':
    HOST = ''
    PORT = 3214
    serv = SocketServer.TCPServer((HOST,PORT),MyHdl)
    serv.serve_forever()
 