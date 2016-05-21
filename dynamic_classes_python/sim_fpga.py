import numpy as np


class SIM_FPGA:
    def __init__(self):
        self.reg0 = 0x00000
        self.reg1 = 0x00000
        self.reg2 = 0x00000
        self.reg3 = 0x00000
        self.reg4 = 0x00000
        self.reg5 = 0x00000
        self.reg6 = 0x00000
        self.reg7 = 0x00000
        self.reg8 = 0x00000
        self.reg9 = 0x00000
    '''This is needed to prevent python from creating a new class variable when you call setattr()'''
    def __setattr__(self, attribute, value):
        if attribute not in self.__dict__:
            print "Cannot set %s" % attribute
        else:
            self.__dict__[attribute] = value

    def write_int(self, reg, value):
        setattr(self, reg, value)
        print 'Writing ' + hex(value) + ' to register ' + str(reg)

    def read_int(self, reg):
        value = getattr(self, reg)
        print 'Reading ' + hex(value) + ' from register ' + str(reg)
        return value
