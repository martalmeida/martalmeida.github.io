from okean import roms
import pylab as pl

his='ocean_his.nc'
grd='ocean_grd.nc'

r=roms.His(his)
t,z,v=r.time_series('salt',-91.5,29.25,depth=-5)

pl.figure(figsize=(8,4.85))
ax=pl.axes()
ax.plot(r.datetime,v)

import matplotlib.dates as mdates
months = mdates.MonthLocator()
fmt=mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(fmt)

pl.savefig('ex_roms_09.png',dpi=50)
