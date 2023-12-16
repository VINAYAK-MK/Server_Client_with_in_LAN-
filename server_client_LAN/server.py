import socket 
import threading
from time import sleep

members_lock = threading.Lock()
def add_member(member,add):
	print(f"connected to {member}")
	member.send(bytes("Connected","utf-8"))  #sent a message when 1 stly connected
	while True:
		msg=member.recv(1024).decode("utf-8")
		global members
		with members_lock:
			clnts=members
		for i in clnts:
			if i!=member:
				i.send(bytes(msg.encode()))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1",8080))
server.listen()
print("Listening for connections...")
members=[]
while True:
	member, addr = server.accept()
	members.append(member)
	t=threading.Thread(target=add_member,args=(member,addr))
	t.start()

