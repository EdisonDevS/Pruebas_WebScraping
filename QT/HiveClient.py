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
        msg="ftc_request€contacts"

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

    def send_msg(self):
        msg=self.txtMsg.toPlainText()
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(config)
        print("conexion establecida")
        msg=self.actual_contact+"€"+msg
        sock.send(msg.encode('utf-8'))
        sock.close()
        self.txtMsg.clear()


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())