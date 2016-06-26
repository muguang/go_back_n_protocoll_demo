from demo_ui4 import QApplication, QMainWindow, Ui_MainWindow, QThread
import sys
from demo_ui4 import *
# from GoBack5 import *
# import GoBack5


# from demo_ui4 import gobackn_thread_start
#
# class go_back_thread(QThread):
#     def __init__(self):
#         super(go_back_thread, self.__init__())
#
#     def run(self):
#         # gobackn_thread_start()
#         gobackn_thread_start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
