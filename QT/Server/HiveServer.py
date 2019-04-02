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

driver=webdriver.Chrome("driver/chromedriver")
driver.set_window_size(1400,10000)
driver.get("https://web.whatsapp.com/")

while True:
    con, direccion = sock.accept()
    print("conexion desde: "+direccion[0])
    while True:
        mensaje=con.recv(4000)
        if mensaje:
            mensaje=mensaje.decode('utf-8')
            mensaje_descompuesto=mensaje.split('€')
            contacto=mensaje_descompuesto[0]
            msg=mensaje_descompuesto[1]
            
            if contacto=="ftc_request":
                #se solicitan los contactos para la primera conexión

                chats = driver.find_elements_by_xpath('//span[@class = "_1wjpf"]')

                contacts=""
                for contacto in chats:
                    nombre = contacto.get_attribute("title")
                    contacts = contacts + "€" + nombre

                print(contacts)
                con.send(contacts.encode('utf-8'))
            elif msg=="#$%":
                try:
                    paquete=""
                    #En el navegador se busca el span cuya propiedad de titulo en HTML es igual al nombre del usuario
                    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(contacto))
                    user.click()

                    sleep(2)

                    #se ubican los mensajes de salida por su xpath
                    salida=driver.find_elements_by_xpath('//div[@class = "_3_7SH _3DFk6 message-out" or @class = "_3_7SH _3DFk6 message-out tail"]/div[@class="Tkt2p"]/div[@class="copyable-text"]/div[@class="_3zb-j ZhF0n"]/span[@class="selectable-text invisible-space copyable-text"]')

                    print("\nMENSAJES ENVIADOS:")
                    for x in salida:
                        print (x.get_attribute('innerHTML'))
                        paquete=paquete+"€"+x.get_attribute('innerHTML')

                    paquete=paquete+"<=>"
                    #se ubican los mensajes de entrada por su xpath
                    entrada=driver.find_elements_by_xpath('//div[@class = "_3_7SH _3DFk6 message-in" or @class = "_3_7SH _3DFk6 message-in tail"]/div[@class="Tkt2p"]/div[@class="copyable-text"]/div[@class="_3zb-j ZhF0n"]/span[@class="selectable-text invisible-space copyable-text"]')

                    print("\nMENSAJES RECIBIDOS:")
                    for x in entrada:
                        print (x.get_attribute('innerHTML'))
                        paquete=paquete+"€"+x.get_attribute('innerHTML')

                    paquete=paquete+"<=>"                                                                       
                    todos=driver.find_elements_by_xpath('//span[@class="selectable-text invisible-space copyable-text"]')

                    print("\nTODOS LOS MENSAJES:")
                    for x in todos:
                        print (x.get_attribute('innerHTML'))
                        paquete=paquete+"€"+x.get_attribute('innerHTML')

                    con.send(paquete.encode('utf-8'))
                    print("se envió")
                except:
                    print("No se ha encontrado el contacto")
            else:
                print("Contacto: "+contacto)
                print("Mensaje: "+msg)
                try:
                    usuario=driver.find_element_by_xpath('//span[@title="{}"]'.format(contacto))
                    usuario.click()
                    caja=driver.find_element_by_class_name("_2S1VP")
                    caja.send_keys(msg)

                    enviar=driver.find_element_by_class_name("_35EW6")
                    enviar.click()
                except:
                    print("No se ha encontrado el contacto")
            
            break