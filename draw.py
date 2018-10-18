# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:52:08 2018

@author: Administrator
"""

from matplotlib import pyplot as plt 
from pylab import mpl

import numpy as np
from math import sin,pi


t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*pi*t)
plt.plot(t, s, linewidth=1.0)
 
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.axis('equal')
plt.legend()

plt.show()

