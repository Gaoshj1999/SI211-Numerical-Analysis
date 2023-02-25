# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:29:09 2020

@author: duola
"""

import math
from sympy import *
import matplotlib.pyplot as plt
true=1-math.sqrt(2)/2
print(true)
i3=math.pi/4*(1/8*math.sin(0)+3/8*math.sin(math.pi/12)+3/8*math.sin(math.pi/6)+1/8*math.sin(math.pi/4))
i5=math.pi/4*(19/288*math.sin(0)+25/96*math.sin(math.pi/20)+25/144*math.sin(math.pi/10)+25/144*math.sin(math.pi/20*3)+25/96*math.sin(math.pi/5)+19/288*math.sin(math.pi/4))
print(i3-true)
print(i5-true)