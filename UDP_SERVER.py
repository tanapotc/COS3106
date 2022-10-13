from socket import *
import os
os.system('cls' if os.name == 'nt' else 'clear')
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
while True: 
    message, clientAddress = serverSocket.recvfrom(2048) 
    modifiedMessage = message.decode().upper() 
    print("From Client :",modifiedMessage)
    serverSocket.sendto(modifiedMessage.encode(),clientAddress) 