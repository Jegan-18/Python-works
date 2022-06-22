server.py


import socket

s=socket.socket()
print("socket created")
s.bind(('localhost',9999))
s.listen()
print("waiting for connection")

while true:
    c,addr=s.accept()
    print('connected with',addr)
    c.send(bytes('welcome','utf-8')
    c.close()
    
    
client.py

import socket

c=socket.socket()
c.connect(('localhost',9999))
s.listen()
print(c.recv(1024))

