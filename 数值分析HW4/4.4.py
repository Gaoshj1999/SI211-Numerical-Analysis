# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:18:40 2020

@author: duola
"""

import math
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
x=symbols("x")  # 符号x，自变量
from sympy import *
x = symbols('x')
fx=math.e**x
gx=2.2812*x*x-2.249*x+2.7215
a = np.linspace(1,2,1000)
b = [fx.evalf(subs={x:t}) for t in a]
c = [gx.evalf(subs={x:t}) for t in a]
plt.plot(a, c)
plt.plot(a, b)
plt.show()