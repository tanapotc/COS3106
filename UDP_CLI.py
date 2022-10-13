from socket import *
import os
os.system('cls' if os.name == 'nt' else 'clear')
serverAddressPort = ('localhost' , 8080)
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input("Input lowercase sentence: ")
clientSocket.sendto(str.encode(message),(serverAddressPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())
clientSocket.close()