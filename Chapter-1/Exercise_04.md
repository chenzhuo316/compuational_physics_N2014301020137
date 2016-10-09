## 作业1.5
###要解方程：<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/Exercise_04/1.png)<br>
两式相加：<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/Exercise_04/2.png)<br>
两式相减：<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/Exercise_04/3.png)<br>
所以：<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/Exercise_04/4.png)<br>
因而可得：<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/Exercise_04/5.png)<br>
带入初始条件则有：<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/Exercise_04/6.png)<br>
###编辑代码如下：<br>
```python
import pylab as pl
class nuclei_decay:
    """
    A decay problem with two types of nuclei A and B.
    Simulation of the decay.
    Program to problem_1.5 on the book Computational Physics.
    """
    def __init__(self, number_of_A = 100, number_of_B = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        # unit of time is second
        self.N_A = [number_of_A]
        self.N_B = [number_of_B]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration / time_step + 1)
        print("Initial number of nuclei A ->", number_of_A)
        print("Initial number of nuclei B ->", number_of_B)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)

    def calculate(self):
         for i in range(self.nsteps):
            tmp_A = self.N_A[i] + (self.N_B[i] - self.N_A[i]) * self.dt / self.tau
            tmp_B = self.N_B[i] + (self.N_A[i] - self.N_B[i]) * self.dt / self.tau
            self.N_A.append(tmp_A)
            self.N_B.append(tmp_B)
            self.t.append(self.t[i] + self.dt)

    def show_results(self):
        plot1, = pl.plot(self.t, self.N_A, 'r')
        plot2, = pl.plot(self.t, self.N_B, 'g')
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.title("Number's change of nuclei A and nuclei B")
        pl.legend([plot1, plot2], ['nuclei A', 'nuclei B'], loc="best")
        pl.show()

    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            myfile.write(str(self.t[i]))
            myfile.write(str(self.N_A[i]))
        myfile.close()
        print myfile

a = nuclei_decay()
a.calculate()
a.show_results()
a.store_results()
```
###运行程序得到结果如图：<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/Exercise_04/7.JPG)<br>
###结论： 
系统趋于一个稳定状态，N(A)和N(B)都于常数，且其微商都趋于零。  
