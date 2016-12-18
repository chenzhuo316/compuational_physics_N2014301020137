第十三次作业
=====
##Exercise6.9-6.17
##The central equation of wave motion is  
![](http://i1.piimg.com/1949/ac3f4e7be96dbcc1.png)<br>
###Then use a finite difference approximation for the angles  
![](http://i1.piimg.com/1949/8855fa0887cf5be4.jpg)<Br>
![](http://p1.bqimg.com/1949/4a5c25b849d5d6d2.png)<br>
##we obtain 
![](http://p1.bqimg.com/1949/e143d57e0b33ea72.png)<br>
##We can get this result  
![](http://p1.bqimg.com/1949/fa70c39e1639185f.png)<br>

###Code1:
```python
from matplotlib import animation
from pylab import*
import numpy as np
c=300.0
dx=0.01
dt=0.01
t=0.0

y=[]
l=np.linspace(0,1,100)#x-axis
y0=np.exp(-1000*(l-0.3)**2)#y-axis it's a wave package locates at x=0.3
y0_2=np.exp(-1000*(l-0.7)**2)+np.exp(-700*(l-0.7)**2)    

def w():
    global t,dt
    y.append(y0_2)
    y.append(y0_2)
    while t<100.0:
        y_next=np.zeros(100)

        for i in range(1,98):
            y_next[i]=-y[-2][i]+y[-1][i+1]+y[-1][i-1]

        y.append(y_next)
        t=t+dt
    return y, t
#print w()[0] ,w()[1]

def w2():
    global t,dt
    y.append(y0)
    y.append(y0)
    while t<100.0:
        y_next=np.zeros(100)

        for i in range(1,98):
            if i<50:
                y_next[i]=-y[-2][i]+y[-1][i+1]+y[-1][i-1]
            else: 
                y_next[i]=2*(1-0.5)*y[-1][i]-y[-2][i]+0.5*(y[-1][i+1]+y[-1][i-1])
        y.append(y_next)
        t=t+dt
    return y, t
#print w()[0] ,w()[1]

a=w()[0]
a=w()[0]
f=figure()
ax=axes(xlim=(0,1),ylim=(-1.2,1.2))
line, =ax.plot([],[],lw=2)

def animate(i):
    line.set_data(l,a[i])
    return line,
def init():
    line.set_data([],[])
    return line,
anim=animation.FuncAnimation(f,animate,init_func=init,frames=200,interval=50,blit=True)#frames mean zhenshu,interval mean each frame last how long
show()

```

###The rresults:  
######During the course of a calculation,the time index n will run from the initial time(n=0) to some final value corresponding to the ######time interval of interest.Sincd the string is modeled as a large number of discrete elements,I generate a lot of "data", but I ######only need to store information for 3 consecutive time step. 
![](http://p1.bqimg.com/1949/e1456be6a213d42c.gif)<br>
![](http://p1.bqimg.com/1949/0eebcc4595975704.gif)<br>


######These peaks can in terms of the standing waves that are found for a string with fixed ends.The standing waves with the longest ######wavelength has a wavelength λ1 > 2L ,the other standing waves have wavelengths of L, 2L/3.These standing waves can be thought of ######as the basic spatial Fourier components of the strin motion
###Code2
```python
from matplotlib import animation
from pylab import*
import numpy as np
c=320.0
dx=6.5*1e-4
l=np.linspace(0,0.65,1000)

def w():
    y=[]
    dt=dx/c
    t=0.0
    y0=np.exp(-1000*(l-l*0.2)**2)
    y.append(y0)
    y.append(y0)
    while t<0.05:
        y_next=np.zeros(1000)

        for i in range(1,998):
            y_next[i]=-y[-2][i]+y[-1][i+1]+y[-1][i-1]

        y.append(y_next)
        t=t+dt
    return y, t
#print w()[0] ,w()[1]

y1=[]
def w2():
    t1=0.0
    dt1=dx/c
    y_1=np.exp(-1000*(l-l*0.05)**2)
    y1.append(y_1)
    y1.append(y_1)
    while t1<0.05:
        y_next=np.zeros(1000)
        for i in range(1,998):
            y_next[i]=-y1[-2][i]+y1[-1][i+1]+y1[-1][i-1]
        y1.append(y_next)
        t1=t1+dt1
    return y1, t1

a=w()[0]
a01=w2()[0]
#print cmp(a,a01)
'''
for iter in a01:
   print type(a01)
   '''
b=[a_iter[800] for a_iter in a]
b01=[a01_iter[950] for a01_iter in a01]
print( len(b))
e=len(b)
e01=len(b01)
d=linspace(0,dx/c*e,e)
d01=linspace(0,dx/c*e01,e01)
#print d
'''
plot(d,b)
xlim(0,0.05)
xlabel('Time(s)')
ylabel('Signal(arbitary units)')
title('String signal versus time')
show()
'''
y2=np.fft.fft(b)

f=np.fft.fftfreq(len(b),dx/c)
y2=abs(y2)**2
#print f,len(y2)
plot(f,y2)
xlim(0,6000)
xlabel('Frequency(Hz)')
ylabel('Power(arbitrary units)')
title('Guitar Power spectrum:Pluck at 1/5')
show()

y21=np.fft.fft(b01)
f01=np.fft.fftfreq(len(b01),dx/c)
y21=abs(y21)**2
plot(f01,y21,color='r')
xlim(0,12000)
xlabel('Frequency(Hz)')
ylabel('Power(arbitrary units)')
title('Guitar Power spectrum:Pluck at 1/20')
show()
```

