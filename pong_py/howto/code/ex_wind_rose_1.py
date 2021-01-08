import numpy as np
import pylab as pl
from okean import pl_plots

d=np.arange(0,360,10)
D=np.array(())
V=np.array(())
for i in range(len(d)):
  n=d[i]/10.
  D=np.append(D,np.ones(n)*d[i])
  V=np.append(V,np.arange(n))

fig0=pl.figure()
pl_plots.wind_rose(D,V)

fig1=pl.figure()
ax0=pl.axes()
ax1=fig1.add_axes((.5,.5,.4,.4))
ax2=fig1.add_axes((.1,.05,.5,.5))

from mpl_toolkits.basemap import Basemap
m=Basemap(resolution='l',urcrnrlon=-60,urcrnrlat=50,llcrnrlon=-130,llcrnrlat=0)
m.drawcoastlines(ax=ax0)

d=np.arange(0,360)
v=d*0+1
pl_plots.wind_rose(d,v,ax=ax1,bg=None)
pl_plots.wind_rose(D,V,ax=ax2,bg=None,cmap=pl.cm.gist_ncar)
