import socket
from TCP import send
from TCP.send import sendNormal

TCP_IP = '192.168.0.3'
TCP_PORT = 11201
BUFFER_SIZE = 82  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

s.listen(1)
conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print("received data:", data)
    normalData = sendNormal()
    conn.send(bytes(normalData))  # echo


conn.close()
print("disconnected")