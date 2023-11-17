import socket
from socket import *


HOST = "127.0.0.1"
PORT = 6969 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ghost:
    ghost.bind((HOST, PORT))
    ghost.listen()
    conn, address = ghost.accept()
    with conn:
        print(f"Established new operator from: {address}")
        while True:
            data = conn.recv(4096)
            if not data:
                continue
            conn.sendall(data)