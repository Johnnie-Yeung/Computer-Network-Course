from socket import *
#获取计算机名称
hostname=gethostname()
#获取本机IP
ip=gethostbyname(hostname)
clientPort=7179  #如何在未连接前得知自己的本地端口号？

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)         # 用socket函数来创建客户套接字。第一个参数指示底层网络使用的是IPv4。第二个参数指示该套接字是SOCK_STREAM 类型。这表明它是一个 TCP 套接字，而不是一个 UDP 套接字。
print('A client is running.')
print("The client address: ('", str(ip), "', ", str(clientPort), ')')

if clientSocket.connect((serverName, serverPort)):    # 如果成功建立TCP连接
    print('Connected to ', serverName, ':', serverPort, '.')    # connect()方法的参数是这条连接中服务器端的地址。这行代码执行完后，执行三次握手，并在客户和服务器之间创建起一条TCP连接。一般address的格式为元组(hostname,port)
    sentence = input('Send a request:')
    clientSocket.send(sentence.encode())  # 向服务器发送字符串sentence
    modifiedSentence = clientSocket.recv(1024)  # 接收
    while True:
        if sentence == 'Time':
            print('Received the current system time on the server: ',modifiedSentence.decode(),'.')  # 字符串modifiedSentence
        elif sentence == 'Exit':
            print('Received a response: ',modifiedSentence.decode())
            break
clientSocket.close()   # 关闭套接字
