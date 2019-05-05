import socket

server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(('127.0.0.1',1234))
nickname = input("请输入你的网名:")
print("%s已上线,请等待好友上线"%nickname)
while True:
    re_data,address = server.recvfrom(1024)
    data = re_data.decode().split("#")
    print(data[0]+"说:"+data[1])
    send_msg = input("请输入要发送的信息:")
    if send_msg == 'quit':
        send_msg = "已下线"
        server.sendto((nickname+"#"+send_msg).encode(),address)
        break
    else:
        server.sendto((nickname+"#"+send_msg).encode(),address)
server.close()
