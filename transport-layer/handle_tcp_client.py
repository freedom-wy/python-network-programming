import socket

#创建客户端socket
client = socket.socket(type=socket.SOCK_STREAM)
client.connect(("127.0.0.1",1234))
client.send("你好".encode())
recv_data = client.recv(1024)
print("服务端发送过来的消息为:%s"%recv_data.decode())
client.close()