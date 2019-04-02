import socket
from .config import *

class communication:
    def __init__(self, host="localhost", port=10000):
        self.clientConnection=None
        self.clientAddres=None

        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        configuration=config()
        configuration.setHost(host)
        configuration.setPort(port)

        self.sock.connect(configuration.getConfig())


    def getClientAddres(self):
        return self.clientAddres


    def reciveMessage(self):
        while True:
            message=self.sock.recv(4000)
            if message:
                return message.decode('utf-8')


    def sendMessage(self, message):
        self.sock.send(message)
    
    def __del__(self):
        self.sock.close()
