##第八次作业
###Chapter3-exercise 3.18
####We want to calculate Poincaré sections for the pendulum as it undergoes the period-doubling route to chaos. 
####For F=1.4,1.44 and 1.465  
####We use this code tu simulate  
```python
import math
import pylab as pl
class harmonic:
    def __init__(self, w_0 = 0, theta_0=0.2, time_of_duration = 10000, time_step = 0.04,g=9.8,length=9.8,q=1/2,F=1.465,D=2/3):
        # unit of time is second
        self.n_uranium_A = [w_0]
        self.n_uranium_B = [theta_0]
        self.t = [0]
        self.g=g
        self.length=length
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.q=q
        self.F=F
        self.D=D
        self.n_uranium_A2=[0]
        self.n_uranium_B2=[0]
    def calculate(self):
        for i in range(self.nsteps):
            self.n_uranium_A.append(self.n_uranium_A[i] -((self.g/self.length)*math.sin(self.n_uranium_B[i])+self.q*self.n_uranium_A[i]-self.F*math.sin(self.D*self.t[i]))*self.dt)
            self.n_uranium_B.append(self.n_uranium_B[i] + self.n_uranium_A[i+1]*self.dt)
            if self.n_uranium_B[i+1]<-math.pi:
                self.n_uranium_B[i+1]=self.n_uranium_B[i+1]+2*math.pi
            if self.n_uranium_B[i+1]>math.pi:
                self.n_uranium_B[i+1]=self.n_uranium_B[i+1]-2*math.pi
            else:
                pass
            self.t.append(self.t[i] + self.dt)
        for i in range(self.nsteps):
            if self.t[i]%(2*math.pi/self.D)<0.02:
                self.n_uranium_A2.append(self.n_uranium_A[i])
                self.n_uranium_B2.append(self.n_uranium_B[i])
    def show_results(self):
        pl.plot( self.n_uranium_B2,self.n_uranium_A2,'.')
        pl.xlabel('angle(radians)')
        pl.ylabel(' angle velocity')
        pl.legend(loc='upper right',frameon = True)
        pl.grid(True)
        pl.show()
a = harmonic()
a.calculate()
a.show_results()
```
####The results like that:  
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/8.1.png) 
===
####Use the following code, we get the results for θ as a function of time: 
```python
import math
import pylab as pl
class harmonic:
    def __init__(self, w_0 = 0, theta_0=0.2,  time_of_duration =70, time_step = 0.04,g=9.8,length=9.8,q=1/2,F=1.4,D=2/3):
        # unit of time is second
        self.n_uranium_A = [w_0]
        self.n_uranium_B = [theta_0]
        self.t = [0]
        self.g=g
        self.length=length
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.q=q
        self.F=F
        self.D=D
    def calculate(self):
        for i in range(self.nsteps):
            tmpA = self.n_uranium_A[i] -((self.g/self.length)*math.sin(self.n_uranium_B[i])+self.q*self.n_uranium_A[i]-self.F*math.sin(self.D*self.t[i]))*self.dt
            tmpB = self.n_uranium_B[i] + self.n_uranium_A[i]*self.dt
            self.n_uranium_A.append(tmpA)
            self.n_uranium_B.append(tmpB)
            self.t.append(self.t[i] + self.dt)
            if self.n_uranium_B[i+1]<-math.pi:
                self.n_uranium_B[i+1]=self.n_uranium_B[i+1]+2*math.pi
            if self.n_uranium_B[i+1]>math.pi:
                self.n_uranium_B[i+1]=self.n_uranium_B[i+1]-2*math.pi
            else:
                pass
    def show_results(self):
        pl.plot(self.t, self.n_uranium_B,label=' F=1.4')
        pl.xlabel('time ($s$)')
        pl.ylabel('angle(radians)')
        pl.legend(loc='best',frameon = True)
        pl.grid(True)
a = harmonic()
a.calculate()
a.show_results()
```
####This is the result: 
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/8.2.png)

