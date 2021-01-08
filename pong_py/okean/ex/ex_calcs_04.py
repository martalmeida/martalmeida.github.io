from okean import ticks, roms
import pylab as pl
from mpl_toolkits.basemap import cm

# loose label example:
print ticks.loose_label(105,543)
# returns [ 100.  200.  300.  400.  500.  600.]

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
m=proj([-90.25,-88.5],[28.5,30])

x,y,z,v=r.slicek('salt',-1,0)
x,y=m(x,y)


pl.figure()
ax=pl.axes()
vals=ticks.loose_label(v.mean()-v.std(),v.mean()+v.std(),10)
p=ax.contourf(x,y,v,vals,cmap=cm.s3pcpn,extend='both')
c=pl.colorbar(p)
p2=ax.contour(p,levels=p.levels[::2],colors='g')
c.add_lines(p2)

draw_map(m,ax)
meridians=ticks.loose_label(m.llcrnrlon,m.urcrnrlon)
m.drawmeridians(meridians, labels=[0,0,0,1],ax=ax,color='r',fontdict={'color':'b'})

pl.savefig('ex_calcs_04.png',dpi=50)


