import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.2.179', 11203))
server_socket.listen(0)
client_socket, addr = server_socket.accept()
data = client_socket.recv(65535)
print("recieve Data:", data.decode())
