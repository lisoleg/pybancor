import numpy as np
import matplotlib.pyplot as plt

s0=486000000
pool=10**9-s0
oneday=24*60*60
oneyear=365
t=[i for i in range(0,oneyear*60,1)] 
bprice=43000
b0=bprice*1000
cw=0.075
allmine=0
plist=[]
newb=b0
percentforbancor=0.08
dotpersec=2
s=s0
b=b0
for i in t:
	l=i/(365*4+1)+1
	mineperday=(1.0*dotpersec/l)*oneday
	if allmine>pool:
		mineperday=0
	allmine+=mineperday
        b+=mineperday*percentforbancor*(b/(cw*s))
        s+=mineperday	
	plist.append(b/(cw*s))
p=np.array(plist)
plt.plot(t,p,color="red",linestyle="--",marker="*",label='price')
plt.savefig("1.png",dpi=60)
plt.legend()
plt.title("Price-Day")
plt.xlabel("day")
plt.ylabel("price")
plt.show()
