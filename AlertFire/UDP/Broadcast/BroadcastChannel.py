import socket

UDP_IP = "192.168.0.255"
UDP_PORT = 11202                        # ___  ____  ____  ____
MESSAGE = bytes([0x02, 0x07, 0x00, 0x10, 0xC0, 0xA8, 0x00, 0x03, 0xA0, 0x93, 0x03])

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
