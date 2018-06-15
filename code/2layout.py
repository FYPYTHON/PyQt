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
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit)
from PyQt5.QtWidgets import QGridLayout


class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()

        # self.initUI()
        self.initUI()

    def initUI(self):
        # 菜单初始化
        self.initMenu()
        # 布局初始化
        self.initLayout()
        self.show()

    def initMenu(self):
        # self.statusBar().showMessage('Ready')
        pass

    def initLayout(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
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

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        grid.addWidget(okButton, 5, 0, 1, 2)
        grid.addWidget(cancelButton, 5, 2, 1, 2)

        vbox.addLayout(hbox, 1)
        vbox.addSpacing(1)
        vbox.addLayout(grid, 1)

        self.setLayout(vbox)
        self.move(300, 150)
        self.setWindowTitle('Calculator')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())