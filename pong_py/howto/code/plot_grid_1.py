import pylab as pl
from okean import roms

roms.Grid('roms_grd.nc').plot()
pl.show()
