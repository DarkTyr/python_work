import numpy as np
import time
import sim_fpga
fpga = sim_fpga.SIM_FPGA()


class FW_INTERFACE_CLASS:
    def __init__(self, fpga=None):
        if fpga == None:
            self.fpga = sim_fpga.SIM_FPGA()
        else:
            self.fpga = fpga

    def write_value(self, reg, value):
        self.fpga.write_int(reg, value)
        return 0

    def read_value(self, reg):
        return self.fpga.read_int(reg)
