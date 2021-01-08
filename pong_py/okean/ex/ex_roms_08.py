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

v=r.use('salt',ocean_time=200)
z=r.s_levels(time=10)
d=roms.roms_tools.depthof(v,z,30)
x,y=m(r.grid.lon,r.grid.lat)

pl.figure(figsize=(8,4.85))
ax=pl.axes()
p=ax.pcolormesh(x,y,d,cmap=pl.cm.BuPu_r)
pl.colorbar(p,orientation='horizontal',pad=0.075)

draw_map(m,ax)
pl.savefig('ex_roms_08.png',dpi=50)
