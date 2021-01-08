from okean import roms, pl_tools
import pylab as pl

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

x,y,z,v=r.slicez('salt',-50,0)
x,y=m(x,y)
pl.figure(figsize=(8,4.85))
ax=pl.axes()
p=ax.contourf(x,y,v)
pl.colorbar(p,orientation='horizontal',pad=0.075)

draw_map(m,ax)
pl.savefig('ex_roms_03.png',dpi=50)
