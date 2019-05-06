import socket

#创建Socket时， SOCK_DGRAM 指定了这个Socket的类型是UDP。
client = socket.socket(type=socket.SOCK_DGRAM)
send_data  = input("请输入发送的数据:")
client.sendto(send_data.encode(),('127.0.0.1',1234))
re_Data,address = client.recvfrom(1024)
print('服务器回复数据为:%s'%re_Data.decode('utf-8'))
client.close()
