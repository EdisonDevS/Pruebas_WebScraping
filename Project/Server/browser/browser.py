from selenium import webdriver
from time import sleep

class browser:
    def __init__(self):
        self.contacts=""
        self.messages=""
        self.messagePackage=""

        self.driver=webdriver.Chrome('browser/driver/chromedriver')
        self.driver.set_window_size(1400,10000)
        self.driver.get("https://web.whatsapp.com/")

    def updateContacts(self):
        chats = self.driver.find_elements_by_xpath('//span[@class = "_1wjpf"]')

        self.contacts=""
        for contact in chats:
            name=contact.get_attribute("title")
            self.contacts = self.contacts + "€" + name


    def getContacts(self):
        self.updateContacts()        
        return self.contacts.encode('utf-8')


    def sentMessages(self):
        sent = self.driver.find_elements_by_xpath('//div[@class = "_3_7SH _3DFk6 message-out" or @class = "_3_7SH _3DFk6 message-out tail"]/div[@class="Tkt2p"]/div[@class="copyable-text"]/div[@class="_3zb-j ZhF0n"]/span[@class="selectable-text invisible-space copyable-text"]')

        for mess in sent:
            self.messagePackage=self.messagePackage+'€'+mess.get_attribute('innerHTML')
        
        self.messagePackage=self.messagePackage+'<=>'


    def recivedMessages(self):
        recived=self.driver.find_elements_by_xpath('//div[@class = "_3_7SH _3DFk6 message-in" or @class = "_3_7SH _3DFk6 message-in tail"]/div[@class="Tkt2p"]/div[@class="copyable-text"]/div[@class="_3zb-j ZhF0n"]/span[@class="selectable-text invisible-space copyable-text"]')

        for mess in recived:
            self.messagePackage=self.messagePackage+'€'+mess.get_attribute('innerHTML')
        
        self.messagePackage=self.messagePackage+'<=>'

    
    def allMessages(self):
        total = self.driver.find_elements_by_xpath('//span[@class="selectable-text invisible-space copyable-text"]')

        for mess in total:
            self.messagePackage=self.messagePackage+'€'+mess.get_attribute('innerHTML')

        

    def getMessages(self, contact):
        
        self.messagePackage=""

        user = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact))
        user.click()

        sleep(2)

        self.sentMessages()
        self.recivedMessages()
        self.allMessages()

        return self.messagePackage.encode('utf-8')
    
        print('No se ha encontrado el contacto')


    def sendMessage(self, contact, message):
        try:
            user=self.driver.find_element_by_xpath('//span[@title="{}"]'.format(contact))
            user.click()
            
            textBox=self.driver.find_element_by_class_name("_2S1VP")
            textBox.send_keys(message)

            sendButton=self.driver.find_element_by_class_name("_35EW6")
            sendButton.click()
        except:
            print("No se ha encontrado el contacto")                
            