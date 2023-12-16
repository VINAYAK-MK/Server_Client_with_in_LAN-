import socket
from threading import Thread

server_IP="IP adress of device in wwhich server code is running and type should be String"
port="port number on which server is listening and type should be integer"

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
	client.connect(("server_IP",port))
except socket.error as a:
	print("not connected")
msg=(client.recv(1024)).decode("utf-8")
take_input=Thread(target=input_taking)
take_input.start()
recieve=Thread(target=recv)
recieve.start()
