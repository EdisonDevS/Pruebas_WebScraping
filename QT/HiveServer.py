#-*- coding: utf-8 -*-
import sys
from selenium import webdriver
import socket
from time import sleep

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Iniciando servidor")
config=("localhost",10000)
sock.bind(config)
sock.listen(1)

print("Servidor en pie")

driver=webdriver.Chrome("/home/edison/chromedriver")
driver.get("https://web.whatsapp.com/")

while True:
    con, direccion = sock.accept()
    print("coneccion desde: "+direccion[0])
    while True:
        mensaje=con.recv(4000)
        if mensaje:
            mensaje=mensaje.decode('utf-8')
            mensaje_descompuesto=mensaje.split('€')
            contacto=mensaje_descompuesto[0]
            msg=mensaje_descompuesto[1]
            
            if contacto=="ftc_request":
                #se solicitan los contactos para la primera conección

                chats = driver.find_elements_by_xpath('//span[@class = "_1wjpf"]')

                cant_contacts=str(len(chats))
                
                con.send(cant_contacts.encode('utf-8'))

                contacts=""
                for contacto in chats:
                    nombre = contacto.get_attribute("title")
                    contacts = contacts + "€" + nombre

                con.send(contacts.encode('utf-8'))    
            else:
                print("Contacto: "+contacto)
                print("Mensaje: "+msg)
                try:
                    usuario=driver.find_element_by_xpath('//span[@title="{}"]'.format(contacto))
                    usuario.click()
                except:
                    print("No se ha encontrado el contacto")

                caja=driver.find_element_by_class_name("_2S1VP")
                caja.send_keys(msg)

                enviar=driver.find_element_by_class_name("_35EW6")
                enviar.click()
            
            break