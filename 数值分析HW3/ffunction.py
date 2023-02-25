# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:59:46 2020

@author: duola
"""

from sympy import symbols
from sympy import *
x = symbols('x')
fx=1/(1+x**2)
diff1=diff(fx,x)
diff2=diff(diff1,x)
print(integrate(diff2**2,(x,-5,5)))