import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from pylab import meshgrid,cm,imshow,colorbar

def LeapFrog(func, eps=0.0001, bounds=3 , delay=0.01, iterations=3000, printV=False, draw=True):
	plt.figure()

	players = (2*np.random.rand(20,2)-1)*bounds
	x= np.arange(-bounds, bounds, 0.01)
	y= np.arange(-bounds, bounds, 0.01)
	X,Y = meshgrid(x, -y)
	Z = func(X, Y)
	im = plt.imshow(Z,cmap=cm.RdBu,extent=[-bounds, bounds, -bounds, bounds])
	points, =plt.plot(players[:,0],players[:,1],'yo', marker='x')
	colorbar(im) 

	for i in range(1,iterations):
		z=func(players[:,0], players[:,1])
		maxZ=np.argmax(z)
		minZ = np.argmin(z)
		r = np.random.rand(1,2)
		players[maxZ, :]=players[minZ, :]-r*(players[maxZ, :]-players[minZ, :])
		if(abs(z[maxZ]-z[minZ])<eps):
			if(printV):
				print("Minimum at: {0}".format(players[minZ,:]))
			return players[minZ,:];
		if(printV):
			print([z[minZ], players[minZ,:]])
		points.set_xdata(players[:,0])
		points.set_ydata(players[:,1])
		if(draw):
			plt.pause(delay)
			plt.draw()
