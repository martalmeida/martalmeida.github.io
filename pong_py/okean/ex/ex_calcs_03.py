from okean import calc, hull
import numpy as np
import pylab as pl

pl.figure()
ax=pl.subplot(131)
ax1=pl.subplot(132)
ax2=pl.subplot(133)

x=np.linspace(-10,10,15)
y=np.linspace(-7,7,15)
x,y=np.meshgrid(x,y)
v=x**2+y**2
v=np.ma.masked_where(v<5,v)

x1=np.linspace(-7,12,30)
y1=np.linspace(-5,5,25)
x1,y1=np.meshgrid(x1,y1)
v1=calc.griddata(x,y,v,x1,y1)
v1e=calc.griddata(x,y,v,x1,y1,extrap=True)

ax.pcolormesh(x,y,v)

ax1.plot(x,y,'k')
ax1.plot(x.T,y.T,'k')
ax1.pcolormesh(x1,y1,v1)

ax2.plot(x,y,'k')
ax2.plot(x.T,y.T,'k')
ax2.pcolormesh(x1,y1,v1e)


pl.savefig('ex_calcs_03.png',dpi=50)

