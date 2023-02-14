from PyQt5 import QtWidgets
from mainUI import Ui_MainWindow
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton
from PyQt5.QtCore import QTimer, QDateTime
# 确保Windows系统下任务栏图标正常
try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.iniVariable()
        self.iniUI()
        self.iniConfigFunction()
        self.iniThread()
        self.connectFunction()

    def iniVariable(self):
        self.baseDir = os.path.dirname(__file__)
        pass

    def iniUI(self):
        self.setWindowTitle('TITLE')
        self.setWindowIcon(
            QIcon(os.path.join(self.baseDir, "icon", "A.ico")))
        self.setGeometry(150, 150, 1550, 800)
        self.statusShowTime()
        pass

    def iniConfigFunction(self):
        pass

    def iniThread(self):
        pass

    def connectFunction(self):
        self.pushButtonTEST.clicked.connect(self.TEST)
        # 关于
        self.actionAboutQT.triggered.connect(self.aboutQT_FUNCTION)
        pass
# 背景函数

    def statusShowTime(self):
        '''显示当前时间'''
        self.timer = QTimer()
        self.timeLabel = QLabel()
        self.statusBar.addPermanentWidget(self.timeLabel, 1)
        self.timer.timeout.connect(lambda: self.showCurrentTime(
            self.timeLabel))
        self.timer.start(500)
        self.info = QLabel()
        self.info.setText('-Code by RIAMB-')
        self.statusBar.addPermanentWidget(self.info, 0)

    def showCurrentTime(self, timeLabel):
        '''获取当前时间'''
        # import time
        # time.sleep(5)
        currentTime = QDateTime.currentDateTime()
        self.timeDisplay = currentTime.toString('yyyy-MM-dd hh:mm:ss dddd')
        timeLabel.setText(self.timeDisplay)

    def aboutQT_FUNCTION(self):
        QMessageBox.aboutQt(self, 'QT')
# 功能函数

    def TEST(self):
        self.textEdit.append('test message ~')
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
