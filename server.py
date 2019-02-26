#-*- coding: utf-8 -*-
import sys
from selenium import webdriver
import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Iniciando servidor")
config=("192.168.0.43",10000)
sock.bind(config)
sock.listen(100)

print("Servidor en pie")

driver=webdriver.Chrome("/home/edison/chromedriver")
driver.get("https://web.whatsapp.com/")

while True:
    con, direccion = sock.accept()
    print("coneccion desde: "+direccion[0])
    contacto=con.recv(4000)

    if contacto:
        while True:
            msg=con.recv(4000)
            if msg:
                print("Leegó: "+msg.decode('utf-8'))
                try:
                    usuario=driver.find_element_by_xpath('//span[@title="{}"]'.format(contacto.decode('utf-8')))
                    usuario.click()
                except:
                    print("No se ha encontrado el contacto")

                caja=driver.find_element_by_class_name("_2S1VP")
                caja.send_keys(msg.decode('utf-8'))

                enviar=driver.find_element_by_class_name("_35EW6")
                enviar.click()
                break