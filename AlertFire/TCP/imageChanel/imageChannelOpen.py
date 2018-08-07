import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.237', 0))
server_socket.listen(0)
client_socket, addr = server_socket.accept()
data = client_socket.recv(11203)
print("recieve Data:", data.decode())
