from socket import *
import datetime  # 导入时间模块，以便获取系统时间
#获取计算机名称
hostname=gethostname()
#获取本机IP
ip=gethostbyname(hostname)

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)  # 服务器创建欢迎套接字
serverSocket.bind(('', serverPort))  # 将服务器的端口号与该套接字关联起来
serverSocket.listen(1)     # 该行让服务器聆听来自客户的 TCP 连接请求。其中参数定义了请求连接的最大数（至少为 1）。
print('The server is ready to connect.')
print("The server address: ('", str(ip), "', ", str(serverPort), ')')

connectionSocket, addr = serverSocket.accept()   # 创建连接套接字
print('Accepted a new connection.')
while True:
    sentence = connectionSocket.recv(1024).decode()
    print('Received a request: ', sentence, '.')
    if sentence == 'Time':
        now_time = datetime.datetime.now().strftime('%F %T')  # strftime是格式化成我们想要的格式，%F是年-月-日，%T是时:分:秒
        connectionSocket.send(now_time.encode())
        print('Send a response: ', now_time, '.')
    elif sentence == 'Exit':
        response = 'Bye'
        connectionSocket.send(response.encode())
        print('Send a response: ', response, '.')
        break
connectionSocket.close()  # 关闭连接套接字
