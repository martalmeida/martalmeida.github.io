from okean import calc, hull
import numpy as np
import pylab as pl

np.random.seed(1)
x=np.random.rand(20)
y=np.random.rand(20)

np.random.seed(3)
x1=np.random.rand(10)
y1=np.random.rand(10)

pl.figure()
pl.plot(x,y,'b')
pl.plot(x1,y1,'k')

xi,yi=calc.meetpoint(x,y,x1,y1)

pl.plot(xi,yi,'ro')

pl.gca().set_frame_on(0)
pl.gca().set_xticks([])
pl.gca().set_yticks([])

pl.savefig('ex_calcs_02.png',dpi=50)

