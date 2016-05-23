import numpy as np
import sys

'''This is needed to prevent python from creating a new class variable when you call setattr()'''
class FrozenClass(object):
    __isfrozen = False

    def __setattr__(self, key, value):
        if self.__isfrozen and not hasattr(self, key):
            raise TypeError( "%r is a frozen class" % self )
        object.__setattr__(self, key, value)

    def _freeze(self):
        self.__isfrozen = True

class SIM_FPGA(FrozenClass):
    def __init__(self):
        self.list_reg = ['reg0',
                         'reg1',
                         'reg2',
                         'reg3',
                         'reg4',
                         'reg5']
        for x in self.list_reg:
            setattr(self, x, 0x00000000)

        self._freeze()

    def write_int(self, reg, value):
        setattr(self, reg, value)
        print 'Writing ' + hex(value) + ' to register ' + str(reg)

    def read_int(self, reg):
        value = getattr(self, reg)
        print 'Reading ' + hex(value) + ' from register ' + str(reg)
        return value
