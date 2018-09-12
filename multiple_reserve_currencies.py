from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
S0=10000
R10=10
R20=60
CW1=0.08
CW2=0.11
R1 = np.arange(1, 600, 8)
R2 = np.arange(1, 600, 8)
R1, R2 = np.meshgrid(R1, R2)
S = S0*(R1/R10)**CW1*(R2/R20)**CW2
plt.title("Supply - 2 Reserves")
ax.set_xlabel('R1 CW='+str(round(CW1*100,2))+'%', color='r')
ax.set_ylabel('R2 CW='+str(round(CW2*100,2))+'%', color='g')
ax.set_zlabel('Supply', color='b')
ax.plot_surface(R1, R2, S, rstride=1, cstride=1, cmap=plt.cm.coolwarm)
plt.show()
