import os
from PyQt4 import QtGui
import imp
import sys
import signal
import gui
import numpy as np
import pylab as pl
'''ctrl+c grabber to instantly kill the program'''
signal.signal(signal.SIGINT, signal.SIG_DFL)
import fw_template
#fw_module_ob = fw_template.FW_INTERFACE_CLASS()


class MAINGUI(QtGui.QMainWindow):
    def __init__(self, fw_module_ob):
        QtGui.QMainWindow.__init__(self)
        self.fw_module_ob = fw_module_ob
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_buttons()
        self.read_reg_all()

    def connect_buttons(self):
        self.ui.but_exit.clicked.connect(QtGui.qApp.quit)

        self.ui.but_read_registers.clicked.connect(self.read_reg_all)

        self.ui.line_reg_0_hex.returnPressed.connect(self.write_reg_0_hex)
        self.ui.line_reg_1_hex.returnPressed.connect(self.write_reg_1_hex)
        self.ui.line_reg_2_hex.returnPressed.connect(self.write_reg_2_hex)
        self.ui.line_reg_3_hex.returnPressed.connect(self.write_reg_3_hex)
        self.ui.line_reg_4_hex.returnPressed.connect(self.write_reg_4_hex)
        self.ui.line_reg_5_hex.returnPressed.connect(self.write_reg_5_hex)

        self.ui.line_reg_0_int.returnPressed.connect(self.write_reg_0_int)
        self.ui.line_reg_1_int.returnPressed.connect(self.write_reg_1_int)
        self.ui.line_reg_2_int.returnPressed.connect(self.write_reg_2_int)
        self.ui.line_reg_3_int.returnPressed.connect(self.write_reg_3_int)
        self.ui.line_reg_4_int.returnPressed.connect(self.write_reg_4_int)
        self.ui.line_reg_5_int.returnPressed.connect(self.write_reg_5_int)


    def write_reg_0_hex(self):
        value = int(str(self.ui.line_reg_0_hex.text()), 16)
        self.ui.line_reg_0_int.setText(str(value))
        self.fw_module_ob.write_value('reg0', value)

    def write_reg_1_hex(self):
        value = int(str(self.ui.line_reg_1_hex.text()), 16)
        self.ui.line_reg_1_int.setText(str(value))
        self.fw_module_ob.write_value('reg1', value)

    def write_reg_2_hex(self):
        value = int(str(self.ui.line_reg_2_hex.text()), 16)
        self.ui.line_reg_2_int.setText(str(value))
        self.fw_module_ob.write_value('reg2', value)

    def write_reg_3_hex(self):
        value = int(str(self.ui.line_reg_3_hex.text()), 16)
        self.ui.line_reg_3_int.setText(str(value))
        self.fw_module_ob.write_value('reg3', value)

    def write_reg_4_hex(self):
        value = int(str(self.ui.line_reg_4_hex.text()), 16)
        self.ui.line_reg_4_int.setText(str(value))
        self.fw_module_ob.write_value('reg4', value)

    def write_reg_5_hex(self):
        value = int(str(self.ui.line_reg_5_hex.text()), 16)
        self.ui.line_reg_5_int.setText(str(value))
        self.fw_module_ob.write_value('reg5', value)

    def write_reg_0_int(self):
        value = int(str(self.ui.line_reg_0_int.text()))
        self.ui.line_reg_0_hex.setText(hex(value))
        self.fw_module_ob.write_value('reg0', value)

    def write_reg_1_int(self):
        value = int(str(self.ui.line_reg_1_int.text()))
        self.ui.line_reg_1_hex.setText('0x' + '%X' % value)
        self.fw_module_ob.write_value('reg1', value)

    def write_reg_2_int(self):
        value = int(str(self.ui.line_reg_2_int.text()))
        self.ui.line_reg_2_hex.setText('0x' + '%X' % value)
        self.fw_module_ob.write_value('reg2', value)

    def write_reg_3_int(self):
        value = int(str(self.ui.line_reg_3_int.text()))
        self.ui.line_reg_3_hex.setText('0x' + '%X' % value)
        self.fw_module_ob.write_value('reg3', value)

    def write_reg_4_int(self):
        value = int(str(self.ui.line_reg_4_int.text()))
        self.ui.line_reg_4_hex.setText('0x' + '%X' % value)
        self.fw_module_ob.write_value('reg4', value)

    def write_reg_5_int(self):
        value = int(str(self.ui.line_reg_5_int.text()))
        self.ui.line_reg_5_hex.setText('0x' + '%X' % value)
        self.fw_module_ob.write_value('reg5', value)

    def read_reg_all(self):
        value = self.fw_module_ob.read_value('reg0')
        self.ui.line_reg_0_hex.setText('0x' + '%X' % value)
        self.ui.line_reg_0_int.setText(str(int(value)))

        value = self.fw_module_ob.read_value('reg1')
        self.ui.line_reg_1_hex.setText('0x' + '%X' % value)
        self.ui.line_reg_1_int.setText(str(int(value)))

        value = self.fw_module_ob.read_value('reg2')
        self.ui.line_reg_2_hex.setText('0x' + '%X' % value)
        self.ui.line_reg_2_int.setText(str(int(value)))

        value = self.fw_module_ob.read_value('reg3')
        self.ui.line_reg_3_hex.setText('0x' + '%X' % value)
        self.ui.line_reg_3_int.setText(str(int(value)))

        value = self.fw_module_ob.read_value('reg4')
        self.ui.line_reg_4_hex.setText('0x' + '%X' % value)
        self.ui.line_reg_4_int.setText(str(int(value)))

        value = self.fw_module_ob.read_value('reg5')
        self.ui.line_reg_5_hex.setText('0x' + '%X' % value)
        self.ui.line_reg_5_int.setText(str(int(value)))

