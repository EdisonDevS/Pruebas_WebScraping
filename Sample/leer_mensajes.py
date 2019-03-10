#-*- coding: utf-8 -*-
import sys
from selenium import webdriver

#Se crea un objeto correspondiente al driver de crome que se descargó con anterioridad
driver = webdriver.Chrome("/home/edison/chromedriver")

#Se le solicita al driver que cargue la pagina de WhatsApp
driver.get('https://web.whatsapp.com/')

#Se crea un loop donde se ejecutará el aplicativo
while(True):
    #Se pide el nombre de destinatario al que se va a enviar el mensaje
    name = input('\nContacto : ')

    #En el navegador se busca el span cuya propiedad de titulo en HTML es igual al nombre del usuario
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    #se ubican los mensajes de salida por su xpath
    salida=driver.find_elements_by_xpath('//div[@class = "_3_7SH _3DFk6 message-out" or @class = "_3_7SH _3DFk6 message-out tail"]/div[@class="Tkt2p"]/div[@class="copyable-text"]/div[@class="_3zb-j ZhF0n"]/span[@class="selectable-text invisible-space copyable-text"]')

    print("\nMENSAJES ENVIADOS:")
    for x in salida:
        print (x.get_attribute('innerHTML'))

    #se ubican los mensajes de entrada por su xpath
    entrada=driver.find_elements_by_xpath('//div[@class = "_3_7SH _3DFk6 message-in" or @class = "_3_7SH _3DFk6 message-in tail"]/div[@class="Tkt2p"]/div[@class="copyable-text"]/div[@class="_3zb-j ZhF0n"]/span[@class="selectable-text invisible-space copyable-text"]')

    print("\nMENSAJES RECIBIDOS:")
    for x in entrada:
        print (x.get_attribute('innerHTML'))

    
    todos=driver.find_elements_by_xpath('//span[@class="selectable-text invisible-space copyable-text"]')

    print("\nTODOS LOS MENSAJES:")
    for x in todos:
        print (x.get_attribute('innerHTML'))