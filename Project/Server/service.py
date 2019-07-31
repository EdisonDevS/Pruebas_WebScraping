# -*- coding: utf-8 -*-
import sys
from browser.browser import *
from communications.communication import *
from message.message import *

class service:
    def __init__(self, host="localhost", port=10000):
        self.server=communication(host,port)

    def start(self):
        web=browser()

        while True:
            self.server.getClientConnection()
            self.message = message(self.server.reciveMessage())

            if self.message.getContact() == "FirstTimeConnectionRequest":
                contacts = web.getContacts()
                self.server.sendMessage(contacts)
            elif self.message.getMessage() == "MessagesRequest":
                messagesPackage=web.getMessages(self.message.getContact())
                self.server.sendMessage(messagesPackage)
            else:
                web.sendMessage(self.message.getContact(), self.message.getMessage())
            


