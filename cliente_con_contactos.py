import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (sys.argv[1], 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
print("Los chats disponibles son: \n")

c=0

while(True):
    cant_contacts=sock.recv(10)
    if(cant_contacts):
        c=int(cant_contacts.decode('utf-8'))
        break


for x in range(c):
    contacto=sock.recv(1000)
    print(contacto.decode('utf-8'))

try:
    while(True):
        msg=input("Mensaje: ")
        sock.send(bytes(msg, 'utf-8'))

finally:
    sock.close()