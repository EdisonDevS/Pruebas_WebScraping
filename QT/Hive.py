# -*- coding: utf-8 -*-
import sys
from PyQt5 import uic, QtWidgets
from selenium import webdriver
from selenium.webdriver.support.ui import Select

qtCreatorFile = "Hive.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.driver = webdriver.Chrome("/home/edison/chromedriver")
        self.driver.get('https://web.whatsapp.com/')
        self.btnEnviar.clicked.connect(self.enviar)

    def enviar(self):
        msg=self.txtMsg.toPlainText()
        
        name="Cacho"

        
        user = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        msg_box = self.driver.find_element_by_class_name('_2S1VP')

        msg_box.send_keys(msg)
        button = self.driver.find_element_by_class_name('_35EW6')
        button.click()

        self.txtMsg.clear()


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


"""
driver = webdriver.Chrome("/home/edison/chromedriver")
driver.get('https://web.whatsapp.com/')

while(True):
    name = input('Holi : ')
    msg = input('Wiiiii : ')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')

    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
"""