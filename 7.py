import numpy as np
import matplotlib.pyplot as plt
import random
#Bancor whitepaper sell formula is wrong and walletrade whitepaper is good
s0=4.96*10**8
mtop=5*10**8
stop=5.04*10**8
oneday=24*60*60
oneyear=365
t=[i for i in range(1,oneyear*2*5)] 
bprice0=6.4669
bprice=bprice0
bnum0=1000000
b0=bnum0
cw=0.075
realmine=0
plist=[]
blist=[]
slist=[]
splist=[]
b=b0*1.0
p0=b0/(cw*s0)
percentforbancor=0.08
dotpersec=2
s=1.0*s0
newprice=p=p0
sp=s0*p0
feerate=0.05
allmine=0
for i in t:
	l=(i/2)/(365*4+1)
	mineperhalfday=(1.0*dotpersec/(2**l))*oneday/2
	if allmine+mineperhalfday>mtop:
		realmine=mtop-allmine
	else:
		realmine=mineperhalfday
	allmine+=realmine
	s+=realmine
	newprice=b/(cw*s)
	b+=realmine*percentforbancor*newprice
	newprice=b/(cw*s)
	#bprice*=bprice0*random.uniform(0.9,1.2)
	if i<365:
		buymoney=1000000.0
	else:
		buymoney=(i*1.0/2)/365*2000000.0
	buy=buymoney*1.0/bprice
	if buy<=0:
		blist.append(b/10**6)
		slist.append(s/10**6)
		plist.append(newprice*10**3)
		splist.append((s0+stop+allmine)*newprice*bprice/10**9)
		continue
	if i%2==0:#buy
		fee=buy*feerate	
		realbuybeforerate=buy
		buyafterrate=buy-fee	
		token=-1*s*(1-(1+buyafterrate/b)**cw)	
		nowtop=s0+allmine+stop
		if (s+token>nowtop):
			realtoken=nowtop-s
			realbuybeforerate=-1*b*(1-(1+realtoken/s)**(1/cw))
			fee=realbuybeforerate*feerate
			realbuy=realbuybeforerate-fee
			realtoken=-1*s*(1-(1+realbuy/b)**cw)
		else:
			realtoken=token
			realbuy=buyafterrate
		s+=realtoken	
		b+=realbuybeforerate
		#newprice=realbuybeforerate/realtoken
		newprice=b/(cw*s)
		blist.append(b/10**6)
		slist.append(s/10**6)
		plist.append(newprice*10**3)
		splist.append((s0+stop+allmine)*newprice*bprice/10**9)
	else:#sell
		if i<365*2:
			sell=50000*random.uniform(0,2)
		else:
			sell=buymoney/bprice/newprice*random.uniform(0.01,2.88)
		if newprice<bprice0*0.01:
			 sell=0.1*buymoney/bprice/newprice
		btcdownmaybe=0#random.uniform(0.33,3)	
		if btcdownmaybe>0.8 and btcdownmaybe<1.0:
			sell=sell*3	
			bprice*=0.5
		if sell>s:
			realsell=s
		else:
			realsell=sell
		e=b*(1-(1-realsell/s)**(1/cw))
		if b-2500000<e:
			newprice=b/(cw*s)
			blist.append(b/10**6)
                	slist.append(s/10**6)
                	plist.append(newprice*10**3)
                	splist.append((s0+stop+allmine)*newprice*bprice/10**9)
			continue	
		s-=realsell
		reale=e*(1-feerate)
		b-=reale
		#if (e>0): 
			#newprice=reale/realsell
		newprice=b/(cw*s)
		blist.append(b/10**6)
                slist.append(s/10**6)
		plist.append(newprice*10**3)
		splist.append((s0+stop+allmine)*newprice*bprice/10**9)
sp=plt.subplot(411)
sp.plot(t,np.array(slist))
bp=plt.subplot(412)
bp.plot(t,np.array(blist))
pp=plt.subplot(413)
pp.plot(t,np.array(plist))
spp=plt.subplot(414)
spp.plot(t,np.array(splist))
plt.legend()
pp.set_title("Price-Day")
pp.set_ylabel("10^-3EOS")
sp.set_title("Supply-Day cw="+str(cw)+" rate="+str(percentforbancor)+" fee="+str(feerate))
sp.set_ylabel("mDOT")
bp.set_title("Reserve-Day")
bp.set_ylabel("mEOS")
spp.set_title("Market Cap-Day")
spp.set_xlabel("1/2day")
spp.set_ylabel("bUSDT")
plt.tight_layout()
plt.show()
