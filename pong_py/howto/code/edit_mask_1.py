import pygridgen
from okean import roms
import pylab as pl

grd='roms_grd.nc'

r=roms.Grid(grd)

def save_mask(rmask):
  print 'saving ...'
  u,v,p=pygridgen.uvp_masks(rmask)
  import netCDF4
  nc=netCDF4.Dataset(grd,'a')
  nc.variables['mask_rho'][:]=rmask
  nc.variables['mask_u'][:]=u
  nc.variables['mask_v'][:]=v
  nc.variables['mask_psi'][:]=p
  nc.close()

# cell edges:
xv,yv=pygridgen.rho_to_vert(r.use('x_rho'),r.use('y_rho'),r.pm,r.pn,r.angle)

# start it, manually edit the mask:
e=pygridgen.edit_mask_mesh(xv,yv,r.mask)

# show cells:
ax=pl.gca()
ax.plot(xv,yv,'#f88d01',alpha=.1)
ax.plot(xv.T,yv.T,'#f88d01',alpha=.1)

# save it back to file when figure closes:
fig=pl.gcf()
def close(evt,mask=e.mask): save_mask(mask)
fig.canvas.mpl_connect('close_event', close)

# or save it by hand:
#save_mask(e.mask)

