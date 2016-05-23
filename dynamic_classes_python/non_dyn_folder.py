'''This worked by adding the folder to the python path. But pycahrm didn't know how to handle it.'''
#import sys
#sys.path.insert(0, 'fic/')

'''Ths works as well as long as there is an __init__ file in the directory with a list of all of the files in the
all def'''
from fic import *


ob1 = calc_1.CALC()
ob2 = calc_2.CALC()
ob3 = calc_3.CALC()

a = 2
b = 3
c = 4

print ob1.run_calc(a, b, c), ob1.value
print ob2.run_calc(a, b, c), ob2.value
print ob3.run_calc(a, b, c), ob3.value