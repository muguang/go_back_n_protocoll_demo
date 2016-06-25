

import socket
import string

host = "127.0.0.1"
port = 10006


bufsize = 1024


receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


receiver.connect((host, port))




while True:
    data = input()
    if not data  or data=="exit":
        break

    receiver.send(data.encode())
    data = receiver.recv(bufsize).decode()

    if not data:
        break

    print(data.strip())


receiver.close()
