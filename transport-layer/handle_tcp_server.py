import socket


#创建连接
server = socket.socket(type=socket.SOCK_STREAM)
#绑定IP和端口号
address = "127.0.0.1"
port = 1234
server.bind((address,port))
print("TCP服务器已启动,地址为:%s,端口号为:%s"%(address,port))
#设置最大连接数
server.listen(128)
#接受客户端的连接,如果有新的客户端连接，则产生一个新的服务端连接
new_client,client_address = server.accept()
print("当前连接客户端地址为:%s,端口号为:%s"%(client_address[0],client_address[1]))
#accept已获取到客户端地址，此处使用recv而不用recvfrom
data = new_client.recv(1024)
print("服务器接收到的数据为:%s"%data.decode())
#发送数据给客户端
new_client.send("hahaha".encode())
#关闭连接
new_client.close()
server.close()
