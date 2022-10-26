from socket import *
import os
from turtle import clear
os.system('cls' if os.name == 'nt' else 'clear')
serverAddressPort = ('localhost' , 8080)
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = ''
while message != 'exit':
 message= input("Input lowercase sentence : ")
 clientSocket.sendto(str.encode(message),(serverAddressPort))
 modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
 print ("From Server :",modifiedMessage.decode())
 if message == 'clr':
    print("Clear screen Client press 1")
    print("Clear screen Server press 2")
    print("Clear screen Server & Client press 3")
    message = input("Input : ")
    match message :  
        case '1' :
            os.system('cls' if os.name == 'nt' else 'clear')
            clientSocket.sendto(str.encode('Clear Screen Client'),(serverAddressPort))
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print ("From Server :",modifiedMessage.decode())
        case '2' :
            message = 'CLEARSCR'
            clientSocket.sendto(str.encode(message),(serverAddressPort))
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print ("From Server :",modifiedMessage.decode())
        case '3' :
            message = 'CLEARSCR'
            clientSocket.sendto(str.encode('CLEARSCR'),(serverAddressPort))
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print ("From Server :",modifiedMessage.decode())
            os.system('cls' if os.name == 'nt' else 'clear')
        case 'help' :
            os.system('cls' if os.name == 'nt' else 'clear')  
            print("clr : use for clear screen") 
 if message == 'help' or message == 'HELP' :  
    os.system('cls' if os.name == 'nt' else 'clear')
    print("######### Help menu #########")
    print(" clr  : use for clear screen")
    print(" exit : use for exit from SERVER & CLIENT\n")
os.system('cls' if os.name == 'nt' else 'clear')
clientSocket.close()