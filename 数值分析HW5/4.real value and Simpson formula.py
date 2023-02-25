# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 01:06:07 2020

@author: duola
"""

import math
from sympy import *
import matplotlib.pyplot as plt
x = symbols('x')
true1=integrate(sin(9/10*x), (x, 0, 0.5))
true2=integrate(x**3, (x, 0, 1))
true3=math.sin(1)
s1=0.5/6*(math.sin(9/10*0)+4*math.sin(9/10*0.25)+math.sin(9/10*0.5))
s2=1/6*(0+4*0.5**3+1*1)
s3=1/6*(math.cos(0)+4*math.cos(0.5)+math.cos(1))
print("true1:",true1)
print("true2:",true2)
print("true3:",true3)
print("s1:",s1)
print("s2:",s2)
print("s3:",s3)
