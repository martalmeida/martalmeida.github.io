from okean import roms, pl_tools
import pylab as pl
import numpy as np

his='ocean_his.nc'
grd='ocean_grd.nc'

r=roms.His(his)
pl.ion()
m=r.grid.plot(title='',xlim=[-95,-87.5],bathy=False)

i=pl_tools.InteractiveLine()
x,y=m(i.xx,i.yy,True)
pl.savefig('ex_roms_07a.png',dpi=50)

dist,z,v=r.slicell('salt',x,y,0,dist=True)
pl.figure()
pl.pcolormesh(dist/1000.,z,v,vmin=30,vmax=37.5)
pl.colorbar()
pl.savefig('ex_roms_07b.png',dpi=50)
