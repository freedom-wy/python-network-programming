import socket

client = socket.socket(type=socket.SOCK_DGRAM)
nickname = input("请输入你的网名:")
while True:
    send_msg  = input("请输入发送的消息:")
    if send_msg == 'quit':
        send_msg = "已下线"
        client.sendto((nickname+"#"+send_msg).encode(),address)
        break
    else:
        client.sendto((nickname+"#"+send_msg).encode(),('127.0.0.1',1234))
        re_data,address = client.recvfrom(1024)
        data = re_data.decode().split("#")
        print(data[0]+"说:"+data[1])
client.close()
