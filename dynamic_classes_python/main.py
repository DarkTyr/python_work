import os
from PyQt4 import QtGui
import imp
import sys
import signal
'''ctrl+c grabber to instantly kill the program'''
signal.signal(signal.SIGINT, signal.SIG_DFL)
import fw_template
fw_module = fw_template

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.fw_class = ''

    def initUI(self):
        dlg = QtGui.QFileDialog()
        dlg.setFileMode(QtGui.QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.py)")
        if dlg.exec_():
            filename = dlg.selectedFiles()
        self.fw_class = filename


def main():
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


if __name__ == '__main__':
    main()
