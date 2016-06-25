#sender

import socket
import binascii
import struct
import random
import threading
import time
from multiprocessing import Process

flag = 1
seq = 0
time_flag = 0
time_out = 0
err = 0

host = '127.0.0.1'
port = 9999
'''
sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sender.connect((host, port))

lock = threading.Lock()

def timer():
    global time_out
    global time_flag
    if time_flag == 0:
        for i in range(5):
            if time_flag == 1:
                time_flag = 0
                return
            time.sleep(1)
        lock.acquire()
        time_out = 1
        time_flag = 0
        lock.release()
        return
    else:
        return'''
class send:
    def __init__(self):
        global flag
        global seq
        global time_flag
        global time_out
        global err
        self.flag = 1
        self.seq = 0
        self.time_flag = 0
        self.time_out = 0
        self.err = 0
        self.copy = ''
        self.sender = ''
        self.lock = ''

    def init_socket(self):
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sender.connect((host, port))

        self.lock = threading.Lock()

    def timer(self):
        global time_out
        global time_flag
        if self.time_flag == 0:
            for i in range(5):
                if self.time_flag == 1:
                    self.time_flag = 0
                    return
                time.sleep(1)
            self.lock.acquire()
            self.time_out = 1
            self.time_flag = 0
            self.lock.release()
            return
        else:
            return

    def SEND(self):
        try:
            while True:
                data_type = random.random()
                self.lock.acquire()
                self.seq = (self.seq + 1) % 2
                self.lock.release()
                if data_type < 0.6:
                    random_str = str(data_type)[2:]
                    crc = hex(binascii.crc32(random_str) & b"0xffffffff")
                    data = str(self.seq) + random_str + crc
                    data = struct.pack('1024s', data)
                if 0.6 < data_type < 0.8:
                    data = 'lose'
                    self.copy = struct.pack('1024s', str(self.seq) + 'resend_data')
                if 0.8 < data_type < 1:
                    data = 'err'
                    self.copy = struct.pack('1024s', str(self.seq) + 'resend_data')
                if self.flag == 1:
                    self.lock.acquire()
                    self.sender.send(data)
                    print('send:', data)
                    self.flag = 0
                    print( 'seq_flag:', self.seq)
                    self.lock.release()
                self.timer()
                if self.time_out == 1 or self.err == 1:
                    self.lock.acquire()
                    print ('chongfa')
                    self.sender.send(self.copy)
                    self.time_out = 0
                    self.err = 0
                    self.seq = (self.seq + 1) % 2
                    print( 'seq_time_out:', self.seq)
                    self.lock.release()

        except KeyboardInterrupt:
            exit(0)

    def RECV(self):
        global flag
        global seq
        global time_flag
        global err
        try:
            while True:
                ack = self.sender.recv(1024)

                print ('ack:', ack)
                print ('seq:', seq)
                if str((self.seq + 1) % 2) == str(ack):
                    self.lock.acquire()
                    self.flag = 1
                    self.time_flag = 1
                    self.lock.release()
                    print ('ack:', ack)
                if str(ack) == 'nak' or str((self.seq + 1) % 2) != str(ack):
                    print ('nak')
                    self.lock.acquire()
                    self.err = 1
                    self.time_flag = 1
                    self.lock.release()

        except KeyboardInterrupt:
            exit(0)



def p():
    interface = send()
    interface.init_socket()
    send_thread = threading.Thread(target = interface.SEND)
    send_thread.start()
    recv_thread = threading.Thread(target = interface.RECV)
    recv_thread.start()
    while True:
        pass

proc = Process(target = p)
proc.start()

