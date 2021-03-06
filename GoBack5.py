# -*- coding:utf8 -*-
import threading
import random
import time

from demo_ui4 import *
# import demo_ui4



class GoBack(object):
    def __init__(self, m, prnList):
        self.lock = threading.Lock()
        self.lock2 = threading.Lock()
        self.timerInLock = threading.Lock()
        self.m = m
        self.sw = 2 ** self.m - 1
        self.sn = 0
        self.sf = 0
        self.rn = 0

        self.sf_str = None
        self.sn_str = None
        self.rn_str = None
        self.ack_str = None
        self.data = ''  # 暂时将发送的数据做为全局变量，也可以更改
        self.receiveData = []  # 暂时为接收到的数据做一个接收器，以后可以取消或者更改
        self.ack = None
        self.s_isrec = False
        self.framer = [str(x) for x in range(999900, 999916)]
        self.error = -1
        self.timerIn = 0
        self.timerOut = 0
        self.timerIndex = 0

        self.prnSf = prnList[0]
        self.prnSn = prnList[1]
        self.prnRn = prnList[2]
        self.prnAck = prnList[3]


        self.senderFace = [0] * (self.sw + 1)
        self.revFace = [0] * (self.sw + 1)
        self.sizeFace = [0] * (self.sw + 1)
        self.ack2 = -1

    # self.lis = threading.Thread(target=self.listener)
    # self.lis.spretDaemon(True)
    # self.lis.start()

    def sendProcess(self):
        s_send_thread = threading.Thread(target=self.s_send)
        s_send_thread.setDaemon(True)  # 子线程随父线程结束
        s_send_thread.start()

    def recvProcess(self):
        r_recv_thread = threading.Thread(target=self.r_receive)
        r_recv_thread.setDaemon(True)
        r_recv_thread.start()

    def timer(self, sn):

        def cot(sn, prn=None):

            self.lock.acquire()
            timerOut = self.timerOut
            self.lock.release()
            self.timerInLock.acquire()
            self.timerIn = self.timerIn + 1
            self.timerInLock.release()
            num = 3
            for i in range(num):
                if not self.check_ack(sn):  # 如果check成功，就可以了

                    if i == (num - 1):
                        # self.error = 1
                        print('sn is: ' + str(sn) + ' rn is: ' + str(self.rn) + ' sf is :' + str(
                            self.sf) + ' ack is :' + str(self.ack))

                        self.sf_str = ('sn is: ' + str(sn) + ' rn is: ' + str(self.rn) + ' sf is :' + str(
                            self.sf) + ' ack is :' + str(self.ack))

                        # print self.data[0:2]
                        self.timerInLock.acquire()
                        if self.timerIn == 1:
                            self.error = 1
                            self.sn = self.sf
                        self.timerInLock.release()
                        break
                    if prn != None:
                        prn(self.sf, self.sf_str)
                    time.sleep(1)
                else:
                    # self.sfLock.acquire()
                    self.sf = (self.ack + 1) % (self.sw + 1)
                    # self.errorPoint = -1
                    self.error = -1
                    self.timerInLock.acquire()
                    self.timerIn = 0
                    self.timerInLock.release()
                    self.lock.acquire()
                    self.timerOut = self.timerOut + 1
                    self.lock.release()
                    # self.sfLock.acquire()
                    if prn != None:
                        prn(self.sf, self.sf_str)

                    return
            self.timerInLock.acquire()
            if timerOut == self.timerOut:
                self.timerIn = self.timerIn - 1
            self.timerInLock.release()
            return

        cotThread = threading.Thread(target=cot, args=(sn, self.prnSf))
        cotThread.start()

    def check_OK(self, OkNum):  # 用于判断是否发送成功
        if (0 <= OkNum <= 0.8):
            return True
        else:
            return False

    def check_time(self):
        self.timerInLock.acquire()
        if self.timerIn == 1:
            self.timerInLock.release()
            return True
        else:
            self.timerInLock.release()
            return False



    def s_send(self):
        prn = self.prnSn

        while True:

            random_data = random.random()
            random_right = random.random()
            snAppend = str(self.sn)
            if len(snAppend) <= 1:
                snAppend = '0' + snAppend
            if self.error != 1:
                data = snAppend + str(int(random_data * 1000))  # 初始化一个发送的data
                self.framer[self.sn] = data


            else:
                data = self.framer[self.sn]

            print('Sending: ' + str(self.sn))
            self.sn_str = 'Sending: ' + str(self.sn)


            if self.check_OK(random_right):
                self.data = data  # 模拟正常发送包
            # self.lock.release()
            if not self.check_time():
                self.timer(self.sn)  # 这个函数如果正常退出，将会修改sf到sn的位置

            # self.lock.acquire()
            self.sn = (self.sn + 1) % (self.sw + 1)
            # self.lock.release()

            if prn != None:
                prn(self.sn, self.sn_str)
            time.sleep(0.6)


            # 目前并没有在这个函数里面去修改self.sf的值，而是在send函数中修改，虽然比较奇怪

    def check_ack(self, sn):  # 这个需要判断ack是否在目前的sn之后和是否在窗口之内，极其重要的一个函数

        nowSf = self.sf
        newList = [(x + nowSf) % (self.sw + 1) for x in range(self.sw)]  # 一句话生成目前窗口
        snIndex = newList.index(sn)
        sesnIndex = newList.index(self.sn)
        if self.ack != None and self.ack in newList:
            ackIndex = newList.index(self.ack)
        else:
            ackIndex = 10000

        if ackIndex <= sesnIndex and snIndex <= sesnIndex and nowSf == self.sf:
            return True
        else:
            return False

    def r_send(self, rn):
        prn = self.prnAck
        def ack_OK(rnNum):  # 用来模拟ack丢包

            ackOk = random.random()
            if ackOk <= 0.9:
                return True
            else:
                return False

        ack = rn
        if ack_OK(ack):
            self.ack = ack
            print('ack is: ' + str(self.ack))
            self.ack_str = 'ack is: ' + str(self.ack)
        if prn != None:
            prn(self.ack, self.ack_str)


    def r_receive(self):
        prn = self.prnRn
        while True:
            if self.data == '':
                continue
            if self.rn == int(self.data[0:2]):
                # print 'receving: ' + str(self.rn)
                self.receiveData.append(self.data[2:])
                # print self.data[2:]
                self.data = ''
                self.r_send(self.rn)
                self.rn = (self.rn + 1) % (2 ** self.m)
            if prn != None:
                prn(self.rn)
            time.sleep(0.2)

        # def listener(self):
        # 	while True:
        # 		senderFace = [0] * (self.sw + 1)
        # 		revFace = [0] * (self.sw + 1)
        # 		sizeFace = [0] * (self.sw + 1)
        # 		sn = self.sn
        # 		sf = self.sf
        # 		rn = self.rn
        # 		ack = self.ack
        # 		self.ack2 = (ack + 1) % (self.sw + 1)
        # 		sizeFace = [(x + sf) % (self.sw + 1) for x in range(self.sw)]
        # 		senderFace[sn] = 1
        # 		senderFace[sf] = -1
        # 		revFace[rn] = 1
        # 		self.senderFace = senderFace
        # 		self.revFace = revFace
        # 		self.sizeFace = sizeFace
        # 		time.sleep(0.1)


def main():
    goback = GoBack(4)
    goback.sendProcess()
    goback.recvProcess()


def gobackn_thread_start():
    print("start go back n protocol")
    main()


if __name__ == '__main__':
    mainThread = threading.Thread(target=main)
    mainThread.setDaemon(True)
    mainThread.start()
    while True:
        pass
