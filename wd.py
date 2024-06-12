from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import pandas as pd
from Recognizer import Recognizer
recognizer = Recognizer('./model/chinese-45.keras', './model/chinese-features-45.npy')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.filename='???'
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagelabel = QtWidgets.QLabel(self.centralwidget)
        self.imagelabel.setGeometry(QtCore.QRect(70, 20, 681, 401))
        self.imagelabel.setText("")
        self.imagelabel.setPixmap(QtGui.QPixmap("sadasd.jpg"))
        self.imagelabel.setObjectName("imagelabel")
        self.imagelabel.setScaledContents(True)
        self.input_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.input_line_edit.setGeometry(QtCore.QRect(70, 430, 271, 31))
        self.input_line_edit.setObjectName("input_line_edit")
        self.input_line_edit.returnPressed.connect(self.getname)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_line_edit.setFont(font)
        font.setBold(True)
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(480, 430, 211, 31))
        self.result.setObjectName("result")
        self.result.setFont(font)
        self.shibie = QtWidgets.QPushButton(self.centralwidget)
        self.shibie.setGeometry(QtCore.QRect(480, 530, 171, 61))
        self.shibie.setObjectName("shibie")
        self.shibie.clicked.connect(self.beginshibie)
        
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(70, 530, 171, 61))
        self.Button.setObjectName("Button")
        self.Button.clicked.connect(self.msg)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 490, 71, 21))
        self.label_2.setObjectName("label_2")
        self.xuanzhongwenjian = QtWidgets.QLabel(self.centralwidget)
        self.xuanzhongwenjian.setGeometry(QtCore.QRect(80, 480, 350, 41))
        self.xuanzhongwenjian.setToolTipDuration(-1)
        self.xuanzhongwenjian.setText("")
        self.xuanzhongwenjian.setObjectName("xuanzhongwenjian")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)




        self.shibie.setStyleSheet("background-color:rgb(111,180,219)")
        self.shibie.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}")  # 按下时的样式
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Button.setStyleSheet("background-color:rgb(111,180,219)")
        self.Button.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}")  # 按下时的样式
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "汉字识别"))
        self.result.setText(_translate("MainWindow", "结果显示"))
        self.shibie.setText(_translate("MainWindow", "识别"))
        self.Button.setText(_translate("MainWindow", "选择文件"))
        self.label_2.setText(_translate("MainWindow", "当前选中："))

    def msg(self):
        self.imagelabel.setGeometry(QtCore.QRect(220, 20, 401, 401))
        self.filename,_=QtWidgets.QFileDialog.getOpenFileName(None,"选取文件","/","JPEG文件 (*.jpg *.jpeg)")
        self.xuanzhongwenjian.setText(self.filename)
        self.imagelabel.setPixmap(QtGui.QPixmap(self.filename))


    def getname(self):
        self.imagelabel.setGeometry(QtCore.QRect(220, 20, 401, 401))
        self.filename = self.input_line_edit.text()
        print(str(self.filename))
        # result=recognizer.recognize_image('./image/'+filename+'.jpg')
        self.input_line_edit.clear()
        

    
    def beginshibie(self):
        if os.path.exists(self.filename):
            print(self.filename,'1')
            self.begin(self.filename)
        elif os.path.exists('./image/'+self.filename+'.jpg'):
            self.xuanzhongwenjian.setText(self.filename+'.jpg')
            self.filename='./image/'+self.filename+'.jpg'
            #调用识别函数
            print(self.filename)
            self.begin(self.filename)
        else:
            self.xuanzhongwenjian.setText('无效文件')


    def begin(self, filename):
        print(filename,'2')
        result=recognizer.recognize_image(filename)

        self.result.setText(result)

        




if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(mainWindow)

    mainWindow.show()

    sys.exit(app.exec_())
