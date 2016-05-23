import os
from PyQt4 import QtGui
import imp
import sys
import signal
import gui
'''ctrl+c grabber to instantly kill the program'''
signal.signal(signal.SIGINT, signal.SIG_DFL)
import fw_template
fw_module = fw_template

class MAINGUI(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionQuit.triggered.connect(QtGui.qApp.quit)
        
    def connect_buttons():
        
    def read_reg_0():
        

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(styleSheet)
    window = MAINGUI()
    window.show()
    sys.exit(app.exec_())
    
    
    '''
    '''Make a Qt app to start the GUI'''
    app = QtGui.QApplication(sys.argv)
    '''Trying to make it close gracefully'''
    app.quitOnLastWindowClosed = True
    '''Open popup for the user to select firmware class'''
    fw_class_path = str(QtGui.QFileDialog.getOpenFileName(
                            caption='Select Firmware Class to build GUI with',
                            filter='*.py'))
    '''For now a debug tool to print the path to the file'''
    print fw_class_path
    '''Import the module and assign the module to ob1'''
    fw_module = imp.load_source(fw_class_path.rsplit('/', 1)[-1], fw_class_path)
    '''instantiate a class object from the module as ob2 and run'''
    fw_class = fw_module.FW_INTERFACE_CLASS()
    fw_class.write_value('reg3', 0xDEADBEEF)
    fw_class.read_value('reg3')
    fw_class.read_value('reg0')
    fw_class.read_value('reg1')
    fw_class.write_value('reg10', 0xDEADBEEF)
    fw_class.read_value('reg10')
    sys.exit(app.exec_())
'''

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