#-*- coding: utf-8 -*-
import sys
from selenium import webdriver

driver=webdriver.Chrome("/home/edison/chromedriver")

driver.get("https://web.whatsapp.com/")

while(True):
    cont=input("Contacto: ")
    msg=input("Mensaje: ")

    try:
        usuario=driver.find_element_by_xpath('//span[@title="{}"]'.format(cont))
        usuario.click()
    except:
        print("No se ha encontrado el contacto")

    caja=driver.find_element_by_class_name("_2S1VP")
    caja.send_keys(msg)

    enviar=driver.find_element_by_class_name("_35EW6")
    enviar.click()