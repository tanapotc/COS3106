from socket import *
import os
os.system('cls' if os.name == 'nt' else 'clear')
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
modifiedMessage = ''
while modifiedMessage != 'EXIT': 
    message, clientAddress = serverSocket.recvfrom(2048)  
    modifiedMessage = message.decode().upper()  
    print("From Client :",modifiedMessage)
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)  
    if modifiedMessage == 'CLEARSCR' :
        os.system('cls' if os.name == 'nt' else 'clear') 
        print ("The server is ready to receive")  
os.system('cls' if os.name == 'nt' else 'clear')
serverSocket.close()