#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
py40 PyQt5 tutorial

This example shows an icon
in the titlebar of the window.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QToolTip


class Example(QWidget):
    def __init__(self,):
        super(Example,self).__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('PyQt')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('web.jpg'))
        # 居中显示
        self.center()
        # PyQt 按钮
        self.initButton()
        # 显示窗口
        self.resize(400,400)
        self.show()

    def initButton(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('Button Tips', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())

        # 移动窗口的位置
        btn.move(50, 50)

        # 退出按钮
        qbtn = QPushButton('Quit', self)
        # qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.clicked.connect(sys.exit)
        qbtn.resize(qbtn.sizeHint())
        print btn.size().width(),btn.size().height()
        qbtn.move(50 + btn.size().width(), 50)

        # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())