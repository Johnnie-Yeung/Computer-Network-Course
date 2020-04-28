from socket import *
import os  # 用于检测文件是否存在及获取文件大小
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)  # 服务器创建欢迎套接字
serverSocket.bind(('', serverPort))  # 将服务器的端口号与该套接字关联起来
serverSocket.listen(1)  # 该行让服务器聆听来自客户的 TCP 连接请求。其中参数定义了请求连接的最大数（至少为 1）。
print('-----------------------------------')
print('The server is ready to connect.')

# 创建连接套接字
connectionSocket, addr = serverSocket.accept()
print('Accepted a new connection.')
# 接收文件名
filename = connectionSocket.recv(1024).decode()
print("Received a filename '" + filename + "'.")
# 检测文件是否存在
if os.path.isfile(filename):
    # 确认找到文件
    connectionSocket.send('Found'.encode())
    # 先发送文件大小
    file_size = os.path.getsize(filename)
    connectionSocket.send(str(file_size).encode())
    # 发送文件内容
    f = open(filename,'rb')
    send_size = 0
    while send_size < file_size:
        if (file_size - send_size) > 64:  #多次接收
            size = 64
        else:
            size = file_size - send_size
        data = f.read(size)
        connectionSocket.send(data)
        # 更新已发送的数据大小
        send_size += len(data)
        print('Send a chunk of ' + str(size) + ' bytes.')
    print('Send a file of ' + str(file_size) + ' bytes.')
    f.close()
else:
    connectionSocket.send('Cannot find the file'.encode())
    print('Cannot find the file.')
connectionSocket.close()
