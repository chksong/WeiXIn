# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:44:47 2018

@author: Administrator
"""


import numpy as np
from math import  pi
from matplotlib import pyplot as plt 
 
import base64

from io import BytesIO
from PIL import Image

#def showimage(request):
    # Construct the graph
t = np.arange(0.0, 2.0, 0.01)
s =5* np.sin(2*pi*t)
plt.plot(t, s, linewidth=1.0)
 
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
fig = plt.figure()
plt.show()

imgdata = BytesIO()
fig.savefig(imgdata, format='png')
imgdata.seek(0)  # rewind the data
   # im = Image.open(imgimgdatadata)
   
buffer = b''.join(imgdata)
b2 = base64.b64encode(buffer)
im=b2.decode('utf-8')
    
#return im
 
    # Send buffer in a http response the the browser with the mime type image/png set
    #return HttpResponse(buffer.getvalue(), content_type="image/png")
