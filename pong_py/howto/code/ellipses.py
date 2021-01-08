from okean.pl_plots import plot_ellipse
import pylab as pl
import numpy as np

x = np.linspace(1,100,8)
y = np.linspace(1,100,10)
x,y = np.meshgrid(x,y)
major = (x+y)/30.
minor = np.sqrt(x+y)/10.
inc   = x/2.
phase = y

pl.figure()
ax0=pl.subplot(2,2,1)
ax1=pl.subplot(2,2,2)
ax2=pl.subplot(2,2,3)
ax3=pl.subplot(2,2,4)

# several types of ellipses:
opts=dict(color='g',marker=dict(color='r',marker='o',ms=5))
plot_ellipse(0,0,1,   0.5,30, 90,type=2,ax=ax0,**opts)
plot_ellipse(0,0,1,   0.5,80, 10,type=1,ax=ax0,color='b')
plot_ellipse(0,0,0.7, 0.3,80, 10,type=4,ax=ax0,color='r')
plot_ellipse(0,0,0.2, 0.1, 0,  0,type=3,ax=ax0,color='k')
plot_ellipse(0,0,0.25,0.25,0,-30,type=0,ax=ax0,color='c')

# ellipses field:
plot_ellipse(x,y,major,minor,inc,phase,ax=ax1)

# ellipses field, color according to major axis:
r=plot_ellipse(x,y,major,minor,inc,phase,ax=ax2)

cNorm  = pl.matplotlib.colors.Normalize(vmin=major.min(), vmax=major.max())
scalarMap = pl.cm.ScalarMappable(norm=cNorm, cmap=pl.cm.jet)
colors=[scalarMap.to_rgba(i) for i in major.flat]

for i in range(major.size):
  r[i]['line'].set_color(colors[i])

# filled ellipses:
r2=plot_ellipse(x,y,major,minor,inc,phase,ax=ax3,lw=.5,
                fill={'facecolor':'none','alpha':.3})
for i in range(major.size):
  r2[i]['fill'].set_facecolor(colors[i])

# colorbar:
cbax=pl.axes((.92,.1,.02,.3))
scalarMap._A = []
cb=pl.colorbar(scalarMap,cax=cbax,alpha=.3)
# same as:
#pl.matplotlib.colorbar.ColorbarBase(cbax, cmap=jet,norm=cNorm,
#                                    orientation='vertical',alpha=.3)
