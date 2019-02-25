import socket
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Esperando para levantar el servidor\n")
server_address = ('localhost', 10000)
sock.bind(server_address)

driver = webdriver.Chrome("/home/edison/chromedriver")
driver.get('https://web.whatsapp.com/')

sock.listen(1)

try:
    while True:
        print("Servidor en linea\n")
        connection, client_address = sock.accept()

        #se envia la lista de contactos cuando se realiza la conexion
        button = driver.find_elements_by_class_name('rAUz7')
        button[1].click()

        chats = driver.find_elements_by_xpath('//span[@class = "_1wjpf"]')

        cant_contacts=bytes(str(len(chats)),'utf-8')
        
        connection.send(cant_contacts)

        for contacto in chats:
            nombre = bytes('    - \n' + contacto.get_attribute("title"), 'utf-8')
   
            print(nombre)
            connection.send(nombre)

        connection.send(bytes("fin", 'utf-8'))
        name="Sandwichman"

        while(True):
            msg=connection.recv(4000)

            if msg:
                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                user.click()

                msg_box = driver.find_element_by_class_name('_2S1VP')
                msg_box.send_keys(msg.decode('utf-8'))

                button = driver.find_element_by_class_name('_35EW6')
                button.click()
finally:
    connection.close()

 
