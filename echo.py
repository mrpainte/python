import socket
import os

os.cpu_count()

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    temp = input("Please enter a phrase to be echoed back ")
    s.sendall(b'{temp}')
    data = s.recv(1024)

print('Received', repr(data))