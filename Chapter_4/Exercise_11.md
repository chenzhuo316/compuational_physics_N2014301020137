第十一次作业
===
```python
from math import pi,sqrt,sin,cos
import matplotlib.pyplot as plt
def hyperion(theta0):
    # set the mass of saturn
    gm=4*pi**2
    # initialize position of center of mass, angle, angle velocity
    xc=[1]
    yc=[0]
    theta=[theta0]
    avelo=[0]
    vxc=[0]
    vyc=[2*pi]
    # get the trails
    dt=0.0001
    t=[0]
    while t[-1]<=15:
        r=sqrt((xc[-1])**2+(yc[-1])**2)
        vxc_new=vxc[-1]-gm*xc[-1]*dt/r**3
        vyc_new=vyc[-1]-gm*yc[-1]*dt/r**3
        avelo_new=avelo[-1]-12*(pi**2)*(xc[-1]*sin(theta[-1])-yc[-1]*cos(theta[-1]))*(xc[-1]*cos(theta[-1])+yc[-1]*sin(theta[-1]))*dt/r**5
        vxc.append(vxc_new)
        vyc.append(vyc_new)
        avelo.append(avelo_new)
        xc.append(xc[-1]+vxc[-1]*dt)
        yc.append(yc[-1]+vyc[-1]*dt)
        theta_new=theta[-1]+avelo[-1]*dt
        if theta_new<-pi:
            theta_new+=2*pi
        if theta_new>pi:
            theta_new-=2*pi
        theta.append(theta_new)
        t.append(t[-1]+dt)
    return theta,t
t=hyperion(0)[1]
the1=hyperion(0)[0]
the2=hyperion(0.01)[0]
dthe=[]
plt.plot(t,the1)
plt.title(' theta vs time')
plt.xlabel('time(yr)')
plt.ylabel('theta(radians)')
plt.xlim(0,15)
plt.show()
```
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/887ea9fa7ecc5cadaf05cd8edc6ae08488b7d671/File_2/10.1.png)<br>
```python
from math import pi,sqrt,sin,cos
import matplotlib.pyplot as plt
def hyperion(theta0):
    # set the mass of saturn
    gm=4*pi**2
    # initialize position of center of mass, angle, angle velocity
    xc=[1]
    yc=[0]
    theta=[theta0]
    avelo=[0]
    vxc=[0]
    vyc=[5]
    # get the trails
    dt=0.0001
    t=[0]
    while t[-1]<=15:
        r=sqrt((xc[-1])**2+(yc[-1])**2)
        vxc_new=vxc[-1]-gm*xc[-1]*dt/r**3
        vyc_new=vyc[-1]-gm*yc[-1]*dt/r**3
        avelo_new=avelo[-1]-12*(pi**2)*(xc[-1]*sin(theta[-1])-yc[-1]*cos(theta[-1]))*(xc[-1]*cos(theta[-1])+yc[-1]*sin(theta[-1]))*dt/r**5
        vxc.append(vxc_new)
        vyc.append(vyc_new)
        avelo.append(avelo_new)
        xc.append(xc[-1]+vxc[-1]*dt)
        yc.append(yc[-1]+vyc[-1]*dt)
        theta_new=theta[-1]+avelo[-1]*dt
        theta.append(theta_new)
        t.append(t[-1]+dt)
    return theta,t
t=hyperion(0)[1]
the1=hyperion(0)[0]
the2=hyperion(0.01)[0]
dthe=[]
for i in range(len(the1)):
    dthe.append(abs(the2[i]-the1[i]))
plt.plot(t,dthe)
plt.semilogy(t,dthe)
plt.title('delta theta vs time')
plt.xlabel('time(yr)')
plt.ylabel('dtheta(radians)')
plt.xlim(0,15)
plt.show()
```
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/887ea9fa7ecc5cadaf05cd8edc6ae08488b7d671/File_2/10.2.png)<br>
```python
from math import pi,sqrt,sin,cos
import matplotlib.pyplot as plt
def hyperion(theta0):
    # set the mass of saturn
    gm=4*pi**2
    # initialize position of center of mass, angle, angle velocity
    xc=[1]
    yc=[0]
    theta=[theta0]
    avelo=[0]
    vxc=[0]
    vyc=[1]
    # get the trails
    dt=0.0001
    t=[pi]
    while t[-1]<=15:
        r=sqrt((xc[-1])**2+(yc[-1])**2)
        vxc_new=vxc[-1]-gm*xc[-1]*dt/r**3
        vyc_new=vyc[-1]-gm*yc[-1]*dt/r**3
        avelo_new=avelo[-1]-12*(pi**2)*(xc[-1]*sin(theta[-1])-yc[-1]*cos(theta[-1]))*(xc[-1]*cos(theta[-1])+yc[-1]*sin(theta[-1]))*dt/r**5
        vxc.append(vxc_new)
        vyc.append(vyc_new)
        avelo.append(avelo_new)
        xc.append(xc[-1]+vxc[-1]*dt)
        yc.append(yc[-1]+vyc[-1]*dt)
        theta_new=theta[-1]+avelo[-1]*dt
        theta.append(theta_new)
        t.append(t[-1]+dt)
    return theta,t
t=hyperion(0)[1]
the1=hyperion(0)[0]
the2=hyperion(0.01)[0]
dthe=[]
for i in range(len(the1)):
    dthe_new=abs(abs(the2[i]-the1[i]))
    while dthe_new>pi:
        dthe_new-=2*pi
    while dthe_new<-pi:
        dthe_new+=2*pi
    dthe.append(dthe_new)
plt.plot(t,dthe)
plt.semilogy(t,dthe)
plt.title(r'$\theta=1$'+'  '+'v0=0',fontsize=18)
plt.xlabel('time(yr)')
plt.ylabel('dtheta(radians)')
plt.xlim(0,15)
plt.show()
```
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/11.2.jpg)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/11.3.jpg)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/11.4.jpg)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/11.5.jpg)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/11.6.jpg)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/11.7.jpg)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/11.8.jpg)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/11.9.jpg)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/11.10.jpg)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/11.11.jpg)<br>












