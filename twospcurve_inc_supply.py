import numpy as np
import matplotlib.pyplot as plt

s0=4960
step=[i for i in range(1,20000)] 
b0=1000
cw=0.44
p0list=[]
p0=b0/(cw*s0)
for i in step:
        if cw==0:
		price=p0
	elif cw<1:
		price=p0*(i*1.0/s0)**(1/cw-1)	
	else:
		price=p0*(s0*1.0/i)**(1-1/cw)
	#if i>=s0:
	p0list.append(price)
	#else:
	#	p0list.append(0)
	if i==s0:
		plt.plot([i,i],[0,price],color="black")
p1list=[]
s1=s0*1.1
p1=b0/(cw*s1)
for j in step:
	if cw==0:
		price=p1
	elif cw<1:
		price=p1*(j*1.0/s1)**(1/cw-1)
	else:
		price=p1*(s1*1.0/i)**(1-1/cw)
	#if j>=s1:
	p1list.append(price)
	#else:
	#	p1list.append(0)
        if j==s1:
                plt.plot([j,j],[0,price],color="black")
p3=p4=p1*3.3
a=1/(1/cw-1)
if cw==0:
	s3=s0
	s4=s1
elif cw<1:
	s3=s0*(p3/p0)**a
	s4=s1*(p4/p1)**a
else:
	s3=s0*(p0/p3)**(-a)
	s4=s1*(p1/p4)**(-a)
sell=3000
s5=s3-sell
s6=s4-sell
if cw==0:
	p5=p0
	p6=p1
	er=s3*p3
	eb=s4*p4
elif cw<1:
	p5=p0*(s5/s0)**(1/cw-1)
	p6=p1*(s6/s1)**(1/cw-1)
	er=cw*s3*p3*(1-(1-sell/s3)**(1/cw-1))
	eb=cw*s4*p4*(1-(1-sell/s4)**(1/cw-1))
else:
	p5=p0*(s0/s5)**(1-1/cw)
	p6=p1*(s1/s6)**(1-1/cw)
	er=cw*s3*p3*(1-(1/(1-sell/s3))**(1-1/cw))
	eb=cw*s4*p4*(1-(1/(1-sell/s4))**(1-1/cw))
plt.plot([s5,s5],[0,p5],color="blue")
plt.plot([s6,s6],[0,p6],color="blue")
plt.plot([0,s4],[p3,p4],color="grey")
plt.plot([s3,s3],[0,p3],color="grey")
plt.plot([s4,s4],[0,p4],color="grey")
plt.plot([s3,s4],[p3,p4],color="grey")
plt.plot(s0, p0, 'r*')
plt.plot(s1, p1, 'r*')
plt.plot([s0,s1],[p0,p1],color="blue")
plt.plot(step,p0list,color="red")
plt.plot(step,p1list,color="black")
plt.savefig("1.png",dpi=60)
plt.legend()
plt.title("red s0="+str(s0)+"/black s1="+str(s1)+"\nr:b="+str(er)+":"+str(eb))
plt.xlabel("supply")
plt.ylabel("price")
plt.show()
