from socket import *
import os
os.system('cls' if os.name == 'nt' else 'clear')
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Input lowercase sentence: ")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ("From Server :", modifiedSentence.decode())
clientSocket.close()