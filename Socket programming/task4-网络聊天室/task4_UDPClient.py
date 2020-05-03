from socket import *
import threading

def recvData():
    while True:
        message, serverAddress = clientSocket.recvfrom(2048)
        quit_message = username + " has left the chat!"
        if message.decode() == quit_message:
            clientSocket.close()
            break
        else:
            print(message.decode())

def sendData():
    while True:
        send_message = input()
        if send_message == '<quit>':
             clientSocket.sendto(send_message.encode(), (serverName, serverPort))
             break
        else:
            clientSocket.sendto(send_message.encode(), (serverName, serverPort))

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # IPv4, UDP
username = input('Please input your nickname:')
clientSocket.sendto(username.encode(), (serverName, serverPort))
print('Welcome ' + username + ', input <quit> to quit the chat!')

thread_1 = threading.Thread(target=recvData)
thread_2 = threading.Thread(target=sendData)
thread_1.start()
thread_2.start()