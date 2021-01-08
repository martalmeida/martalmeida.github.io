from okean import roms
import pylab as pl

his='ocean_his.nc'
grd='ocean_grd.nc'

r=roms.His(his,grd)

z_r=r.s_levels(time=100,ruvpw='r',i=50,j=20)
z_w=r.s_levels(time=100,ruvpw='w',i=50,j=20)

pl.figure()
for z in z_w:
  pl.plot([-1,1],[z,z],'b')

pl.plot(0*z_r,z_r,'ro')
pl.xlim(-5,5)
pl.ylim(z_w.min()-3,z_w.max()+3)
pl.text(0,z_w.min()-2,'bottom, h',ha='center')
pl.text(0,z_w.max()+.5,'zeta',ha='center')
pl.gca().set_xticks([])

pl.savefig('ex_roms_10.png',dpi=50)
