# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'run_gallery_tv_s.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_play_1 = QPushButton(self.centralwidget)
        self.pushButton_play_1.setObjectName(u"pushButton_play_1")
        self.pushButton_play_1.setGeometry(QRect(500, 540, 180, 35))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(24)
        font.setBold(True)
        self.pushButton_play_1.setFont(font)
        self.pushButton_play_1.setFlat(True)
        self.pushButton_play_2 = QPushButton(self.centralwidget)
        self.pushButton_play_2.setObjectName(u"pushButton_play_2")
        self.pushButton_play_2.setGeometry(QRect(740, 540, 180, 35))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.pushButton_play_2.setFont(font1)
        self.pushButton_play_2.setFlat(True)
        self.pushButton_play_3 = QPushButton(self.centralwidget)
        self.pushButton_play_3.setObjectName(u"pushButton_play_3")
        self.pushButton_play_3.setGeometry(QRect(990, 540, 180, 35))
        font2 = QFont()
        font2.setPointSize(24)
        self.pushButton_play_3.setFont(font2)
        self.pushButton_play_3.setFlat(True)
        self.pushButton_play_4 = QPushButton(self.centralwidget)
        self.pushButton_play_4.setObjectName(u"pushButton_play_4")
        self.pushButton_play_4.setGeometry(QRect(1240, 540, 180, 35))
        self.pushButton_play_4.setFlat(True)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 1920, 1080))
        MainWindow.setCentralWidget(self.centralwidget)
        self.graphicsView.raise_()
        self.pushButton_play_1.raise_()
        self.pushButton_play_2.raise_()
        self.pushButton_play_3.raise_()
        self.pushButton_play_4.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Video Presentation", None))
        self.pushButton_play_1.setText("")
        self.pushButton_play_2.setText("")
        self.pushButton_play_3.setText("")
        self.pushButton_play_4.setText("")
    # retranslateUi

