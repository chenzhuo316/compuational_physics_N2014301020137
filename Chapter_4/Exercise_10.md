第十次作业
===
##Precession of the periheloin of Mericury 
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/10.1.gif)<br>
####The force law predicted by general relativity is  
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/10.2.png)<br>
####Conservation of total energy:   
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/10.3.png)<br>
####Conservation of the angular momentum:
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/10.4.png)<br>
####Then  
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/10.5.png)<br>
####For different elliptical orbits with different eccentricities,but with the same perihelion.<br>
####we use this code to simulate the motion of the plant  
```python
from numpy import *
import matplotlib.pyplot as plt
class INVERSE(object):
    ''' 
    class BINARY solves for system that not satisfy the inverse-square law
    where:
        -beta: index of the force
        e: ellipticity
        m: mass of central star
        dt, time : time step size and total time 
    '''
    def __init__(self, _beta=2.05, _e=0., _m=4*(pi**2), _dt=0.001, _time=20):
        self.m=_m
        self.e=_e
        self.x, self.y=[1.],[0.]
        self.vx, self.vy=[0],[sqrt(_m)*sqrt((1.-_e)/(1.+_e))]
        self.beta=_beta
        self.dt=_dt
        self.time= _time
        self.n=int(_time/_dt)
        #print self.x[-1],self.y[-1],self.vx[-1],self.vy[-1]
    def cal(self):       # use Euler-Cromer Method to calculate the trajectory of stars
        for i in range(self.n):
            self.r=sqrt(self.x[-1]**2+self.y[-1]**2)
            self.vx.append(self.vx[-1]+self.dt*(-self.m*self.x[-1]/self.r**(self.beta+1.)))
            self.vy.append(self.vy[-1]+self.dt*(-self.m*self.y[-1]/self.r**(self.beta+1.)))
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def plot_trajectory(self):       # plot the trajectory
        plt.plot(self.x,self.y,markersize=0.5,label='e= %.2f'%self.e)
        plt.plot([self.x[-1]],[self.y[-1]],markersize=8)
        plt.plot([0],[0],'or',markersize=20)
    def precession_rate(self):  # calculate the precession rate
        self.x_critical=0
        self.y_critical=0
        self.t_critical=0
        for i in range(len(self.x)-2):
            self.r_i=sqrt(self.x[i]**2+self.y[i]**2)
            self.r_i1=sqrt(self.x[i+1]**2+self.y[i+1]**2)
            self.r_i2=sqrt(self.x[i+2]**2+self.y[i+2]**2)
            if self.r_i<self.r_i1 and self.r_i1>self.r_i2:
                self.x_critical=self.x[i+1]
                self.y_critical=self.y[i+1]
                self.t_critical=self.dt*(i+1)
                break
        self.rate = arctan(self.y_critical/self.x_critical)/self.t_critical
        return self.rate
# calculate the trajectory of planet with different ellipticity       
for i in range(8):
    fig=plt.figure(figsize=(10,10)) 
    plt.xlim(-1.2,1.2)
    plt.ylim(-1.2,1.2)
    plt.xlabel(r'$x$'+' (AU)',fontsize=18)
    plt.ylabel(r'$y$'+' (AU)',fontsize=18)
    plt.title(r'$\beta=2.05$'+'  '+'e='+str(i*0.2),fontsize=18)
    cmp=INVERSE(2.05,i*0.2)
    cmp.cal()
    cmp.plot_trajectory()
    plt.show()
# change the ellipticity and get the corresponding precession rate
e=[]
rate=[]
for i in linspace(0.1,0.6,20):
    cmp= INVERSE(2.05,i)
    cmp.cal()
    e.append(i)
    rate.append(180/pi*cmp.precession_rate())
plt.xlim(-0,0.7)
plt.xlabel(r'e')
plt.ylabel(r'Precession rate '+r'$ degree/yr $',fontsize=18)
plt.title(r'Precession rate',fontsize=18)
plt.plot(e,rate,'oy')
plt.plot(e,rate,'-r')
plt.show()
```
####Then we get the results like that:  
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/10.6.png)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/10.7.png)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/10.8.png)<br>
