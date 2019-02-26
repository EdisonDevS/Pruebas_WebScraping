#-*- coding: utf-8 -*-
import sys
from selenium import webdriver
import socket

config=("192.168.0.43",10000)

def send_msg(contacto):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(config)
    print("conexion establecida")
    sock.send(contacto.encode('utf-8'))
    msg=input("Mensaje: ")
    sock.send(msg.encode('utf-8'))
    sock.close()

while True:
    contacto=input("Contacto: ")
    send_msg(contacto)

