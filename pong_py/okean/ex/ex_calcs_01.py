from okean import calc, hull
import numpy as np
import pylab as pl

np.random.seed(0)
x=np.random.rand(100)
y=np.random.rand(100)

pl.figure()
pl.plot(x,y,'bo')

# concave/convex hull:
i=hull.convex_hull(x,y)
pl.plot(x[i],y[i],'r-x')

j=hull.concave_hull(x,y)
pl.plot(x[j],y[j],'b-s')

pl.gca().set_frame_on(0)
pl.gca().set_xticks([])
pl.gca().set_yticks([])

# centroid and area:
x0,y0=calc.poly_centroid(x[i],y[i])
pl.plot(x0,y0,'r+',ms=16)
print x0,y0,calc.poly_area(x[i],y[i])

x0,y0=calc.poly_centroid(x[j],y[j])
pl.plot(x0,y0,'bx',ms=16)
print x0,y0,calc.poly_area(x[j],y[j])

# in polygon:
xp=0.2,0.8,0.2
yp=0.3,0.6,0.8
i=calc.inpolygon(x,y,xp,yp)
pl.plot(xp+(xp[0],),yp+(yp[0],),'r')
pl.plot(x[i],y[i],'o',ms=15,mfc='none',mec='r')

pl.savefig('ex_calcs_01.png',dpi=50)

