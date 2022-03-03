# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d
import scipy.interpolate as spi

"temperature"
x = np.array([-195,-80,-20,0,200]) 
"energy/percentage crystallinity"
y = np.array([100,100,90,10,0])  

"interpolation"
#using akima 1d interpolation
X_Y_Spline = spi.Akima1DInterpolator(x, y)
#using cubic spline interpolation
X_Y_Spline = make_interp_spline(x, y,k=3)
cubic_interploation_model = interp1d(x, y, kind = "cubic")

X_ = np.linspace(x.min(), x.max(), 1000)
Y_ = X_Y_Spline(X_)
plt.plot(X_, Y_)

"you can plot without interpolation"
plt.plot(x,y)

"finding intersection"
avg=(np.min(y)+np.max(y))/2
lx=np.linspace(-195,200,1000)
#"this is for fracture energy"
ly=np.array([avg]*1000) 
#"this is for percentage crystallinity"
ly=np.array([50]*1000) 

idx = np.argwhere(np.diff(np.sign(Y_-ly))).flatten()
plt.plot(X_[idx], ly[idx],'ro')
print(lx[idx]) #finding x point of intersection


"construction lines"

plt.plot(lx,ly,":")
auxliney=np.arange(0,200)
auxlinex=np.array([lx[idx]]*200)
plt.plot(auxlinex,auxliney,":")
plt.xlabel("Temperature(℃)")
plt.ylabel("Percentage crystallinty")

"controlling yaxis limits"
ax=plt.gca()
ax.set_ylim([0, 200])

plt.show()
