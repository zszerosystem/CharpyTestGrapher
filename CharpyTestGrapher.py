# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d
import scipy.interpolate as spi

"this is for percentage crystallinity vs temp"
# # graph=np.array([200,0],[0,10],[-20,90],[-80,100],[-195,100])
# # cline=np.array([200,50],[0,50],[-20,50],[-80,50],[-195,50])
# gx=np.array([200,0,-20,-80,-195])
# gy=np.array([0,0,0,0,0])

# lx=np.array([200,0,-20,-80,-195])
# ly=np.array([50,50,50,50,50])

# auxliney=np.arange(0,51)
# auxlinex=np.array([-45]*51)

# plt.plot(gx,gy)
# # plt.plot(lx,ly,':')
# # plt.plot(auxlinex,auxliney,':')
# plt.xlabel("Temperature℃")
# plt.ylabel("Percentage Crystallinity")

# x=np.linspace(-20,0,1000)
# m=(10-90)/(0-(-20))

"this is for impact energy "

"temperature"
x = np.array([-195, -80, -20, 0, 20,50,80, 100, 200]) 
'energy'
y = np.array([2, 3, 12, 24, 158, 149,260,271,258])  

"interpolation"
X_Y_Spline = spi.Akima1DInterpolator(x, y)

# X_Y_Spline = make_interp_spline(x, y,k=3)
# cubic_interploation_model = interp1d(x, y, kind = "cubic")
X_ = np.linspace(x.min(), x.max(), 1000)
Y_ = X_Y_Spline(X_)
plt.plot(X_, Y_)
# plt.plot(x,y)

"finding intersection"
avg=(np.min(y)+np.max(y))/2
lx=np.linspace(-195,200,1000)
ly=np.array([avg]*1000)

idx = np.argwhere(np.diff(np.sign(Y_-ly))).flatten()
plt.plot(X_[idx], ly[idx],'ro')
print(lx[idx])


"construction lines"

plt.plot(lx,ly,":")
auxliney=np.arange(0,200)
auxlinex=np.array([lx[idx]]*200)
plt.plot(auxlinex,auxliney,":")
plt.xlabel("Temperature(℃)")
plt.ylabel("Energy(J)")




plt.show()