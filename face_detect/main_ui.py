# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QDialog,QApplication

from open_image import *
from facd_detect import *
from eye_detect import *
from animation_effect import animation
from ui import *
import sys
TIEMOUT = 30
class MyClient(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.img_widget = QWidget()
        self.number = 1
        self._timeout = QtCore.QTimer(self)
        self._timeout.timeout.connect(self._animation)
        _timer = QtCore.QTimer(self)
        _timer.timeout.connect(self._showtime)
        _timer.start()
        self._showtime()

        self.ui.pushButton_2.clicked.connect(self._showpicture)
        self.ui.pushButton_3.clicked.connect(self._facedetect)
        self.ui.pushButton_4.clicked.connect(self._eyedetect)
        self.ui.pushButton_6.clicked.connect(self._timetook)

    def _showtime(self):
        _time = QtCore.QTime.currentTime()
        _text = _time.toString("hh:mm")
        self.ui.lcdNumber.display(_text)

    def _showpicture(self):
        showPicture()

    def _facedetect(self):

        facd_detect()


    def _eyedetect(self):
        eydDetect()

    def paintEvent(self, QPaintEvent):
        pass

    def _timetook(self):
        self.img_widget.label = QLabel(self.img_widget)
        self.img_widget.label.resize(454,286)
        self.img_widget.resize(454,286)
        self.img_widget.show()
        self._timeout.start(TIEMOUT)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Space:
            self._timeout.start(TIEMOUT)
        if e.key() == QtCore.Qt.Key_Escape:
            self.img_widget.close()
            self._timeout.stop()


    def _animation(self):

        try:

            if (self.number > 99):
                self.number = 1
                # self.img_widget.close()
                self._timeout.stop()

            # show = animation(self.number)
            print self.number
            # showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            # showImage = QImage(show.data,QImage.Format_RGB888)
            filename_temp = './img/bmp/%d.bmp' % self.number
            showImage = QImage(filename_temp)

            self.img_widget.label.setPixmap(QPixmap.fromImage(showImage))
            QApplication.processEvents()
            self.number += 1
        except Exception as e:
            print e




if __name__ == '__main__':
    app = QApplication(sys.argv)
    my = MyClient()
    my.show()
    sys.exit(app.exec_())