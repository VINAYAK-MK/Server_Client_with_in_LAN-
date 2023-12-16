import socket
from threading import Thread
from time import *
def input_taking():
	while True:
		m=input()
		client.send(bytes(m,"utf-8"))

def recv():
	while True:
		msg=(client.recv(1024)).decode("utf_8")
		print("                      "+msg)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	client.connect(("127.0.0.1",8080))
except socket.error as a:
	print("not connected")
msg=(client.recv(1024)).decode("utf-8")
t=Thread(target=input_taking)
t.start()
thy=Thread(target=recv)
thy.start()
