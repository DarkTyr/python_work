class CALC:

    def __int__(self):
        self.vid = 0xDEADBEEF
        self.pid = 0x00000003
        self.name = 'calc_3'
        self.value = 0

    def run_calc(self, a, b, c):
        out = a + b * c
        self.value = a + c
        return out

    def value(self):
        return self.value
