import numpy as np
import matplotlib.pyplot as plt

r0=1000.0
e=[i for i in range(1,4000)] 
cw=0.08
plist=[]
for i in e:
	plist.append(cw*i/(2*r0*((1+i/r0)**cw-1)))
p=np.array(plist)
plt.plot(e,p,color="red",linestyle="--",marker="*",label='')
plt.legend()
plt.title("pay-slippage")
plt.xlabel("pay")
plt.ylabel("slippage")
plt.show()
