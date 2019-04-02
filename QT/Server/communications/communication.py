import socket
from .config import *

class communication:
    def __init__(self, host, port):
        self.clientConnection=None
        self.clientAddres=None

        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        configuration=config()
        configuration.setHost(host)
        configuration.setPort(port)

        print("Iniciando servidor")
        self.sock.bind(configuration.getConfig())
        self.sock.listen(1)
        print ("Servicio a la escucha en " + configuration.getHost() + ":" + configuration.getPort())

    def getClientConnection(self):
        self.clientConnection,self.clientAddres=self.sock.accept()
        print("Nueva conexion desde: "+self.clientAddres[0])
    
    def getClientAddres(self):
        return self.clientAddres

    def reciveMessage(self):
        while True:
            message=self.clientConnection.recv(4000)
            if message:
                return message.decode('utf-8')

    def sendMessage(self, message):
        self.clientConnection.send(message)
