# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Mon May 23 10:01:38 2016
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
        self.line_reg_2_int = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_2_int.setObjectName(_fromUtf8("line_reg_2_int"))
        self.gridLayout.addWidget(self.line_reg_2_int, 3, 3, 1, 1)
        self.line_reg_0_int = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_0_int.setObjectName(_fromUtf8("line_reg_0_int"))
        self.gridLayout.addWidget(self.line_reg_0_int, 1, 3, 1, 1)
        self.but_read_registers = QtGui.QPushButton(self.centralwidget)
        self.but_read_registers.setObjectName(_fromUtf8("but_read_registers"))
        self.gridLayout.addWidget(self.but_read_registers, 7, 2, 1, 1)
        self.line_reg_1_int = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_1_int.setObjectName(_fromUtf8("line_reg_1_int"))
        self.gridLayout.addWidget(self.line_reg_1_int, 2, 3, 1, 1)
        self.line_reg_3_int = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_3_int.setObjectName(_fromUtf8("line_reg_3_int"))
        self.gridLayout.addWidget(self.line_reg_3_int, 4, 3, 1, 1)
        self.line_reg_5_hex = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_5_hex.setObjectName(_fromUtf8("line_reg_5_hex"))
        self.gridLayout.addWidget(self.line_reg_5_hex, 6, 2, 1, 1)
        self.line_reg_0_hex = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_0_hex.setObjectName(_fromUtf8("line_reg_0_hex"))
        self.gridLayout.addWidget(self.line_reg_0_hex, 1, 2, 1, 1)
        self.line_reg_1_hex = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_1_hex.setObjectName(_fromUtf8("line_reg_1_hex"))
        self.gridLayout.addWidget(self.line_reg_1_hex, 2, 2, 1, 1)
        self.line_reg_2_hex = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_2_hex.setObjectName(_fromUtf8("line_reg_2_hex"))
        self.gridLayout.addWidget(self.line_reg_2_hex, 3, 2, 1, 1)
        self.line_reg_3_hex = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_3_hex.setObjectName(_fromUtf8("line_reg_3_hex"))
        self.gridLayout.addWidget(self.line_reg_3_hex, 4, 2, 1, 1)
        self.line_reg_4_hex = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_4_hex.setObjectName(_fromUtf8("line_reg_4_hex"))
        self.gridLayout.addWidget(self.line_reg_4_hex, 5, 2, 1, 1)
        self.line_reg_4_int = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_4_int.setObjectName(_fromUtf8("line_reg_4_int"))
        self.gridLayout.addWidget(self.line_reg_4_int, 5, 3, 1, 1)
        self.line_reg_5_int = QtGui.QLineEdit(self.centralwidget)
        self.line_reg_5_int.setObjectName(_fromUtf8("line_reg_5_int"))
        self.gridLayout.addWidget(self.line_reg_5_int, 6, 3, 1, 1)
        self.but_exit = QtGui.QPushButton(self.centralwidget)
        self.but_exit.setObjectName(_fromUtf8("but_exit"))
        self.gridLayout.addWidget(self.but_exit, 7, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_1 = QtGui.QLabel(self.centralwidget)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
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
        self.but_exit.setText(_translate("MainWindow", "Exit", None))
        self.label_3.setText(_translate("MainWindow", "Reg2", None))
        self.label_1.setText(_translate("MainWindow", "Reg0", None))
        self.label_2.setText(_translate("MainWindow", "Reg1", None))
        self.label_4.setText(_translate("MainWindow", "Reg3", None))
        self.label_5.setText(_translate("MainWindow", "Reg4", None))
        self.label_6.setText(_translate("MainWindow", "Reg5", None))
        self.label_8.setText(_translate("MainWindow", "Hex", None))
        self.label_7.setText(_translate("MainWindow", "Value", None))

