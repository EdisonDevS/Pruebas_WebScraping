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
        chats = self.driver.find_elements_by_xpath('//span[@class = "_19RFN"]')

        self.contacts=""
        for contact in chats:
            name=contact.get_attribute("title")
            self.contacts = self.contacts + "€" + name


    def getContacts(self):
        self.updateContacts()        
        return self.contacts.encode('utf-8')


    def sentMessages(self):
        sent = self.driver.find_elements_by_xpath('//div[@class = "_1zGQT _2ugFP message-out" or @class = "_1zGQT _2ugFP message-out tail"]/div[@class="-N6Gq"]/div[@class="copyable-text"]/div[@class="_12pGw EopGb"]/span[@class="selectable-text invisible-space copyable-text"]')
        print(sent)
        for mess in sent:
            self.messagePackage=self.messagePackage+'€'+mess.get_attribute('innerHTML')
        
        self.messagePackage=self.messagePackage+'<=>'


    def recivedMessages(self):
        recived=self.driver.find_elements_by_xpath('//div[@class = "_1zGQT _2ugFP message-in" or @class = "_1zGQT _2ugFP message-in tail"]/div[@class="-N6Gq"]/div[@class="copyable-text"]/div[@class="_12pGw EopGb"]/span[@class="selectable-text invisible-space copyable-text"]')
        print(recived)
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
            
            textBox=self.driver.find_element_by_class_name("_13mgZ")
            textBox.send_keys(message)

            sendButton=self.driver.find_element_by_class_name("_3M-N-")
            sendButton.click()
        except:
            print("No se ha encontrado el contacto")                
            