# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
# import sys
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
from GoBack5 import *


# d_rn = None
# d_sn = None
# d_ack = None
# d_sf = None
#
# def check_the_info_sf(sf):
#     print("start the check_info function--" + "sf" * 10)
#     print("sf : ", sf)
#
#     d_rn = sf
#
#
# def check_the_info_sn(sn):
#     print("start the check_info function--" + "sn" * 10)
#     print("ack: ", sn)
#     d_sn = sn
#
#
# def check_the_info_ack(ack):
#     print("start the check_info function--" + "ack" * 10)
#     print("ack : ", ack)
#     d_ack = ack
#
# def check_the_info_rn(rn):
#     print("start the check_info function--" + "rn" * 10)
#     print("ack : ", rn)
#     d_rn = rn

class Ui_MainWindow(object):

    def __init__(self):
        self.goback = GoBack(4, [self.test_sf, self.test_sn, self.package_rn, None])

        self.u_sf = None
        self.u_sn = None
        self.u_ack = None
        self.u_rn = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 40, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 100, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 60, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gobackn = self.gobackn_thread_start
        # 批量添加属性
        for i in range(1, 33):
            setattr(self, "label_{}".format(str(i)), QtWidgets.QLabel(self.centralwidget))

        x = 90
        y = 90
        # 批量设置属性
        for i in range(1, 33):
            label = getattr(self, "label_{}".format(str(i)))
            _translate = QtCore.QCoreApplication.translate
            label.setText(_translate("MainWindow", "{}".format(str(i))))
            if i <= 16:
                label.setText(_translate("MainWindow", "{}".format(str(i))))
                label.setGeometry(QtCore.QRect(x, 250, 16, 16))
                x+=40

            if i>16:
                label.setText(_translate("MainWindow", "{}".format(str(i-16))))
                label.setGeometry(QtCore.QRect(y, 310, 16, 16))
                y+=40

        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(10, 250, 59, 16))
        self.label_44.setText("Sender :")
        self.label_55 = QtWidgets.QLabel(self.centralwidget)
        self.label_55.setGeometry(QtCore.QRect(10, 310, 59, 16))
        self.label_55.setText("Receiver :")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 390, 256, 131))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(400, 390, 301, 131))
        self.textBrowser_2.setObjectName("textBrowser_2")



        #
        # for label in list:
        #     print(type(list[label]))
            # list[label].
        # self.list[i].setOnjectName("label_{}".format(str(i)))




        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        #
        # self.Sender = ARQ_sender.Sender_start
        # self.Receiver = ARQ_receiver.Receiver_start

        # self.pushButton.clicked.connect(self.start_sender_receiver)
        # self.pushButton.clicked.connect(self.start_change)
        # self.pushButton.clicked.connect(self.show_sender_info)

        self.pushButton_2.clicked.connect(self.start_gobackn)
        # self.pushButton_2.clicked.connect(self.show_sender_info)
        # self.pushButton_2.clicked.connect(self.show_receive_info)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ARQ"))
        self.pushButton_2.setText(_translate("MainWindow", "GO_BACK_N"))
        self.pushButton_3.setText(_translate("MainWindow", "STOP"))

    # def gobackn_thread(self):
    #     self.gobackn.sendProcess()
    #     self.gobackn.recvProcess()

    def start_gobackn(self):

        thread1 = threading.Thread(target=self.gobackn)
        thread1.start()

        # thread2 = threading.Thread(target=self.check_the_info)
        # thread2.start()
        # self.check_the_info()

        # 线程1  : goback n
        # self.gobackn()
        # 两个线程之间不能互相访问




    # def start_sender_receiver(self):
    #     pass
    #     # thread_sender = threading.Thread(target=self.Sender)
    #     # thread_receiver  = threading.Thread(target=self.Receiver)
    #     #
    #     #
    #     # thread_receiver.start()
    #     # thread_sender.start()


    # def start_change_color(self):
    #     self.changeColor(1, 15)


    # 改变 (start -> end)的label的颜色
    def changeColor(self, start_n, end_n):

        palette1 = QPalette()
        palette2 = QPalette()
        # palette1.setColor(QPalette.WindowText, QColor(192, 253, 123))

        # 设为绿色
        palette1.setColor(QPalette.Background, QColor(192, 253, 123))

        # 设为无色
        palette2.setColor(QPalette.Background, QColor(237, 237, 237))

        list = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6,
                self.label_7,self.label_8, self.label_9, self.label_10, self.label_11, self.label_12,
                self.label_13, self.label_14, self.label_15, self.label_16]

        a = start_n
        b = end_n
        if a != None and a>0:
            for i in range(start_n):
                list[i+1].setAutoFillBackground(True)
                list[i+1].setPalette(palette2)
        if a != None and b != None and b-a+1>0:
            for i in range(b-a+1):
                list[a+i-1].setAutoFillBackground(True)
                list[a + i - 1].setPalette(palette1)

    def changeColor_2(self, start_n, end_n):
        palette1 = QPalette()
        palette2 = QPalette()
        # 设为绿色
        palette1.setColor(QPalette.Background, QColor(192, 253, 123))
        # 设为无色
        palette2.setColor(QPalette.Background, QColor(237, 237, 237))

        list = [self.label_17, self.label_18, self.label_19, self.label_20, self.label_21,
                self.label_22, self.label_23, self.label_24, self.label_25, self.label_26,
                self.label_27, self.label_28, self.label_29, self.label_30, self.label_31,
                self.label_32]

        a = start_n
        b = end_n
        if a != None and a > 0:
            for i in range(start_n):
                list[i + 1].setAutoFillBackground(True)
                list[i + 1].setPalette(palette2)
        if b - a + 1 > 0:
            for i in range(b - a + 1):
                list[a + i - 1].setAutoFillBackground(True)
                list[a + i - 1].setPalette(palette1)

    def changeColor_loss(self, start_n,):
        pass



    def package_rn(self, item):
        print("rn"*10, end="")
        print(":", item)

        self.textBrowser.append("loss happened")

        # self.textBrowser.moveCursor(QTextCursor.End)

    def package_ack(self,item):
        print("ack"*10+item)

        self.textBrowser_2.append("receiver :"+item)

    # def test1(self, item):
        # self.textBrowser.clear()


        # self.textBrowser.append(str(item))



    def test_sf(self, item, sf_str):
        print("sf"*10, end="")
        print(": ", item)
        self.u_sf = item
        self.textBrowser_2.append(sf_str)
        tt = 0
        if tt > 0:
            self.textBrowser_2.moveCursor(QtGui.QTextCursor.End)
        tt += 1


        # self.changeColor(self.u_sf, self.u_sn)
        # self.changeColor_2(self.u_sf, self.u_sn)

    def test_sn(self, item, sn_str):
        print("sn"*10, end="")
        print(": ", item)
        self.u_sn = item

        self.textBrowser.append(sn_str)

        tt = 0
        if tt > 0:
            self.textBrowser_2.moveCursor(QtGui.QTextCursor.End)
        tt += 1

        self.changeColor(self.u_sf, self.u_sn)
        self.changeColor_2(self.u_sf, self.u_sn)

        # self.changeColor(sn,)

    def gobackn_thread_start(self):

        print("start go back n protocol")
        self.goback.sendProcess()
        self.goback.recvProcess()

        # def






def main():
    goback = GoBack(4, [None, None, None, None])
    goback.sendProcess()
    goback.recvProcess()


def gobackn_thread_start():
    print("start go back n protocol")
    main()
