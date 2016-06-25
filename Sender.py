


import socketserver
from socketserver import StreamRequestHandler as SRH
from time import ctime

host = "127.0.0.1"
port = 10006

addr = (host, port)


class Sender(SRH):
    def handle(self):
        print("connected from ", self.client_address)

        while True:
            data = self.request.recv(1024).decode()
            if not data:
                break
            print(data)

            self.request.send(data.encode())




print("server is running")


sendder = socketserver.ThreadingTCPServer(addr,Sender)

sendder.serve_forever()



