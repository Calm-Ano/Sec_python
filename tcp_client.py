# coding: utf-8

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "127.0.0.1"
port = 8080

server = (ip, port)
sock.connect(server)

msg = ''
while msg != 'exit':
    msg = input("t_c>")
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data)

sock.close()