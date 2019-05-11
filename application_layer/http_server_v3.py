import socket
import multiprocessing


HTML_DIR = "./html"

class HttpServer(object):
    def __init__(self):
        self.server = socket.socket(type=socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.server.bind(("", 8080))

    def handle_client(self,client):
        # 接收客户端的数据
        client_request_data = client.recv(1024)
        print("客户端的请求数据为:%s" % client_request_data)

        # 向客户端响应数据,一定要按照http协议规范,带上\r\n,并且一定要注意斜杠的方向
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server:My server\r\n"
        request_data = client_request_data.decode().split(" ")
        if request_data[1] == "/":
            # 斜杠一定要加上
            filename = "/index.html"
        else:
            filename = request_data[1]
        try:
            # rb是因为可能为图片视频等数据,并且需要判断文件是否存在
            with open(HTML_DIR + filename, 'rb') as f:
                response_body = f.read()
        except:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_body = "File Not Found".encode("utf-8")
        # response_body注意要decode
        response = response_start_line + response_headers + "\r\n" + response_body.decode()
        print("响应数据为:%s" % response)

        # 向客户端响应数据
        client.send(response.encode("utf-8"))
        # 关闭客户端连接
        client.close()

    #创建一个启动服务器方法
    def start(self):
        print('服务器启动,等待客户端连接...')
        self.server.listen(128)
        while True:
            # 接收客户端请求
            client, address = self.server.accept()
            print("%s,%s连接上了" % (address[0], address[1]))
            # 处理客户端请求,引入多进程
            client_process = multiprocessing.Process(target=self.handle_client, args=(client,))
            client_process.start()
            client.close()

def main():
    server = HttpServer()
    server.start()

if __name__ == '__main__':
    main()
