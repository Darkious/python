import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
import random
##arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
##old_values=arr3d[0].copy()
##names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
##data=randn(7,4)
##print(data)
##data[names =='Bob',:2]
##arr=np.empty((8,4))
##for i in range(8):
##    arr[i]=i
############################################
##points=np.arange(-5,5,0.01)
##xs,ys=np.meshgrid(points,points)
##z=np.sqrt(xs**2+ys**2)
##plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()
##plt.show()
############################################
##xarr=np.array([1.1,1.2,1.3,1.4,1.5])
##yarr=np.arange(2.1,2.6,0.1)
##cond=np.array([True,False,True,True,False])
##result=np.where(cond,xarr,yarr)
##arr=np.ones([5,4])
############################################
##x=np.array([[1,2,3],[4,5,6]])
##y=np.array([[6,23],[-1,7],[8,9]])
############################################
##position = 0
##walk=[position]
##steps=1000
##for i in range(steps):
##    step = 1 if random.randint(0,1) else -1
##    position +=step
##    walk.append(position)
############################################
nwalks=5000
nsteps = 1000
#draws = np.random.randint(0,2,size=(nwalks,nsteps))
draws = np.random.normal(loc=0,scale=2,size=(nwalks,nsteps))
steps = np.where(draws>0,1,-1)
walk = steps.cumsum(1)
hits30 = (np.abs(walk) >=30).any(1)
crossing_times = (np.abs(walk[hits30])>=30).argmax(1)
print(crossing_times.mean())


