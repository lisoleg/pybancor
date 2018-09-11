import numpy as np
import matplotlib.pyplot as plt
import random

s0=4.96*10**8
mtop=5.04*10**8
oneday=24*60*60
oneyear=365
t=[i for i in range(1,oneyear*30)] 
bprice0=6.4669
bprice=bprice0
bnum0=1000000
b0=1.0*bnum0
cw0=0.065
cw1=0.075
cw2=0.08
cw3=0.1
realmine=0
p0list=[]
b0list=[]
s0list=[]
p1list=[]
b1list=[]
s1list=[]
p2list=[]
b2list=[]
s2list=[]
p3list=[]
b3list=[]
s3list=[]
b=b0
p0=b0/(cw0*s0)
percentforbancor=0.08
dotpersec=2
s=1.0*s0
newprice=p=p0
sp=s0*p0
allmine=0
for i in t:
	l=i/(365*4+1)
	mineperday=(1.0*dotpersec/(2**l))*oneday
	if allmine+mineperday>mtop:
		realmine=mtop-allmine
	else:
		realmine=mineperday
	allmine+=realmine
	s+=realmine
	newprice=b/(cw0*s)
	b+=realmine*percentforbancor*newprice
	newprice=b/(cw0*s)
	b0list.append(b/10**6)
        s0list.append(s/10**6)
	p0list.append(newprice*10**3)
b=b0
s=s0
realmine=allmine=0
for i in t:
        l=i/(365*4+1)
        mineperhalfday=(1.0*dotpersec/(2**l))*oneday
        if allmine+mineperhalfday>mtop:
                realmine=mtop-allmine
        else:
                realmine=mineperhalfday
        allmine+=realmine
        s+=realmine
	newprice=b/(cw1*s)
	b+=realmine*percentforbancor*newprice
        newprice=b/(cw1*s)
        b1list.append(b/10**6)
        s1list.append(s/10**6)
        p1list.append(newprice*10**3)
b=b0
s=s0
realmine=allmine=0
for i in t:
        l=i/(365*4+1)
        mineperhalfday=(1.0*dotpersec/(2**l))*oneday
        if allmine+mineperhalfday>mtop:
                realmine=mtop-allmine
        else:
                realmine=mineperhalfday
        allmine+=realmine
        s+=realmine
	newprice=b/(cw2*s)
	b+=realmine*percentforbancor*newprice
        newprice=b/(cw2*s)
        b2list.append(b/10**6)
        s2list.append(s/10**6)
        p2list.append(newprice*10**3)
b=b0
s=s0
realmine=allmine=0
for i in t:
        l=i/(365*4+1)
        mineperhalfday=(1.0*dotpersec/(2**l))*oneday
        if allmine+mineperhalfday>mtop:
                realmine=mtop-allmine
        else:
                realmine=mineperhalfday
	allmine+=realmine
        s+=realmine
	newprice=b/(cw3*s)
	b+=realmine*percentforbancor*newprice
        newprice=b/(cw3*s)
        b3list.append(b/10**6)
        s3list.append(s/10**6)
        p3list.append(newprice*10**3)
sp=plt.subplot(311)
sp.plot(t,np.array(s0list),color="black")
sp.plot(t,np.array(s1list),color="red")
sp.plot(t,np.array(s2list),color="green")
sp.plot(t,np.array(s3list),color="grey")
bp=plt.subplot(312)
bp.plot(t,np.array(b0list),color="black")
bp.plot(t,np.array(b1list),color="red")
bp.plot(t,np.array(b2list),color="green")
bp.plot(t,np.array(b3list),color="grey")
pp=plt.subplot(313)
pp.plot(t,np.array(p0list),color="black")
pp.plot(t,np.array(p1list),color="red")
pp.plot(t,np.array(p2list),color="green")
pp.plot(t,np.array(p3list),color="grey")
plt.legend()
plt.rcParams['font.sans-serif']=['AR PL UKai CN']
pp.set_title('Price-Day')
pp.set_ylabel("10^-3EOS")
sp.set_title("Supply-Day cw b="+str(cw0)+"/r"+str(cw1)+"/g"+str(cw2)+"/y"+str(cw3)+" rate="+str(percentforbancor))
sp.set_ylabel("mDOT")
bp.set_title("Reserve-Day")
bp.set_ylabel("mEOS")
plt.tight_layout()
plt.show()
