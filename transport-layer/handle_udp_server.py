import socket

server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(('127.0.0.1',1234))
print('这里是UDP服务器,端口号为1234,可以连接')
data,address = server.recvfrom(1024)
print("客户端的地址信息为:%s,客户端端口号为%s,"%(address[0],address[1]),'客户端发送过来的信息为:%s'%data.decode())
server.sendto('好好学习,天天向上'.encode(),address)
server.close()
