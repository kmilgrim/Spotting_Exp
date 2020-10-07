# -*- coding: utf-8 -*-

#user input (goto)

# Form implementation generated from reading ui file 'Spotexp_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# Hey Iris ily!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from functools import partial
from pathlib import Path
import sys
import pickle
import os
from pyaxidraw import axidraw
from ModifyWindow_GUI import Ui_ModifyWindow
# import csv
# from pyaxidraw import axidraw
# from PyQt5.QtWidgets import *
# app = QApplication([])
# app.setStyle('Fusion')

# makes GUI correct size for higher screen resolution

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

# Set up the main GUI window
class Ui_SpottingExp(QMainWindow):

    # Literally set up all the buttons and other pretty things
    def setupUi(self, SpottingExp):
        self.connection = False # variable to see the connection status of the axidraw

        self.ad = axidraw.AxiDraw()          # Initialize class
        self.ad.interactive()                # Enter interactive context
        self.ad.options.units = 1            # change units to centimeters

        SpottingExp.setObjectName("SpottingExp")
        SpottingExp.resize(578, 380)
        SpottingExp.setWindowOpacity(1)
        self.centralwidget = QtWidgets.QWidget(SpottingExp)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 281, 51))
        font_16 = QtGui.QFont()
        font_16.setFamily("Yu Gothic UI Semilight")
        font_16.setPointSize(16)
        self.label.setFont(font_16)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 75, 23))
        font_10 = QtGui.QFont()
        font_10.setFamily("Yu Gothic UI Light")
        font_10.setPointSize(10)
        self.pushButton.setFont(font_10)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 50, 75, 23))
        self.pushButton_2.setFont(font_10)
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(180, 100, 61, 21))
        font_12 = QtGui.QFont()
        font_12.setFamily("Yu Gothic Light")
        font_12.setPointSize(12)
        self.spinBox.setFont(font_12)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox.setMaximum(500)
        self.spinBox.setSingleStep(10)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.label_2.setFont(font_12)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 161, 21))
        self.label_3.setFont(font_12)
        self.label_3.setObjectName("label_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(250, 100, 61, 22))
        self.spinBox_2.setFont(font_12)
        self.spinBox_2.setMaximum(500)
        self.spinBox_2.setSingleStep(10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 151, 31))
        self.label_4.setFont(font_12)
        self.label_4.setObjectName("label_4")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(320, 100, 61, 22))
        self.spinBox_3.setFont(font_12)
        self.spinBox_3.setMaximum(500)
        self.spinBox_3.setSingleStep(10)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 161, 21))
        self.label_5.setFont(font_12)
        self.label_5.setObjectName("label_5")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(180, 140, 61, 22))
        self.spinBox_4.setFont(font_12)
        self.spinBox_4.setMaximum(500)
        self.spinBox_4.setSingleStep(10)
        self.spinBox_4.setObjectName("spinBox_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 50, 81, 31))
        self.pushButton_3.setFont(font_12)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 90, 81, 31))
        self.pushButton_4.setFont(font_12)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(460, 130, 81, 31))
        self.pushButton_8.setFont(font_12)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setGeometry(QtCore.QRect(460, 170, 81, 31))
        self.pushButton_9.setFont(font_12)
        self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(250, 140, 61, 22))
        self.spinBox_5.setFont(font_12)
        self.spinBox_5.setMaximum(500)
        self.spinBox_5.setSingleStep(10)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(320, 140, 61, 22))
        self.spinBox_6.setFont(font_12)
        self.spinBox_6.setMaximum(500)
        self.spinBox_6.setSingleStep(10)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_7.setGeometry(QtCore.QRect(180, 180, 101, 22))
        self.spinBox_7.setFont(font_12)
        self.spinBox_7.setMaximum(100)
        self.spinBox_7.setProperty("value", 60)
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_8.setGeometry(QtCore.QRect(180, 220, 101, 22))
        self.spinBox_8.setFont(font_12)
        self.spinBox_8.setMaximum(100)
        self.spinBox_8.setProperty("value", 40)
        self.spinBox_8.setObjectName("spinBox_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 371, 31))
        self.label_6.setFont(font_12)
        self.label_6.setObjectName("label_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 50, 171, 23))
        self.pushButton_5.setFont(font_10)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 300, 75, 30))
        font_bold12 = QtGui.QFont()
        font_bold12.setFamily("Yu Gothic UI Semibold")
        font_bold12.setPointSize(12)
        font_bold12.setBold(True)
        font_bold12.setWeight(75)
        self.pushButton_6.setFont(font_bold12)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(470, 300, 75, 30))
        self.pushButton_10.setFont(font_12)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 260, 341, 31))
        self.label_7.setFont(font_12)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 260, 341, 31))
        self.label_8.setFont(font_12)
        self.label_8.setObjectName("label_8")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(170, 265, 51, 23))
        self.lineEdit_1.setFont(font_12)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(275, 265, 51, 23))
        self.lineEdit_2.setFont(font_12)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 265, 40, 25))
        self.pushButton_7.setFont(font_12)
        self.pushButton_7.setObjectName("pushButton_7")
        SpottingExp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SpottingExp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 22))
        self.menubar.setObjectName("menubar")
        SpottingExp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SpottingExp)
        self.statusbar.setObjectName("statusbar")
        SpottingExp.setStatusBar(self.statusbar)

        self.retranslateUi(SpottingExp)
        QtCore.QMetaObject.connectSlotsByName(SpottingExp)

        # Connect buttons to events and functions
        self.pushButton.clicked.connect(self.connectAxi)
        self.pushButton_3.clicked.connect(lambda: self.ad.penup())
        self.pushButton_4.clicked.connect(lambda: self.ad.pendown())
        self.pushButton_8.clicked.connect(lambda: self.ad.goto(0, 0))
        self.pushButton_9.clicked.connect(self.updateSettings)
        self.pushButton_2.clicked.connect(self.disconnectAxi)
        self.pushButton_5.clicked.connect(self.DrawChip)
        self.pushButton_7.clicked.connect(self.moveto_xy)
        self.pushButton_6.clicked.connect(self.runSpotter)
        # modifySettings will be a function that brings the user to a pop up
        # window where they can specify how many rows of spots they want and
        # how many columns they want of each pen delay.
        # It's a work in progress srry. LMK if it's nice tho.
        self.pushButton_10.clicked.connect(self.openModifyWin)


    # adding text to all the buttons and labels <3
    def retranslateUi(self, SpottingExp):
        _translate = QtCore.QCoreApplication.translate
        SpottingExp.setWindowTitle(_translate("SpottingExp", "Spotting Experiment"))
        self.label.setText(_translate("SpottingExp", "AxiDraw Spotting Experiment"))
        self.pushButton.setText(_translate("SpottingExp", "Connect"))
        self.pushButton_2.setText(_translate("SpottingExp", "Disconnect"))
        self.label_2.setText(_translate("SpottingExp", "Pen Delay Down (ms)"))
        self.label_3.setText(_translate("SpottingExp", "Pen Delay Up (ms)"))
        self.label_4.setText(_translate("SpottingExp", "Pen Position Up (%)"))
        self.label_5.setText(_translate("SpottingExp", "Pen Position Down (%)"))
        self.pushButton_3.setText(_translate("SpottingExp", "Pen Up"))
        self.pushButton_4.setText(_translate("SpottingExp", "Pen Down"))
        self.label_6.setText(_translate("SpottingExp", "3) Will print two lines of dots for each configuration."))
        self.pushButton_5.setText(_translate("SpottingExp", "1) Draw Placement Box"))
        self.pushButton_6.setText(_translate("SpottingExp", "Spot!"))
        self.pushButton_10.setText(_translate("SpottingExp", "Modify"))
        self.label_7.setText(_translate("SpottingExp", "2) Pen Placement x: "))
        self.label_8.setText(_translate("SpottingExp", "y: "))
        self.pushButton_7.setText(_translate("SpottingExp", "Go"))
        self.pushButton_8.setText(_translate("SpottingExp", "Home"))
        self.pushButton_9.setText(_translate("SpottingExp", "Update"))

    # connect AxiDraw if it isn't already connected.
    def connectAxi(self):
        if self.connection == False:
            self.ad.connect()
            self.connection = True
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("AxiDraw is now connected.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        elif self.connection == True:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("AxiDraw is already connected.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    # disconnect Axidraw duh.
    def disconnectAxi(self):
        if self.connection == True:
            self.ad.disconnect()
            self.connection = False
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("AxiDraw is now disconnected.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        elif self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("AxiDraw is already disconnected.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    # move to the position you indicate
    def moveto_xy(self):
        x_pos = float(self.lineEdit_1.text())
        y_pos = float(self.lineEdit_2.text())
        print(x_pos)
        print(y_pos)
        self.ad.moveto(x_pos, y_pos) # move to the position indicated by the user

    # update the settings of the AxiDraw when changing the pen position
    def updateSettings(self):
        if self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("Please connect the AxiDraw.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        elif
            penPosUp = int(self.spinBox_7.text())
            penPosDown = int(self.spinBox_8.text())
            print(penPosUp)
            print(type(penPosUp))
            self.ad.options.pen_pos_up = penPosUp
            self.ad.options.pen_pos_down = penPosDown
            self.ad.update()
            msg = QMessageBox()
            msg.setWindowTitle("Pen Pos")
            msg.setText("Pen positions have been updated.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            return

    # Here's the good stuff. This is the function that actually runs the
    # spotting experiment. You can change things manually about your rows and
    # columns here.
    def runSpotter(self):
        if self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("Please connect the AxiDraw.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

        def makeRow(self):
            self.ad.update()

            # AxiDraw will make 9 spots then move to the next row.
            for i in range(9):
                self.ad.pendown()
                self.ad.penup()
                self.ad.go(.15, 0)
            self.ad.go(-1.35, .15)

        # update the pen delay settings based on the input from the user
        penDelayDown_1 = int(self.spinBox.text())
        penDelayDown_2 = int(self.spinBox_2.text())
        penDelayDown_3 = int(self.spinBox_3.text())
        penDelayUp_1 = int(self.spinBox_4.text())
        penDelayUp_2 = int(self.spinBox_5.text())
        penDelayUp_3 = int(self.spinBox_6.text())

        # Make 6 rows in total, with each set of 2 being another pen delay value
        # If you want to change the number of rows per pen delay, just call
        # makeRow in a loop (rn it's just called 2 times so it isn't looped).
        # To only test 1 or 2 pen delay values, change the range in the for
        # loop below.
        for i in range(3)
            self.ad.options.pen_delay_down = penDelayDown_1
            self.ad.options.pen_delay_up = penDelayUp_1

            makeRow(self)
            makeRow(self)

        self.ad.goto(0, 0)

    # function that will draw a box with the exact dimensions of the chip
    # so you can place it on paper or whatever.
    def DrawChip(self):
        if self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("Please connect the AxiDraw.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        else
            for i in range(2):
                self.ad.pendown()
                self.ad.go(2.5, 0)
                self.ad.go(0, 1.2)
                self.ad.go(-2.5, 0)
                self.ad.go(0, -1.2)
            self.ad.penup()
            self.ad.goto(0, 0)

    # work in progress, lmk how this is so far plz
    def openModifyWin(self):
        if self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("Please connect the AxiDraw.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        elif
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ModifyWindow()
            self.ui.setupUi(self.window)
            self.window.show()


# close gui and stuff
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpottingExp = QtWidgets.QMainWindow()
    ui = Ui_SpottingExp()
    ui.setupUi(SpottingExp)
    SpottingExp.show()
    sys.exit(app.exec_())
