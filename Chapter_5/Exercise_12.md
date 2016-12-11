第十二次作业
====
##Exercises 5.1-5.10
##Background
In regions of space that do not contain any electric charges,<br>
the electric potential obeys Laplace's equation<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.1.png)<br>
At the point (i,j,k) the derivative with respect to x ca be written as  
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.2.png)<br>
Another conceivable way is  
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.3.png)<br>
or  
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.4.png)<br>
Thus, it is natural to write the second partial derivative as   
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.5.png)<br>
Where the notation here is intended to indicate that the derivatives are to be evaluated at the location (i±½)  
This leads to   
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.6.png)<br>
and at littlerearranging yields   
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.7.png)<br>
Iserting them all into Laplace's equation and solving for V(i,j,k) we find  
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.8.png)<br>
here we assumed that the step sizes along x,y,and z are all the the same(Δx=Δy=Δz)  
Then we have the potential function V(i,j) that satisfies 
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.9.png)<br>
##Now we want to solve for the potential in the prism geometry  
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.10.png)<br>
[Code1](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_1/Homework_12.1.py)<br>
[Code2](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_1/Homework_12.2.py)<br>
We use initial guess V₁:  
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.11.png)<br>
Running the code we obtain the result like that:
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.12.png)<br>
![](https://github.com/kolir/compuational_physics_N2014301020137/blob/master/File_2/12.13.png)<br>



