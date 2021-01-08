import numpy as np
import pylab as pl
from okean import gshhs

x,y=gshhs.get_coastline(xlim=[-15,25],ylim=[36,60],res='h')
pl.plot(x,y)
pl.axis('image')

# you may save it:
fname='my_coastline.npy'
np.ma.vstack((x,y)).dump(fname)

# and load it back:
x,y=np.load(fname)

# or save it as a two columns txt file:
txtfname='my_coastline.txt'
np.savetxt(txtfname,np.ma.vstack((x,y)).T)

# and load it as:
a=np.loadtxt(txtfname).T
x,y=[np.ma.masked_where(a[i]==999.,a[i]) for i in (0,1)]
