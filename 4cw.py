import numpy as np
import matplotlib.pyplot as plt
import random

slista=[]
blista=[]
plista=[]
splista=[]
jlist=[0,1,2,3]
cwlist=[0.05, 0.075, 0.08, 0.1]
totalyr=3

for j in jlist: 
	slista.append([])
	blista.append([])
	plista.append([])
	splista.append([])
	s0=4.96*10**8
	mtop=10*10**8
	stop=10**9-s0
	oneday=24*60*60
	oneyear=365
	t=[i for i in range(1,oneyear*2*totalyr)] 
	bprice=bprice0=45
	bprice=bprice0
	b0=bnum0=10**6
	realmine=0
	cw=cwlist[j]
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
	buymoney=sellmoney=0
	staked=0
	toBP=0.5

	for i in t:
		l=(i/2)/(oneyear*8+2)
		stakeperday=4*10**5
		if staked<s:
			if s>stakeperday:
				staked+=stakeperday
				s-=stakeperday
		elif staked>stakeperday/2:
			staked-=stakeperday/2
			s+=stakeperday/2
		mineperhalfday=(1.0*dotpersec/(2**l))*oneday/2
		if allmine+mineperhalfday>mtop:
			realmine=mtop-allmine
		else:
			realmine=mineperhalfday
		allmine+=realmine
		s+=realmine
		newprice=b/(cw*s)
		b+=realmine*percentforbancor*0.9*newprice
		newprice=b/(cw*s)
		bprice=bprice0*random.uniform(0.88,1.15)
		if i%30==0:
			buymoney=bprice*1050000.0
			sellmoney=bprice*50000.0
		elif i%31==0:
			buymoney=bprice*800000.0
			sellmoney=buymoney*random.uniform(0.9,1.78)
		elif newprice>1.05:
			buymoney=bprice*110000.0
			sellmoney=buymoney*random.uniform(0.91,2.1)
		else:
			buymoney=bprice*130000.0
			sellmoney=buymoney*random.uniform(0.8,1.1)
		buy=buymoney*1.0/bprice
		if buy<=0:
			blista[j].append(b/10**6)
			slista[j].append(s/10**6)
			plista[j].append(newprice)
			splista[j].append((s0+stop+allmine)*newprice*bprice/10**9)
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
			#tokentobp=realtoken*feerate*toBP
			#newprice=realbuybeforerate/realtoken
			newprice=b/(cw*s)
			blista[j].append(b/10**6)
			slista[j].append(s/10**6)
			plista[j].append(newprice)
			splista[j].append((s0+stop+allmine)*newprice*bprice/10**9)
		else:#sell
			sell=sellmoney/bprice/newprice
			sell*=1-feerate*toBP
			#btcdownmaybe=random.uniform(0.33,3)	
			#if btcdownmaybe>0.8 and btcdownmaybe<1.0:
			#	sell=sell*3	
			#	bprice*=0.5
			if sell>s:
				realsell=s
			else:
				realsell=sell
			e=b*(1-(1-realsell/s)**(1/cw))
			if b<e:
				newprice=b/(cw*s)
				blista[j].append(b/10**6)
            	   		slista[j].append(s/10**6)
               			plista[j].append(newprice*10**3)
               			splista[j].append((s0+stop+allmine)*newprice*bprice/10**9)
				continue	
			s-=realsell
			reale=e*(1-feerate*toBP)
			b-=reale
			#if (e>0): 
				#newprice=reale/realsell
			newprice=b/(cw*s)
			blista[j].append(b/10**6)
        		slista[j].append(s/10**6)
			plista[j].append(newprice)
			splista[j].append((s0+stop+allmine)*newprice*bprice/10**9)

colorlist=["red","green","yellow","grey"]
sp=plt.subplot(411)
for j in jlist:
	sp.plot(t,np.array(slista[j]), color=colorlist[j])
bp=plt.subplot(412)
for j in jlist:
	bp.plot(t,np.array(blista[j]), color=colorlist[j])
pp=plt.subplot(413)
for j in jlist:
	pp.plot(t,np.array(plista[j]), color=colorlist[j])
spp=plt.subplot(414)
for j in jlist:
	spp.plot(t,np.array(splista[j]), color=colorlist[j])
plt.legend()
pp.set_title("Price-1/2Day")
pp.set_ylabel("EOS")
p0=b0/(cwlist[0]*s0)
p3=b0/(cwlist[3]*s0)
ibo0=p0*1.8*10**8
ibo3=p3*1.8*10**8
sp.set_title("cw="+str(round(cwlist[0]*100,1))+"%-"+str(round(cwlist[3]*100,1))+"% rate="+str(round(100*percentforbancor,1))+"% fee="+str(round(100*feerate,1))+"%("+str(round(toBP*100,1))+"% to BP)\nIBO:"+str(round(ibo0/10**6,2))+"mEOS/Reserve:"+str(round(b0/ibo0*100,2))+"%-"+str(round(ibo3/10**6,2))+"mEOS/Reserve:"+str(round(b0/ibo3*100,2))+"%\nSupply-1/2Day")
sp.set_ylabel("mDOT")
bp.set_title("Reserve-1/2Day")
bp.set_ylabel("mEOS")
spp.set_title("Market Cap-1/2Day")
spp.set_ylabel("bRMB")
plt.tight_layout()
plt.show()
