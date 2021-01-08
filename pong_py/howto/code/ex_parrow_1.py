import numpy as np
import pylab as pl
from okean import pl_plots as pp

r = np.arange(0,1,0.01)
teta=4.5*np.pi*r
y = r*np.sin(teta)
x = r*np.cos(teta)

def add_colorbar(a,m):
  q=a.get_position()
  cx=pl.axes((q.x0+q.width*.92,q.y0,q.width/20.,q.height))
  pl.colorbar(m,cax=cx)
  pl.setp(cx.get_yticklabels(),fontsize=8)


fig=pl.figure(figsize=(6,8))
ax=[fig.add_subplot(3,2,i+1) for i in range(6)]
[a.set_aspect('equal') for a in ax]
pl.subplots_adjust(left=0.04)

p=pp.parrow(x,y,ax=ax[0])

p,m=pp.parrow(x,y,ax=ax[1],cmap=pl.cm.RdYlBu,C=x)
add_colorbar(ax[1],m)

p,m=pp.parrow(x,y,ax=ax[2],cmap=pl.cm.jet,d=-1)
add_colorbar(ax[2],m)

p,m=pp.parrow(x,y,ax=ax[3],cmap=pl.cm.jet,d=-1,norm=pl.matplotlib.colors.LogNorm)
add_colorbar(ax[3],m)

p,m=pp.parrow(x,y,ax=ax[4],cmap=pl.cm.jet,d=-1,norm=pl.matplotlib.colors.LogNorm,
              head_angle=0,n=2)

p=pp.parrow(x,y,ax=ax[5],color='b',lw=2,d=2,n=6,head_angle=10)

for a in ax:
  a.set_aspect('equal')
  a.axis([-1.,1.,-.9,1.1])
