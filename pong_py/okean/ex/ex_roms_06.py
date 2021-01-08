from okean import roms
import pylab as pl
from mpl_toolkits.basemap import cm
import numpy as np

his='ocean_his.nc'
grd='ocean_grd.nc'

r=roms.His(his)
m=r.grid.plot(title='',xlim=[-95,-87.5],bathy=False)

x=np.linspace(-92.,-88,50)
y=np.linspace(28.,30,50)
xx,yy=m(x,y)
pl.plot(xx,yy,'r')
pl.savefig('ex_roms_06a.png',dpi=50)

dist,z,v=r.slicell('salt',x,y,0,dist=True)
pl.figure()
pl.pcolormesh(dist/1000.,z,v,vmin=30,vmax=37.5,cmap=cm.GMT_no_green)
pl.colorbar()
pl.savefig('ex_roms_06b.png',dpi=50)
