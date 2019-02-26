#-*- coding: utf-8 -*-
import sys
from selenium import webdriver
import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

config=("192.168.0.17",10000)

while True:
    contacto=input("Contacto: ")
    send_msg(contacto)

def send_msg(contacto):
    sock.connect(config)
    print("conexion establecida")
    sock.send(contacto.encode('utf-8'))
    msg=input("Mensaje: ")
    sock.send(msg.encode('utf-8'))
    sock.close()