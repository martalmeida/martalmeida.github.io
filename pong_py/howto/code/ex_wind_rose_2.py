import numpy as np
import pylab as pl
import datetime
from okean import pl_plots, netcdf

f='http://barataria.tamu.edu:8080/thredds/dodsC/mch_forcing_2005/mch_blk_narr_2005.nc'
t=netcdf.nctime(f,'time')
date0=datetime.datetime(t[0].year,8,1)
cond=t>date0
u=netcdf.use(f,'Uwind',xi_rho=100,eta_rho=50,time=cond)
v=netcdf.use(f,'Vwind',xi_rho=100,eta_rho=50,time=cond)
vel=u+1j*v
pl.figure()
pl_plots.wind_rose(np.angle(vel)*180/np.pi,np.abs(vel),
                   title='NARR wind near Mississippi Aug..Dec 2005',
                   legend='Intensity (m$\cdot$s$^{-1}$)')
