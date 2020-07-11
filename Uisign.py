from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import wavbox
import VideoRecognition
import output
import cv2
from datetime import datetime

s=""
j=1
name02=""
name03=""
class Stats:
    def __init__(self):
        #加载designer设计的ui文件
        super().__init__()
        self.ui = QUiLoader().load('SYSui.ui')
        self.ui.setWindowFlags(Qt.FramelessWindowHint)
        #按钮槽
        self.ui.btn_sign.clicked.connect(self.on_btn_sign_clicked)#1
        self.ui.btn_back.clicked.connect(self.on_btn_back_clicked)#2
        self.ui.btn_close.clicked.connect(self.on_btn_close_clicked)#3
        self.ui.btn_maxsize.clicked.connect(self.on_btn_maxsize_clicked)#4
        self.ui.btn_minisize.clicked.connect(self.on_btn_minisize_clicked)#5
        self.ui.btn_open.clicked.connect(self.on_btn_open_clicked)#6
        self.ui.btn_sure.clicked.connect(self.on_btn_sure_clicked)  #7

    def on_btn_sign_clicked(self):#1
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_btn_back_clicked(self):#2
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.Videoshow.setText("")
        QApplication.processEvents()
        global j
        j=1
        for i in range(0, 4):
            if i == 0:
                item = QTableWidgetItem()
                item.setText("")
                self.ui.tableWidget.setItem(j, 0, item)
            if i == 1:
                item = QTableWidgetItem()
                item.setText("")
                self.ui.tableWidget.setItem(j, 1, item)
            if i == 2:
                item = QTableWidgetItem()
                item.setText("")
                self.ui.tableWidget.setItem(j, 2, item)
            if i == 3:
                item = QTableWidgetItem()
                item.setText("")
                self.ui.tableWidget.setItem(j, 3, item)

    def on_btn_close_clicked(self):#3
        sys.exit(app.exec_())

    def on_btn_maxsize_clicked(self):#4
        if(self.ui.isMaximized()==True):
            self.ui.setWindowState(Qt.WindowNoState)
        else:
            self.ui.setWindowState(Qt.WindowMaximized)

    def on_btn_minisize_clicked(self):#5
        self.ui.setWindowState(Qt.WindowMinimized)

    def on_btn_open_clicked(self):#6
        self.ui.Videoshow.setText("开始录音")
        QApplication.processEvents()
        name = wavbox.wavrec()
        self.ui.Videoshow.setText("语音识别:\n" + name)
        QApplication.processEvents()
        if name != None:
            name01 = VideoRecognition.videorec()
        self.ui.Videoshow.setText("语音识别:\n"+name+'\n'+"人脸识别:\n"+name01)
        global name03
        global name02
        name02=name
        name03=name01
        dt=datetime.now()
        global s
        s=str(dt.year)+"."+str(dt.month)+"."+str(dt.day)+" "+str(dt.hour)+":"+str(dt.minute)+":"+str(dt.second)


    def on_btn_sure_clicked(self):#7
        global j
        if name02==name03!="":
            recognition_result = [{'Name': name02, 'Recognition_status': 'Success'}]
            output.output().PushResult(recognition_result)
            for i in range(0,4):
                if i==0:
                    item = QTableWidgetItem()
                    item.setText(name02)
                    self.ui.tableWidget.setItem(j,0, item)
                if i==1:
                    item = QTableWidgetItem()
                    item.setText("计算机科学与技术")
                    self.ui.tableWidget.setItem(j,1, item)
                if i==2:
                    item = QTableWidgetItem()
                    item.setText("17级")
                    self.ui.tableWidget.setItem(j,2, item)
                if i==3:
                    item = QTableWidgetItem()
                    item.setText(s)
                    self.ui.tableWidget.setItem(j, 3, item)
            j=j+1
            self.ui.Videoshow.setText("")
            QApplication.processEvents()
        else:
                dialog = QDialog()
                label = QLabel('不是同一个人', dialog)


                label.move(50, 50)
                dialog.setWindowTitle('别想蒙混过关')
                dialog.setWindowModality(Qt.ApplicationModal)
                dialog.exec()  # 显示对话框

if __name__ == "__main__":
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()