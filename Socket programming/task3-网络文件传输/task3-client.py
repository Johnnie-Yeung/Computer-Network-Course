from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
print('-----------------------------------')
print('Client is running.')
clientSocket.connect((serverName,serverPort))
print('Connected to ', serverName, ':', serverPort, '.')
filename = input('Please input a filename to request: ')
# 向服务器发送文件名filename
clientSocket.send(filename.encode())
print("Send the filename '", filename, "' to the server.")
print('-----------------------------------')

# 判断服务器能否找到所请求的文件
file_confirm = clientSocket.recv(1024)
if file_confirm.decode() == 'Cannot find the file':
    print('Server cannot find the file.')
    clientSocket.close()
else:
    # 先接收文件大小
    server_response = clientSocket.recv(1024)
    file_size = int(server_response.decode())
    # 接收文件内容
    new_filename = 'received_by_client.txt'
    file = open(new_filename, 'wb')
    # 初始化已接收到的数据大小
    received_size = 0
    while received_size < file_size:
        if (file_size-received_size) > 64:  # 多次接收
            size = 64
        else:
            size = file_size-received_size
        data = clientSocket.recv(size)
        # 更新已接收到的数据大小
        received_size += len(data)
        print('Received a chunk of '+ str(size) +' bytes.')
        # 把接收到的数据写入文件
        file.write(data)
    file.close()
    print('-----------------------------------')
    print("A file named '" + new_filename + "' of " + str(received_size) + ' bytes is saved.')
    print('Done!')
    print('-----------------------------------')
    clientSocket.close()
