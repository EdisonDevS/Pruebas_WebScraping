# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtGui, QtCore, uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import socket
from config.config import *
from communications.communication import *
from message.message import *

qtCreatorFile = "UI/Hive.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.serverConfig=config()
        self.actualContact=""
        self.setupUi(self)
        self.isFirstConnection=False
        self.sendButton.clicked.connect(self.first_time_connection)

    def first_time_connection(self):
        if self.isFirstConnection:
            self.sendMessage()
        else:
            self.request_contacts()

    def request_contacts(self):
        service=communication()
        service.sendMessage("FirstTimeConnectionRequest€contacts".encode('utf-8'))
        recivedContacts=service.reciveMessage()
        service.__del__()

        #solicito todos los contactos
        self.contacts=[]
        
        contacts=recivedContacts.split("€")

        for contact in contacts:
            button = QtWidgets.QPushButton(contact)
            button.clicked.connect(self.setContact)
            self.contacts.append(button)

        for contact in self.contacts:
            self.layCont.addWidget(contact)

        self.isFirstConnection=True

    def setContact(self):
        for x in self.contacts:
            if x is self.sender():
                self.actualContact=x.text()
                self.lblChat.setText("Chat: "+x.text())

        for i in reversed(range(self.layIn.count())): 
            self.layIn.itemAt(i).widget().deleteLater()
            self.layOut.itemAt(i).widget().deleteLater()

        print("actualizando")

        service=communication()
        messageString=self.actualContact+"€MessagesRequest"
        service.sendMessage(messageString.encode('utf-8'))
        recivedMessages=service.reciveMessage()
        service.__del__()

        package=recivedMessages
        self.sort(package)


    def sort(self, package):
        sentMessagesString=package.split("<=>")[0]
        recivedMessagesString=package.split("<=>")[1]
        allMessagesString=package.split("<=>")[2]

        sentMessages=sentMessagesString.split("€")
        recivedMessages=recivedMessagesString.split("€")
        allMessages=allMessagesString.split("€")

        allMessages.remove(allMessages[0])
        sentMessages.remove(sentMessages[0])
        recivedMessages.remove(recivedMessages[0])

        sendButtons=[]
        recivedButtons=[]
        while allMessages!=[]:
            if sentMessages!=[] and allMessages[0]==sentMessages[0]:
                #print("Yo: "+enviados[0])
                button = QtWidgets.QPushButton(sentMessages[0])
                button.setStyleSheet("border: 0px solid rgb(224, 161, 75); background-color: rgb(224, 161, 75);border-radius: 5px")
                sendButtons.append(button)
                void_button = QtWidgets.QPushButton("")
                void_button.setStyleSheet("border: 0px solid white;") 
                recivedButtons.append(void_button)
                allMessages.remove(allMessages[0])
                sentMessages.remove(sentMessages[0])
            elif recivedMessages!=[] and allMessages[0]==recivedMessages[0]:
                #print("Otro: "+recibidos[0])
                void_button = QtWidgets.QPushButton("")
                void_button.setStyleSheet("border: 0px solid white;")
                sendButtons.append(void_button)
                button = QtWidgets.QPushButton(recivedMessages[0])
                button.setStyleSheet("border: 0px solid rgb(232, 225, 71);background-color: rgb(232, 225, 71);border-radius: 5px")
                recivedButtons.append(button)
                allMessages.remove(allMessages[0])
                recivedMessages.remove(recivedMessages[0])
            else:
                allMessages.remove(allMessages[0])
        
        self.addButtons(sendButtons, recivedButtons)


    def addButtons(self, sendButtons, recivedButtons):
        for button in sendButtons:
            self.layOut.addWidget(button)
        
        for button in recivedButtons:
            self.layIn.addWidget(button)

    def sendMessage(self):
        service=communication()
        messenger=message(self.actualContact,self.txtMsg.toPlainText())
        service.sendMessage(messenger.getPackagedMessage())
        self.txtMsg.clear()

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
