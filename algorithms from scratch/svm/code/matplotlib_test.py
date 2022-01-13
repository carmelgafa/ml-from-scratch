import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

colors = {1:'r', -1:'b'}


data_dict = {-1:np.array([[1,7],[2,8], [3,8], ]),
			1:np.array([[5,1], [6,-1], [7,3], ])}


for i in data_dict:
	for x in data_dict[i]:
		print(x[0], x[1])
		ax.scatter(x[0], x[1], s=100, color=colors[i]) 


plt.show()