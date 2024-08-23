# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Qt_designerbasSTJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1133, 890)
        MainWindow.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.VOLTAGE1_IN = QLCDNumber(self.centralwidget)
        self.VOLTAGE1_IN.setObjectName(u"VOLTAGE1_IN")
        self.VOLTAGE1_IN.setGeometry(QRect(350, 80, 91, 81))
        self.VOLTAGE_2 = QLCDNumber(self.centralwidget)
        self.VOLTAGE_2.setObjectName(u"VOLTAGE_2")
        self.VOLTAGE_2.setGeometry(QRect(350, 190, 91, 81))
        self.VOLTAGE3_IN = QLCDNumber(self.centralwidget)
        self.VOLTAGE3_IN.setObjectName(u"VOLTAGE3_IN")
        self.VOLTAGE3_IN.setGeometry(QRect(350, 300, 91, 81))
        self.VOLTAGE4_IN = QLCDNumber(self.centralwidget)
        self.VOLTAGE4_IN.setObjectName(u"VOLTAGE4_IN")
        self.VOLTAGE4_IN.setGeometry(QRect(760, 80, 91, 81))
        self.VOLTAGE5_IN = QLCDNumber(self.centralwidget)
        self.VOLTAGE5_IN.setObjectName(u"VOLTAGE5_IN")
        self.VOLTAGE5_IN.setGeometry(QRect(760, 190, 91, 81))
        self.VOLTAGE6_IN = QLCDNumber(self.centralwidget)
        self.VOLTAGE6_IN.setObjectName(u"VOLTAGE6_IN")
        self.VOLTAGE6_IN.setGeometry(QRect(760, 300, 91, 81))
        self.Display1 = QGraphicsView(self.centralwidget)
        self.Display1.setObjectName(u"Display1")
        self.Display1.setGeometry(QRect(500, 500, 61, 51))
        self.Display1.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 170, 0);")
        self.Display1_5 = QGraphicsView(self.centralwidget)
        self.Display1_5.setObjectName(u"Display1_5")
        self.Display1_5.setGeometry(QRect(600, 580, 61, 51))
        self.Display1_5.setStyleSheet(u"\n"
"background-color:rgb(255, 0, 0);\n"
"background-color: rgb(0, 170, 0)")
        self.Display1_2 = QGraphicsView(self.centralwidget)
        self.Display1_2.setObjectName(u"Display1_2")
        self.Display1_2.setGeometry(QRect(500, 580, 61, 51))
        self.Display1_2.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 170, 0);")
        self.Display1_3 = QGraphicsView(self.centralwidget)
        self.Display1_3.setObjectName(u"Display1_3")
        self.Display1_3.setGeometry(QRect(500, 670, 61, 51))
        self.Display1_3.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 170, 0);")
        self.Display1_4 = QGraphicsView(self.centralwidget)
        self.Display1_4.setObjectName(u"Display1_4")
        self.Display1_4.setGeometry(QRect(600, 500, 61, 51))
        self.Display1_4.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 170, 0);")
        self.Display1_6 = QGraphicsView(self.centralwidget)
        self.Display1_6.setObjectName(u"Display1_6")
        self.Display1_6.setGeometry(QRect(600, 670, 61, 51))
        self.Display1_6.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 170, 0);")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(370, 510, 91, 31))
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(370, 590, 91, 31))
        self.textBrowser_3 = QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(370, 680, 91, 31))
        self.textBrowser_4 = QTextBrowser(self.centralwidget)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(700, 510, 91, 31))
        self.textBrowser_5 = QTextBrowser(self.centralwidget)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(700, 590, 91, 31))
        self.textBrowser_6 = QTextBrowser(self.centralwidget)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(700, 680, 91, 31))
        self.textBrowser_13 = QTextBrowser(self.centralwidget)
        self.textBrowser_13.setObjectName(u"textBrowser_13")
        self.textBrowser_13.setGeometry(QRect(250, 100, 91, 31))
        self.textBrowser_14 = QTextBrowser(self.centralwidget)
        self.textBrowser_14.setObjectName(u"textBrowser_14")
        self.textBrowser_14.setGeometry(QRect(250, 210, 91, 31))
        self.textBrowser_15 = QTextBrowser(self.centralwidget)
        self.textBrowser_15.setObjectName(u"textBrowser_15")
        self.textBrowser_15.setGeometry(QRect(250, 320, 91, 31))
        self.textBrowser_16 = QTextBrowser(self.centralwidget)
        self.textBrowser_16.setObjectName(u"textBrowser_16")
        self.textBrowser_16.setGeometry(QRect(660, 100, 91, 31))
        self.textBrowser_17 = QTextBrowser(self.centralwidget)
        self.textBrowser_17.setObjectName(u"textBrowser_17")
        self.textBrowser_17.setGeometry(QRect(660, 210, 91, 31))
        self.textBrowser_18 = QTextBrowser(self.centralwidget)
        self.textBrowser_18.setObjectName(u"textBrowser_18")
        self.textBrowser_18.setGeometry(QRect(660, 320, 91, 31))
        self.textBrowser_19 = QTextBrowser(self.centralwidget)
        self.textBrowser_19.setObjectName(u"textBrowser_19")
        self.textBrowser_19.setGeometry(QRect(450, 110, 21, 31))
        self.textBrowser_20 = QTextBrowser(self.centralwidget)
        self.textBrowser_20.setObjectName(u"textBrowser_20")
        self.textBrowser_20.setGeometry(QRect(450, 220, 21, 31))
        self.textBrowser_21 = QTextBrowser(self.centralwidget)
        self.textBrowser_21.setObjectName(u"textBrowser_21")
        self.textBrowser_21.setGeometry(QRect(450, 330, 21, 31))
        self.textBrowser_22 = QTextBrowser(self.centralwidget)
        self.textBrowser_22.setObjectName(u"textBrowser_22")
        self.textBrowser_22.setGeometry(QRect(860, 100, 21, 31))
        self.textBrowser_23 = QTextBrowser(self.centralwidget)
        self.textBrowser_23.setObjectName(u"textBrowser_23")
        self.textBrowser_23.setGeometry(QRect(860, 220, 21, 31))
        self.textBrowser_24 = QTextBrowser(self.centralwidget)
        self.textBrowser_24.setObjectName(u"textBrowser_24")
        self.textBrowser_24.setGeometry(QRect(860, 320, 21, 31))
        self.textBrowser_26 = QTextBrowser(self.centralwidget)
        self.textBrowser_26.setObjectName(u"textBrowser_26")
        self.textBrowser_26.setGeometry(QRect(0, 800, 121, 31))
        self.plc_screen = QGraphicsView(self.centralwidget)
        self.plc_screen.setObjectName(u"graphicsView")
        self.plc_screen.setGeometry(QRect(120, 800, 41, 31))
        self.plc_screen.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.textBrowser_25 = QTextBrowser(self.centralwidget)
        self.textBrowser_25.setObjectName(u"textBrowser_25")
        self.textBrowser_25.setGeometry(QRect(270, 0, 611, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1133, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">SMPS 1</span></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">SMPS 2</span></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">SMPS 3</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">SMPS 4</span></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">SMPS 5</span></p></body></html>", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">SMPS 6</span></p></body></html>", None))
        self.textBrowser_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Voltage 1</span></p></body></html>", None))
        self.textBrowser_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Voltage 2</span></p></body></html>", None))
        self.textBrowser_15.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Voltage 3</span></p></body></html>", None))
        self.textBrowser_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Voltage 4</span></p></body></html>", None))
        self.textBrowser_17.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Voltage 5</span></p></body></html>", None))
        self.textBrowser_18.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Voltage 6</span></p></body></html>", None))
        self.textBrowser_19.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">V</span></p></body></html>", None))
        self.textBrowser_20.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">V</span></p></body></html>", None))
        self.textBrowser_21.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">V</span></p></body></html>", None))
        self.textBrowser_22.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">V</span></p></body></html>", None))
        self.textBrowser_23.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">V</span></p></body></html>", None))
        self.textBrowser_24.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">V</span></p></body></html>", None))
        self.textBrowser_26.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">PLC Status</span></p></body></html>", None))
        self.textBrowser_25.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">   Enigma Control &amp; Solution Pvt Ltd</span></p></body></html>", None))
    # retranslateUi

