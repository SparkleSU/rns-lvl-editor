# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'level_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 350)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.369318 rgba(18, 22, 22, 255), stop:0.880682 rgba(45, 46, 43, 255));\n"
"font-family: Hack Nerd Font;\n"
"color: white;")
        self.menuSelect = QAction(MainWindow)
        self.menuSelect.setObjectName(u"menuSelect")
        self.menuSave = QAction(MainWindow)
        self.menuSave.setObjectName(u"menuSave")
        self.menuExit = QAction(MainWindow)
        self.menuExit.setObjectName(u"menuExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelMain = QLabel(self.centralwidget)
        self.labelMain.setObjectName(u"labelMain")
        self.labelMain.setGeometry(QRect(0, 0, 550, 81))
        font = QFont()
        font.setFamilies([u"Hack Nerd Font"])
        font.setBold(True)
        self.labelMain.setFont(font)
        self.labelMain.setStyleSheet(u"background-color: rgb(63, 61, 48);\n"
"color: white")
        self.labelMain.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.playMain = QSlider(self.centralwidget)
        self.playMain.setObjectName(u"playMain")
        self.playMain.setGeometry(QRect(0, 130, 551, 22))
        self.playMain.setStyleSheet(u"QSlider::groove:horizontal\n"
"{\n"
"	height:10px;\n"
"	width:480px;\n"
"	background: white;\n"
"	border-radius:5px;\n"
"}\n"
"QSlider::handle:horizontal\n"
"{\n"
"	width: 11px;\n"
"	height: 20px;\n"
"	background: rgb(255, 252, 155); \n"
"	margin: -7px -7px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider\n"
"{\n"
"	background: none;\n"
"}")
        self.playMain.setOrientation(Qt.Orientation.Horizontal)
        self.currentTime = QLabel(self.centralwidget)
        self.currentTime.setObjectName(u"currentTime")
        self.currentTime.setGeometry(QRect(30, 100, 71, 16))
        self.currentTime.setStyleSheet(u"background-color: none;\n"
"color: white")
        self.maxTime = QLabel(self.centralwidget)
        self.maxTime.setObjectName(u"maxTime")
        self.maxTime.setGeometry(QRect(450, 100, 71, 16))
        self.maxTime.setStyleSheet(u"background-color: none;\n"
"color: white")
        self.r1Action = QLabel(self.centralwidget)
        self.r1Action.setObjectName(u"r1Action")
        self.r1Action.setGeometry(QRect(30, 170, 30, 30))
        font1 = QFont()
        font1.setFamilies([u"Hack Nerd Font"])
        font1.setPointSize(12)
        self.r1Action.setFont(font1)
        self.r1Action.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 252, 155);\n"
"color: black;")
        self.r1Action.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.r2Action = QLabel(self.centralwidget)
        self.r2Action.setObjectName(u"r2Action")
        self.r2Action.setGeometry(QRect(70, 170, 30, 30))
        self.r2Action.setFont(font1)
        self.r2Action.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 252, 155);\n"
"color: black;")
        self.r2Action.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.r3Action = QLabel(self.centralwidget)
        self.r3Action.setObjectName(u"r3Action")
        self.r3Action.setGeometry(QRect(110, 170, 30, 30))
        self.r3Action.setFont(font1)
        self.r3Action.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 252, 155);\n"
"color: black;")
        self.r3Action.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.r1Button = QPushButton(self.centralwidget)
        self.r1Button.setObjectName(u"r1Button")
        self.r1Button.setGeometry(QRect(30, 210, 30, 30))
        self.r1Button.setFont(font)
        self.r1Button.setStyleSheet(u"border: none;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 252, 155);\n"
"color: black;")
        self.r2Button = QPushButton(self.centralwidget)
        self.r2Button.setObjectName(u"r2Button")
        self.r2Button.setGeometry(QRect(70, 210, 30, 30))
        self.r2Button.setFont(font)
        self.r2Button.setStyleSheet(u"border: none;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 252, 155);\n"
"color: black;")
        self.r3Button = QPushButton(self.centralwidget)
        self.r3Button.setObjectName(u"r3Button")
        self.r3Button.setGeometry(QRect(110, 210, 30, 30))
        self.r3Button.setFont(font)
        self.r3Button.setStyleSheet(u"border: none;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 252, 155);\n"
"color: black;")
        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(190, 170, 50, 50))
        self.resetButton.setStyleSheet(u"border: none;\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 252, 155);\n"
"color: black;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/stop_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resetButton.setIcon(icon)
        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setGeometry(QRect(250, 170, 50, 50))
        self.playButton.setStyleSheet(u"border: none;\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 252, 155);\n"
"color: black;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/play_arrow_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon1)
        self.pauseButton = QPushButton(self.centralwidget)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setGeometry(QRect(310, 170, 50, 50))
        self.pauseButton.setStyleSheet(u"border: none;\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 252, 155);\n"
"color: black;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/pause_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.playSound = QSlider(self.centralwidget)
        self.playSound.setObjectName(u"playSound")
        self.playSound.setGeometry(QRect(80, 260, 441, 51))
        self.playSound.setStyleSheet(u"QSlider::groove:horizontal\n"
"{\n"
"	height:10px;\n"
"	width:370px;\n"
"	background: white;\n"
"	border-radius:5px;\n"
"}\n"
"QSlider::handle:horizontal\n"
"{\n"
"	width: 11px;\n"
"	height: 20px;\n"
"	background: rgb(255, 252, 155); \n"
"	margin: -7px -7px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider\n"
"{\n"
"	background: none\n"
"}")
        self.playSound.setOrientation(Qt.Orientation.Horizontal)
        self.soundButton = QPushButton(self.centralwidget)
        self.soundButton.setObjectName(u"soundButton")
        self.soundButton.setGeometry(QRect(30, 260, 50, 50))
        self.soundButton.setStyleSheet(u"border: none;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 252, 155);\n"
"color: black;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/volume_up_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.soundButton.setIcon(icon3)
        self.soundButton.setIconSize(QSize(16, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.menuSelect)
        self.menuFile.addAction(self.menuSave)
        self.menuFile.addAction(self.menuExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Level Editor - R&S", None))
        self.menuSelect.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.menuSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.labelMain.setText(QCoreApplication.translate("MainWindow", u"Please select .wav track", None))
        self.currentTime.setText(QCoreApplication.translate("MainWindow", u"00:00.000", None))
        self.maxTime.setText(QCoreApplication.translate("MainWindow", u"00:00.000", None))
        self.r1Action.setText("")
        self.r2Action.setText("")
        self.r3Action.setText("")
        self.r1Button.setText(QCoreApplication.translate("MainWindow", u"r1", None))
        self.r2Button.setText(QCoreApplication.translate("MainWindow", u"r2", None))
        self.r3Button.setText(QCoreApplication.translate("MainWindow", u"r3", None))
        self.resetButton.setText("")
        self.playButton.setText("")
        self.pauseButton.setText("")
        self.soundButton.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

