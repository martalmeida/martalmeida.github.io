from okean import roms
import pylab as pl

his='ocean_his.nc'
grd='ocean_grd.nc'

r=roms.His(his)
r.grid.plot(title='',xlim=[-95,-87.5])
pl.savefig('ex_roms_01.png',dpi=50)
