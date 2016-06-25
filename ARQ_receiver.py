#receiver

import socket
import binascii
import struct
import threading
from multiprocessing import Process

seq = 0
err = 0
lose = 0
normal = 0

host = "127.0.0.1"
port = 9999
'''
receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

receiver.bind((host, port))

receiver.listen(1)

conn, addr = receiver.accept()

lock = threading.Lock()'''

class recive:
    def __init__(self):
        self.seq = 0
        self.err = 0
        self.lose = 0
        self.normal = 0
        self.receiver = ''
        self.conn = ''
        self.addr = ''
        self.lock = ''
        self.packed_data = ''
        self.data = ''

    def init_socket(self):
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.receiver.bind((host, port))
        self.receiver.listen(1)
        self.conn, self.addr = self.receiver.accept()
        self.lock = threading.Lock()

    def RECEIVE(self):
        global seq
        global err
        global lose
        global normal
        try:
            while True:
                self.packed_data = self.conn.recv(1024)
                #data, = struct.unpack('1024s', packed_data)
                print('recv:', self.packed_data)
                if self.packed_data == 'lose':
                    self.lock.acquire()
                    self.lose = 1
                    self.lock.release()
                    continue
                if self.packed_data == 'err':
                    self.lock.acquire()
                    self.err = 1
                    self.lock.release()
                    continue
                else:
                    print ("normal")
                    self.data, = struct.unpack('1024s', self.packed_data)
                    self.lock.acquire()
                    self.seq = int(self.data[0])
                    self.normal = 1
                    self.lose = 0
                    self.err = 0
                    self.lock.release()
                    print ('normal:', normal)

                #print seq
        except KeyboardInterrupt:
            self.receiver.close()
            exit(0)

    def SEND(self):
        global seq
        global lose
        global err
        global normal
        try:
            while True:
                if self.lose == 1:
                    continue
                if self.err == 1:
                    self.lock.acquire()
                    self.err = 0
                    self.lock.release()
                    self.conn.send('nak')
                if self.normal == 1:
                    self.lock.acquire()
                    self.lose = 0
                    self.err = 0
                    self.normal = 0
                    self.seq = (self.seq + 1) % 2
                    self.conn.send(str(self.seq))
                    self.lock.release()
                    print ('send:', self.seq)
        except KeyboardInterrupt:
            self.receiver.close()
            exit(0)

def p():
    interface = recive()
    interface.init_socket()
    recv_thread = threading.Thread(target = interface.SEND)
    recv_thread.start()
    send_thread = threading.Thread(target = interface.RECEIVE)
    send_thread.start()
    while True:
        pass

proc = Process(target = p)
proc.start()

