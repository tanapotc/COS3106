from socket import *
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
while True:
    print ("IN")
    message, clientAddress = serverSocket.recvfrom(2048)
    print ("Sucsess")
    modifiedMessage = message.decode().upper()
    print ("Decode")
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
    print ("as")