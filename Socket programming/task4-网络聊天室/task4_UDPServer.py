from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)  # IPv4, UDP
serverSocket.bind(('', serverPort))
print('The server is ready to receive.')
# 创建字典存放{clientAddress:username}, clientAddress为元组类型
users_list = {}
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    # 判断是否是新用户
    if clientAddress in users_list.keys():
        if message.decode() == '<quit>':
            print(users_list[clientAddress] + ' has quited the chat.')
            send_message = users_list[clientAddress] + " has left the chat!"
            for send_address in users_list.keys():
                serverSocket.sendto(send_message.encode(), send_address)
                # 此处同样给将要离开的client发送消息，意在指示其关闭接受线程。
                print('Send to ' + str(send_address[0]) + ':' + str(send_address[1]) + "--->'" + send_message + "'")
            del users_list[clientAddress]
        else:
            print('Receive from ' + str(clientAddress[0]) + ':' + str(clientAddress[1]) + '--->' + message.decode())
            send_message = "[" + users_list[clientAddress] + "] : " + message.decode()
            for send_address in users_list.keys():
                serverSocket.sendto(send_message.encode(), send_address)
                print('Send to ' + str(send_address[0]) + ':' + str(send_address[1]) + "--->'" + send_message + "'")
    else:
        username = message.decode()
        # 添加用户至用户列表
        users_list[clientAddress] = username
        print('Receive from ' + str(clientAddress[0]) + ':' + str(clientAddress[1]) + '--->' + username)
        # 向用户列表里的每一个用户发送信息
        send_message = username + ' has joined the chat!'
        for send_address in users_list.keys():
            serverSocket.sendto(send_message.encode(), send_address)
            print('Send to ' + str(send_address[0]) + ':' + str(send_address[1]) + "--->'" + send_message + "'")