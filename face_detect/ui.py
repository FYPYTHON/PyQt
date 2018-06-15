# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(683, 417)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 70, 81, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 110, 181, 151))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_6 = QPushButton(Dialog)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6,3, 0, 1, 1)

        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 310, 81, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))


        self.lcdNumber = QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 360, 64, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("新宋体"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.retranslateUi(Dialog)
        # QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        self.pushButton_5.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Client", None))
        self.pushButton.setText(_translate("Dialog", "功能选择", None))
        self.pushButton_3.setText(_translate("Dialog", "Face Detection", None))
        self.pushButton_2.setText(_translate("Dialog", "Show Picture", None))
        self.pushButton_4.setText(_translate("Dialog", "Eye Detetction", None))
        self.pushButton_5.setText(_translate("Dialog", "退出", None))
        self.pushButton_6.setText(_translate("Dialog", "Animation Effect", None))
