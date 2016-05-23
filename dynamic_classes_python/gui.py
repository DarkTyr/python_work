# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun May 22 19:04:53 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(333, 290)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_reg_5 = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_5.setObjectName(_fromUtf8("line_reg_5"))
        self.gridLayout.addWidget(self.line_reg_5, 5, 2, 1, 1)
        self.but_read_registers = QtGui.QPushButton(self.centralwidget)
        self.but_read_registers.setObjectName(_fromUtf8("but_read_registers"))
        self.gridLayout.addWidget(self.but_read_registers, 6, 2, 1, 1)
        self.line_reg_0 = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_0.setObjectName(_fromUtf8("line_reg_0"))
        self.gridLayout.addWidget(self.line_reg_0, 0, 2, 1, 1)
        self.but_read_reg_1 = QtGui.QPushButton(self.centralwidget)
        self.but_read_reg_1.setObjectName(_fromUtf8("but_read_reg_1"))
        self.gridLayout.addWidget(self.but_read_reg_1, 1, 0, 1, 1)
        self.but_read_reg_0 = QtGui.QPushButton(self.centralwidget)
        self.but_read_reg_0.setObjectName(_fromUtf8("but_read_reg_0"))
        self.gridLayout.addWidget(self.but_read_reg_0, 0, 0, 1, 1)
        self.line_reg_1 = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_1.setObjectName(_fromUtf8("line_reg_1"))
        self.gridLayout.addWidget(self.line_reg_1, 1, 2, 1, 1)
        self.but_read_reg_2 = QtGui.QPushButton(self.centralwidget)
        self.but_read_reg_2.setObjectName(_fromUtf8("but_read_reg_2"))
        self.gridLayout.addWidget(self.but_read_reg_2, 2, 0, 1, 1)
        self.line_reg_2 = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_2.setObjectName(_fromUtf8("line_reg_2"))
        self.gridLayout.addWidget(self.line_reg_2, 2, 2, 1, 1)
        self.but_read_reg_3 = QtGui.QPushButton(self.centralwidget)
        self.but_read_reg_3.setObjectName(_fromUtf8("but_read_reg_3"))
        self.gridLayout.addWidget(self.but_read_reg_3, 3, 0, 1, 1)
        self.line_reg_3 = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_3.setObjectName(_fromUtf8("line_reg_3"))
        self.gridLayout.addWidget(self.line_reg_3, 3, 2, 1, 1)
        self.but_read_reg_4 = QtGui.QPushButton(self.centralwidget)
        self.but_read_reg_4.setObjectName(_fromUtf8("but_read_reg_4"))
        self.gridLayout.addWidget(self.but_read_reg_4, 4, 0, 1, 1)
        self.line_reg_4 = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_4.setObjectName(_fromUtf8("line_reg_4"))
        self.gridLayout.addWidget(self.line_reg_4, 4, 2, 1, 1)
        self.but_read_reg_5 = QtGui.QPushButton(self.centralwidget)
        self.but_read_reg_5.setObjectName(_fromUtf8("but_read_reg_5"))
        self.gridLayout.addWidget(self.but_read_reg_5, 5, 0, 1, 1)
        self.but_exit = QtGui.QPushButton(self.centralwidget)
        self.but_exit.setObjectName(_fromUtf8("but_exit"))
        self.gridLayout.addWidget(self.but_exit, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.but_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Firmware Control GUI", None))
        self.but_read_registers.setText(_translate("MainWindow", "Read Registers", None))
        self.but_read_reg_1.setText(_translate("MainWindow", "reg1", None))
        self.but_read_reg_0.setText(_translate("MainWindow", "reg0", None))
        self.but_read_reg_2.setText(_translate("MainWindow", "reg2", None))
        self.but_read_reg_3.setText(_translate("MainWindow", "reg3", None))
        self.but_read_reg_4.setText(_translate("MainWindow", "reg4", None))
        self.but_read_reg_5.setText(_translate("MainWindow", "reg5", None))
        self.but_exit.setText(_translate("MainWindow", "Exit", None))

