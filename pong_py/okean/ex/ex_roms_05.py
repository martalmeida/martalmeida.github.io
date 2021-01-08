from okean import roms, pl_tools
import pylab as pl

his='ocean_his.nc'
grd='ocean_grd.nc'

r=roms.His(his)
x,y,z,v=r.slicei('salt',50,0,dist=0)

pl.figure()
ax=pl.axes()
p=ax.contourf(y,z,v)
pl.colorbar(p)
pl.axis([28,29.5,-200,1])

pl.savefig('ex_roms_05.png',dpi=50)
