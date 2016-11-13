##Exercise 3.12-3.14
####作业代码  
```python
import math
import pylab as pl
class harmonic:
    def __init__(self, w_0 = 0, theta_01=0.2,theta_02=0.2+0.001, time_of_duration = 400, time_step = 0.04,g=9.8,length=9.8,q=1/2,F=1.2,D=2/3):
        # unit of time is second
        self.n_uranium_A1 = [w_0]
        self.n_uranium_B1= [theta_01]
        self.n_uranium_A2 = [w_0]
        self.n_uranium_B2= [theta_02]
        self.a=[math.log(abs(theta_02-theta_01))]
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
            self.n_uranium_A1.append(self.n_uranium_A1[i] -((self.g/self.length)*math.sin(self.n_uranium_B1[i])+self.q*self.n_uranium_A1[i]-self.F*math.sin(self.D*self.t[i]))*self.dt)
            self.n_uranium_B1.append(self.n_uranium_B1[i] + self.n_uranium_A1[i+1]*self.dt)
            if self.n_uranium_B1[i+1]<-math.pi:
                self.n_uranium_B1[i+1]=self.n_uranium_B1[i+1]+2*math.pi
            if self.n_uranium_B1[i+1]>math.pi:
                self.n_uranium_B1[i+1]=self.n_uranium_B1[i+1]-2*math.pi
            else:
                pass
            self.n_uranium_A2.append(self.n_uranium_A2[i] -((self.g/self.length)*math.sin(self.n_uranium_B2[i])+self.q*self.n_uranium_A2[i]-self.F*math.sin(self.D*self.t[i]))*self.dt)
            self.n_uranium_B2.append(self.n_uranium_B2[i] + self.n_uranium_A2[i+1]*self.dt)
            if self.n_uranium_B2[i+1]<-math.pi:
                self.n_uranium_B2[i+1]=self.n_uranium_B2[i+1]+2*math.pi
            if self.n_uranium_B2[i+1]>math.pi:
                self.n_uranium_B2[i+1]=self.n_uranium_B2[i+1]-2*math.pi
            else:
                pass
            self.t.append(self.t[i] + self.dt)
            self.a.append(math.log(abs(self.n_uranium_B2[i+1]-self.n_uranium_B1[i+1])))
    def show_results(self):
        pl.plot(self.t, self.a)
        pl.xlabel('time ($s$)')
        pl.ylabel(' angle(radians)')
        pl.legend(loc='upper right',frameon = True)
        pl.grid(True)
        pl.show()
a = harmonic()
a.calculate()
a.show_results()
```
####运行结果如下： 
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/7.1.png)
