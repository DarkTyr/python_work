import os
from PyQt4 import QtGui
import imp
import sys
import signal
import gui
'''ctrl+c grabber to instantly kill the program'''
signal.signal(signal.SIGINT, signal.SIG_DFL)
import fw_template
fw_module_ob = fw_template.FW_INTERFACE_CLASS()

class MAINGUI(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.but_exit.clicked.connect(QtGui.qApp.quit)

        self.ui.but_read_reg_0.clicked.connect(self.read_reg_0)
        self.ui.but_read_reg_1.clicked.connect(self.read_reg_1)
        self.ui.but_read_reg_2.clicked.connect(self.read_reg_2)
        self.ui.but_read_reg_3.clicked.connect(self.read_reg_3)
        self.ui.but_read_reg_4.clicked.connect(self.read_reg_4)
        self.ui.but_read_reg_5.clicked.connect(self.read_reg_5)

        self.ui.but_read_registers.clicked.connect(self.read_reg_all)

        self.ui.line_reg_0.returnPressed.connect(self.write_reg_0)
        self.ui.line_reg_1.returnPressed.connect(self.write_reg_1)
        self.ui.line_reg_2.returnPressed.connect(self.write_reg_2)
        self.ui.line_reg_3.returnPressed.connect(self.write_reg_3)
        self.ui.line_reg_4.returnPressed.connect(self.write_reg_4)
        self.ui.line_reg_5.returnPressed.connect(self.write_reg_5)

    def read_reg_0(self):
        value = fw_module_ob.read_value('reg0')
        self.ui.line_reg_0.setText(hex(value))

    def read_reg_1(self):
        value = fw_module_ob.read_value('reg1')
        self.ui.line_reg_1.setText(hex(value))

    def read_reg_2(self):
        value = fw_module_ob.read_value('reg2')
        self.ui.line_reg_2.setText(hex(value))

    def read_reg_3(self):
        value = fw_module_ob.read_value('reg3')
        self.ui.line_reg_3.setText(hex(value))

    def read_reg_4(self):
        value = fw_module_ob.read_value('reg4')
        self.ui.line_reg_4.setText(hex(value))

    def read_reg_5(self):
        value = fw_module_ob.read_value('reg5')
        self.ui.line_reg_5.setText(hex(value))

    def write_reg_0(self):
        value = int(str(self.ui.line_reg_0.text()), 16)
        fw_module_ob.write_value('reg0', value)

    def write_reg_1(self):
        value = int(str(self.ui.line_reg_1.text()), 16)
        fw_module_ob.write_value('reg1', value)

    def write_reg_2(self):
        value = int(str(self.ui.line_reg_2.text()), 16)
        fw_module_ob.write_value('reg2', value)

    def write_reg_3(self):
        value = int(str(self.ui.line_reg_3.text()), 16)
        fw_module_ob.write_value('reg3', value)

    def write_reg_4(self):
        value = int(str(self.ui.line_reg_4.text()), 16)
        fw_module_ob.write_value('reg4', value)

    def write_reg_5(self):
        value = int(str(self.ui.line_reg_5.text()), 16)
        fw_module_ob.write_value('reg5', value)

    def read_reg_all(self):
        self.read_reg_0()
        self.read_reg_1()
        self.read_reg_2()
        self.read_reg_3()
        self.read_reg_4()
        self.read_reg_5()

def main():
    app = QtGui.QApplication(sys.argv)
    #app.setStyleSheet(styleSheet)
    window = MAINGUI()
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