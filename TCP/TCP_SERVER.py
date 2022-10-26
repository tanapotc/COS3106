from socket import *
import os
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
os.system('cls' if os.name == 'nt' else 'clear')
print ("The server is ready to receive")
while True: 
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    print("From Client :",sentence)
    connectionSocket.close() 