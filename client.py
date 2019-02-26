#-*- coding: utf-8 -*-
import sys
from selenium import webdriver
import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

config=("192.168.0.17",10000)
print("Conectndo con servidor")
sock.connect(config)
print("conexion establecida")

contacto=input("Contacto: ")

sock.send(contacto.encode('utf-8'))

while True:
    msg=input("Mensaje: ")
    sock.send(msg.encode('utf-8'))
    sock.close()