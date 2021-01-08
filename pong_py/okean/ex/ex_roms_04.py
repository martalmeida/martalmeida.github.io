from okean import roms, pl_tools
import pylab as pl
import numpy as np

def proj(xlim,ylim):
  from mpl_toolkits.basemap import Basemap
  return Basemap(projection='merc',
               resolution='h',
               llcrnrlat=ylim[0],
               llcrnrlon=xlim[0],
               urcrnrlat=ylim[1],
               urcrnrlon=xlim[1],
               lat_ts=0.0)


def draw_map(m,ax):
  m.fillcontinents(color='#f2f2f8',ax=ax)
  m.drawcountries(color='#cccccc',ax=ax)
  m.drawstates(color='#cccccc',ax=ax)
  m.drawcoastlines(color='#cccccc',ax=ax)


his='ocean_his.nc'
grd='ocean_grd.nc'

r=roms.His(his)
m=proj([r.grid.lon.min(),r.grid.lon.max()],
       [r.grid.lat.min(),r.grid.lat.max()])

x,y,z,u,v=r.sliceuv('surface',0)
x,y=m(x,y)
pl.figure(figsize=(8,4.85))
ax=pl.axes()
M=np.zeros(x.shape,'bool')
M[::3,::3]=True
p=pl.quiver(x[M],y[M],u[M],v[M],scale=20,width=.001,color='b')
pl.quiverkey(p,.85,.07,0.5,'0.5 m s$^{-1}$')

draw_map(m,ax)
pl.savefig('ex_roms_04.png',dpi=50)
