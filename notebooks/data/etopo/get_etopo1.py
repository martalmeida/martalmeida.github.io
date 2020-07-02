#f='http://oos.soest.hawaii.edu/thredds/dodsC/etopo5'
f='http://www.ngdc.noaa.gov/thredds/dodsC/relief/ETOPO1/thredds/ETOPO1_Ice_g_gmt4.nc'

from okean import netcdf, calc
import numpy as np


def get(xlim,ylim):
  x=netcdf.use(f,'lon')
  y=netcdf.use(f,'lat')
  i0,i1,j0,j1=calc.ij_limits(x,y,xlim,ylim)

  ix='%d:%d'%(i0,i1)
  iy='%d:%d'%(j0,j1)

  x=netcdf.use(f,'lon',lon=ix)
  y=netcdf.use(f,'lat',lat=iy)
  z=netcdf.use(f,'z',lon=ix,lat=iy)

  x,y=np.meshgrid(x,y)
  np.savez('etopo1_madeira.npz',x=x,y=y,z=z)



'''
f='etopo1_ice_drake.nc'
nc=netcdf.ncopen(f)
x=netcdf.use(nc,'lon')
y=netcdf.use(nc,'lat')
z=netcdf.use(nc,'Band1')
x,y=np.meshgrid(x,y)
np.savez('etopo1_drake.npz',x=x,y=y,z=z)
'''
'''

xlim=-90+360,-20+360
ylim=-75,-45

xlim=-80,-69
ylim=-69,-38

i0,i1,j0,j1=calc.ij_limits(x,y,xlim,ylim)
ix='%d:%d'%(i0,i1)
iy='%d:%d'%(j0,j1)

x=netcdf.use(nc,'lon',ETOPO05_X=ix)-360
y=netcdf.use(nc,'lat',ETOPO05_Y=iy)
z=netcdf.use(nc,'z',ETOPO05_X=ix,ETOPO05_Y=iy)
nc.close()

x,y=np.meshgrid(x,y)
np.savez('etopo1_drake.npz',x=x,y=y,z=z)
'''
