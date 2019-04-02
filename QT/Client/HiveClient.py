# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtGui, QtCore, uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import socket

config=("localhost",10000)

qtCreatorFile = "Hive.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.actual_contact=""
        self.setupUi(self)
        self.ftc=False
        self.btnEnviar.clicked.connect(self.first_time_connection)

    def first_time_connection(self):
        if self.ftc:
            self.send_msg()
        else:
            self.request_contacts()

    def request_contacts(self):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(config)
        print("conexion establecida")
        msg="FirstTimeConnectionRequest€contacts"

        sock.send(msg.encode('utf-8'))

        #solicito todos los contactos
        self.contacts=[]
        contacto=sock.recv(1000)
        contactos=contacto.decode('utf-8').split("€")
        for x in contactos:
            button = QtWidgets.QPushButton(x)
            button.clicked.connect(self.setContact)
            self.contacts.append(button)

        for x in self.contacts:
            self.layCont.addWidget(x)

        sock.close()
        self.ftc=True

    def setContact(self):
        for x in self.contacts:
            if x is self.sender():
                self.actual_contact=x.text()
                self.lblChat.setText("Chat: "+x.text())

        for i in reversed(range(self.layIn.count())): 
            self.layIn.itemAt(i).widget().deleteLater()
            self.layOut.itemAt(i).widget().deleteLater()

        print("actualizando")
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(config)
        actualizar=self.actual_contact+"€MessagesRequest"
        sock.send(actualizar.encode('utf-8'))
           
        while True:
            paquete=sock.recv(4000) 
            #self.Ordenar(historial)
            if paquete:
                sock.close()
                paquete=paquete.decode('utf-8')
                print (paquete)
                self.Ordenar(paquete)
                break


    def Ordenar(self, paquete):
        enviadosString=paquete.split("<=>")[0]
        recibidosString=paquete.split("<=>")[1]
        todosString=paquete.split("<=>")[2]

        enviados=enviadosString.split("€")
        recibidos=recibidosString.split("€")
        todos=todosString.split("€")

        todos.remove(todos[0])
        enviados.remove(enviados[0])
        recibidos.remove(recibidos[0])

        send_buttons=[]
        recived_buttons=[]
        while todos!=[]:
            if enviados!=[] and todos[0]==enviados[0]:
                #print("Yo: "+enviados[0])
                button = QtWidgets.QPushButton(enviados[0])
                button.setStyleSheet("border: 0px solid rgb(224, 161, 75); background-color: rgb(224, 161, 75);border-radius: 5px")
                send_buttons.append(button)
                void_button = QtWidgets.QPushButton("")
                void_button.setStyleSheet("border: 0px solid white;") 
                recived_buttons.append(void_button)
                todos.remove(todos[0])
                enviados.remove(enviados[0])
            elif recibidos!=[] and todos[0]==recibidos[0]:
                #print("Otro: "+recibidos[0])
                void_button = QtWidgets.QPushButton("")
                void_button.setStyleSheet("border: 0px solid white;")
                send_buttons.append(void_button)
                button = QtWidgets.QPushButton(recibidos[0])
                button.setStyleSheet("border: 0px solid rgb(232, 225, 71);background-color: rgb(232, 225, 71);border-radius: 5px")
                recived_buttons.append(button)
                todos.remove(todos[0])
                recibidos.remove(recibidos[0])
            else:
                todos.remove(todos[0])
        
        for btn in send_buttons:
            self.layOut.addWidget(btn)
        
        for btn in recived_buttons:
            self.layIn.addWidget(btn)

    def send_msg(self):
        msg=self.txtMsg.toPlainText()
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(config)
        print("conectado")
        msg=self.actual_contact+"€"+msg
        sock.send(msg.encode('utf-8'))
        sock.close()
        self.txtMsg.clear()

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())