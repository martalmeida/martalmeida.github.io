from okean import roms, netcdf, pl_tools, pl_plots
import pylab as pl
import numpy as np

pl.ion()

his='ocean_his.nc'
grd='ocean_grd.nc'

r=roms.His(his)

r.grid.plot(title='',xlim=[-95,-87.5])
pl.savefig('fig_roms_00png',dpi=50)


def proj(xlim,ylim):
  from mpl_toolkits.basemap import Basemap
  return Basemap(projection='merc',
               resolution='h',
               llcrnrlat=ylim[0],
               llcrnrlon=xlim[0],
               urcrnrlat=ylim[1],
               urcrnrlon=xlim[1],
               lat_ts=0.0)

def go():
 # slices: ----------------------------------- > his, avg, clm !!
 m=proj([r.grid.lon.min(),r.grid.lon.max()],
        [r.grid.lat.min(),r.grid.lat.max()])

 # superficie:
 x,y,z,v=r.slicek('temp',-1,0)
 x,y=m(x,y)

 pl.pcolormesh(x,y,v)
 pl.colorbar()

 m.drawcoastlines()
 pl.savefig('fig0.png')


#
x,y,z,v=r.slicez('salt',-200,0)
x,y=m(x,y)
pl.figure()
pl.pcolormesh(x,y,v)
pl.colorbar()
m.fillcontinents(color='#f2f2f8')
m.drawcountries(color='#cccccc')
m.drawcoastlines(color='#cccccc')
pl.savefig('fig1.png',dpi=50)


q=pl.quiver(x[M],y[M],u[M],v[M],scale=20,width=.001)
m.drawcoastlines(color=(0,.5,.5))
pl.quiverkey(....
pl.savefig('fig2.png',dpi=50)



 # fundo:
 x,y,z,v=r.slicek('temp',-1,0)
 pl.pcolormesh(x,y,v)
 pl.colorbar()

 # eta const:
 dist,z,v=r.slicej('salt',100,10)
 pl.pcolormesh(dist/1000.,z,v)
 pl.colorbar()

 x,y,z,v=r.slicej('salt',100,10,dist=False)
 pl.pcolormesh(x,z,v)
 pl.colorbar()

 # xi const:
 dist,z,v=r.slicei('temp',100,10)
 pl.pcolormesh(dist/1000.,z,v)
 pl.colorbar()

 # any path:
 x=np.linspace(-90,-78,100)
 y=np.linspace(-4,0,100)
 dist,z,v=r.slicell('temp',x,y,0,dist=True)
 pl.pcolormesh(dist/1000.,z,v)
 pl.colorbar()


 # any path interactive !
 pl.pcolormesh(r.grid.lon,r.grid.lat,r.grid.h)
 pl.contour(r.grid.lon,r.grid.lat,r.grid.h,[200,1000,2000],colors='w')
 pl.contour(r.grid.lon,r.grid.lat,r.grid.mask,[.5],colors='g',linewidths=2)

 i=pl_tools.InteractiveLine()
 pl.figure()
 dist,z,v=r.slicell('temp',i.xx,i.yy,0,dist=True)
 pl.pcolormesh(dist/1000.,z,v)
 pl.colorbar()


 # depthof
 v=r.use('salt',ocean_time=10)
 z=r.s_levels(time=10)
 print v.shape, z.shape
 d=roms.roms_tools.depthof(v,z,33.6)

 pl.pcolormesh(r.grid.lon,r.grid.lat,d)
 pl.contour(r.grid.lon,r.grid.lat,r.grid.mask,[.5],colors='g',linewidths=2)
 pl.colorbar()


 # time series:
 dtime=r.datetime
 t,z,v=r.time_series('temp', x=-85, y=0)
 pl.pcolormsh(t,z,v)
 pl.colorbar()



 # ------------------------------------------- pl_plots:
 # wind rose:
 d=np.arange(0,360,10)
 D=np.array(())
 V=np.array(())
 for i in range(len(d)):
   n=d[i]/10.
   D=np.append(D,np.ones(n)*d[i])
   V=np.append(V,np.arange(n))
    
 pl_plot.wind_rose(D,V)

 # ellipse:
 x = np.linspace(1,100,8)
 y = np.linspace(1,100,10)
 x,y = np.meshgrid(x,y)
 major = (x+y)/30.
 minor = np.sqrt(x+y)/10.
 inc   = x/2.
 phase = y
     
 pl_plots.plot_ellipse(x,y,major,minor,inc,phase)

# hycom, iasnfs, etc
# ini, clm, bry
# bulk surface forcing: ecmwd, narr, gfs, ncep ...
# rivers forcing file
#
# netcdf, grib , opendap access ...