def main():
    app = QtGui.QApplication(sys.argv)
    #app.setStyleSheet(styleSheet)
    fw_class_path = str(QtGui.QFileDialog.getOpenFileName(
                                 caption='Select Firmware Class to build GUI with',
                                 filter='*.py'))
    fw_module = imp.load_source(fw_class_path.rsplit('/', 1)[-1], fw_class_path)
    fw_module_ob = fw_module.FW_INTERFACE_CLASS()
    window = MAINGUI(fw_module_ob)
    window.show()
    sys.exit(app.exec_())
    
    

    # '''Make a Qt app to start the GUI'''
    # app = QtGui.QApplication(sys.argv)
    # '''Trying to make it close gracefully'''
    # app.quitOnLastWindowClosed = True
    # '''Open popup for the user to select firmware class'''
    # fw_class_path = str(QtGui.QFileDialog.getOpenFileName(
    #                         caption='Select Firmware Class to build GUI with',
    #                         filter='*.py'))
    # '''For now a debug tool to print the path to the file'''
    # print fw_class_path
    # '''Import the module and assign the module to ob1'''
    # fw_module = imp.load_source(fw_class_path.rsplit('/', 1)[-1], fw_class_path)
    # '''instantiate a class object from the module as ob2 and run'''
    # fw_class = fw_module.FW_INTERFACE_CLASS()
    # fw_class.write_value('reg3', 0xDEADBEEF)
    # fw_class.read_value('reg3')
    # fw_class.read_value('reg0')
    # fw_class.read_value('reg1')
    # fw_class.write_value('reg10', 0xDEADBEEF)
    # fw_class.read_value('reg10')
    # sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    '''
    class R2Gui(QMainWindow):    
     def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionQuit.triggered.connect(QtGui.qApp.quit)

        self.ui.cb_lo_port.insertItem(0, 'phasematrix1')
        self.ui.cb_lo_port.insertItem(1, 'phasematrix2')
        self.ui.cb_lo_port.setCurrentIndex(0)
        
        self.ui.pb_reload_all.clicked.connect(self.reload_tones)
        
        
        
    if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(styleSheet)
    window = R2Gui()
    window.show()
    sys.exit(app.exec_())
    '''