# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
x=0.000000000000001
for i in range(6):
    print(math.log(x,10))
    x=x*10
for i in range(99):
    print(math.log(x,10))
    x=x+0.000000001
for i in range(7):
    print(math.log(x,10))
    x=x*10
print(math.log(0.1,10))
import math
from decimal import Decimal
a=0.0000000001
c=Decimal.from_float(1-math.cos(0.0000001)/(a*a))
x=0.000000000000001
for i in range(6):
    y=(1-math.cos(x))/(x*x)
    print(y)
    x=x*10
for i in range(99):
    y=(1-math.cos(x))/(x*x)
    print(y)
    x=x+0.000000001
for i in range(7):
    y=(1-math.cos(x))/(x*x)
    print(y)
    x=x*10
print((1-math.cos(0.1))/(0.1*0.1))
