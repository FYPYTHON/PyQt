#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial

In this example, we position two push
buttons in the bottom-right corner
of the window.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys
from PyQt5 import QtGui

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import (QWidget, QPushButton, QDesktopWidget,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QMainWindow, QAction, qApp,
                             QLCDNumber, QSlider, QInputDialog, QFrame, QColorDialog, QSizePolicy, QFontDialog,
                             QCheckBox, QCalendarWidget, QComboBox)
from PyQt5.QtWidgets import QGridLayout


class Example(QMainWindow):
    def __init__(self):
        super(Example,self).__init__()

        # self.initUI()
        self.ui = QWidget()
        self.contral_ui = QWidget()
        self.draw_ui = QWidget()
        self.setCentralWidget(self.ui)
        self.initUI()


    def initUI(self):
        self.setWindowTitle('MainWindow Calculator')
        # 菜单初始化
        self.initMenu()
        # 布局初始化
        self.initLayout()
        # self.resize(800,600)
        self.show()

    def initMenu(self):

        exitAction = QAction(QIcon('img/exit.jpg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        exitAction1 = QAction(QIcon('img/exit.jpg'), '&Exit', self)
        exitAction1.setShortcut('Ctrl+Q')
        exitAction1.setStatusTip('Exit application')
        exitAction1.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&File')
        exitMenu = menubar.addMenu('&Exit')
        # 添加事件
        fileMenu.addAction(exitAction)
        fileMenu.addSeparator()          # 增加分割线
        fileMenu.addAction(exitAction1)
        exitMenu.addAction(exitAction)


    def initLayout(self):

        print "init layout..."
        vbox = QVBoxLayout(self.ui)
        hbox = QHBoxLayout(self.ui)
        namelable = QLabel("计算器")
        desclable = QLabel("布局")
        lineedit = QLineEdit("输入")
        hbox.addStretch(1)
        hbox.addWidget(namelable)
        hbox.addStretch(1)
        hbox.addWidget(desclable)
        hbox.addStretch(1)
        hbox.addWidget(lineedit)

        grid = QGridLayout()

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        # 确认 取消按钮
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # 绑定事件
        okButton.clicked.connect(self.buttonClicked)
        cancelButton.clicked.connect(self.buttonClicked)

        grid.addWidget(okButton, 5, 0, 1, 2)
        grid.addWidget(cancelButton, 5, 2, 1, 2)

        # 液晶显示屏
        lcdgrid = QGridLayout()
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        lcdgrid.addWidget(lcd,1,2,20,1)
        lcdgrid.addWidget(sld,21,2,10,1)
        sld.valueChanged.connect(lcd.display)

        vbox.addLayout(hbox, 1)
        vbox.addSpacing(1)
        vbox.addLayout(grid, 1)
        vbox.addStretch(1)
        vbox.addLayout(lcdgrid)


        self.ui.setLayout(vbox)
        self.move(300, 150)

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        self.initContralUI()

        self.contral_ui.show()

    def initContralUI(self):
        # 对话框
        self.contral_ui.btn = QPushButton('Open Dialog', self.contral_ui)
        self.contral_ui.btn.move(20, 20)
        self.contral_ui.btn.clicked.connect(self.showDialog)

        self.contral_ui.le = QLineEdit(self.contral_ui)
        self.contral_ui.le.move(130, 22)
        size = self.geometry()
        x = size.x()
        y = size.y()
        w = size.width()
        h = size.height()
        self.contral_ui.setGeometry(x+w+1,y,w,h)

        # 颜色框
        col = QColor(0, 0, 0)

        self.contral_ui.color_btn = QPushButton('Color Dialog', self.contral_ui)
        self.contral_ui.color_btn.move(20, 60)

        self.contral_ui.color_btn.clicked.connect(self.showColorDialog)

        self.contral_ui.frm = QFrame(self.contral_ui)
        self.contral_ui.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.contral_ui.frm.setGeometry(130, 60, 100, 20)

        # 字体框
        self.contral_ui.font_btn = QPushButton('Font Dialog', self.contral_ui)
        self.contral_ui.font_btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)
        self.contral_ui.font_btn.move(20, 100)

        self.contral_ui.font_btn.clicked.connect(self.showFontDialog)
        self.contral_ui.lbl = QLabel('Knowledge only matters', self.contral_ui)
        self.contral_ui.lbl.move(130, 105)

        # checkbox
        cb = QCheckBox('Show title', self.contral_ui)
        cb.move(20, 150)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        # 日历控件
        self.contral_ui.cal = QCalendarWidget(self.contral_ui)
        self.contral_ui.cal.setGridVisible(True)
        self.contral_ui.cal.move(20, 170)
        self.contral_ui.cal.clicked[QDate].connect(self.showDate)

        self.contral_ui.date_lbl = QLabel(self.contral_ui)
        date = self.contral_ui.cal.selectedDate()
        self.contral_ui.date_lbl.setText(date.toString())
        self.contral_ui.date_lbl.move(130, 380)

        # 下拉框
        self.contral_ui.combo = QComboBox(self.contral_ui)
        self.contral_ui.combo.addItem("Ubuntu")
        self.contral_ui.combo.addItem("Mandriva")
        self.contral_ui.combo.addItem("Fedora")
        self.contral_ui.combo.addItem("Arch")
        self.contral_ui.combo.addItem("Gentoo")
        self.contral_ui.combo.move(50, 400)
        self.contral_ui.combo.activated[str].connect(self.onActivated)

        self.combo_lbl = QLabel("Ubuntu", self.contral_ui)
        self.combo_lbl.move(20,425)
        # self.combo_lbl.setFixedSize()

        # self.contral_ui.resize(600,500)
        self.contral_ui.setWindowTitle('Contral Widget')

    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        if ok:
            self.contral_ui.le.setText(str(text))

    def showColorDialog(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.contral_ui.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())

    def showFontDialog(self):

        font, ok = QFontDialog.getFont()
        if ok:
            self.contral_ui.lbl.setFont(font)

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.contral_ui.setWindowTitle('QCheckBox')
        else:
            self.contral_ui.setWindowTitle('')

    def showDate(self, date):
        self.contral_ui.date_lbl.setText(date.toString())

    def onActivated(self, text):
        #
        print text
        print self.sender()
        print self.sender().currentIndex()
        text = text + " index:"+str(self.sender().currentIndex())
        self.combo_lbl.setText(text)
        print self.combo_lbl.size()
        self.combo_lbl.resize(200,20)

    def keyPressEvent(self, e):
        print "key press event:%s" % e.key()
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Space:
            h = QDesktopWidget().screenGeometry().width()
            w = QDesktopWidget().screenGeometry().height()
            size = self.geometry()  # 同上
            print size
            print self.x(),self.y()
            if self.x() < h and self.y() < w:
                self.move(self.x()+5,self.y()+1)
                # self.contral_ui.move(self.contral_ui.x()+5,self.contral_ui.y()+1)

    def mousePressEvent(self, e):

        if e.button() == Qt.LeftButton:
            print('mouse left press')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())