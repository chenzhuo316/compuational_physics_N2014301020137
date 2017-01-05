import numpy as np
import random
import pylab as pl

def init_spin_array(rows, cols):
    return np.ones((rows, cols))

def find_neighbors(spin_array, lattice, x, y):
    
    left   = (x, y - 1)
    right  = (x, (y + 1) % lattice)
    top    = (x - 1, y)
    bottom = ((x + 1) % lattice, y)
    neighber = [spin_array[left[0], left[1]],
                spin_array[right[0], right[1]],
                spin_array[top[0], top[1]],
                spin_array[bottom[0], bottom[1]]]
    return neighber


def energy(spin_array, lattice, x ,y, H):#J=2
    return (2 * spin_array[x, y] * sum(find_neighbors(spin_array, lattice, x, y))) / 4.0\
           - H * sum(sum(spin_array)) 
           
def monte_carlo(spin_array, lattice, temperature, H):
    E1 = 0
    for i in range(lattice):
        for j in range(lattice):
            e = energy(spin_array, lattice, i, j, H)
            if e <= 0:
                spin_array[i, j] = -1 * spin_array[i, j]
            elif np.exp((-1.0 * e)/temperature) > random.random():
                spin_array[i, j] = -1 * spin_array[i, j]
            E1 = E1 + (-1) * energy(spin_array, lattice, i, j, H)
    return [E1, spin_array]

def mag():
    RELAX_SWEEPS = 50
    lattice = 10#eval(input("Enter lattice size: "))
    sweeps = 10000#eval(input("Enter the number of Monte Carlo Sweeps: "))
    M1 = mag = [0 for i in range(sweeps + RELAX_SWEEPS)]
    E1 = energy_ever=[0 for i in range(sweeps + RELAX_SWEEPS)]
    M2 = mag2 = [0 for i in range(sweeps + RELAX_SWEEPS)]
    E2 = energy_ever2 = [0 for i in range(sweeps + RELAX_SWEEPS)]
    for H in [0]:
        for temperature in np.arange(0, 1.5, 0.05):
            spin_array = init_spin_array(lattice, lattice)
            for sweep in range(sweeps + RELAX_SWEEPS):
                [e, spin_array] = monte_carlo(spin_array, lattice, temperature, H)
                #E1[sweep] = e 
                M1[sweep] = sum(sum(spin_array))
                #E2[sweep] =(e) ** 2 
                #M2[sweep] = (sum(sum(spin_array))) ** 2
            
            #能量和磁化强度
            pl.plot(temperature, abs(sum(M1)) / (RELAX_SWEEPS + sweeps) / (lattice ** 2),'o',color="red")
            #pl.plot(temperature, sum(E1) / (RELAX_SWEEPS + sweeps) / (lattice ** 2), 'rx-')
            
            #磁化率
    pl.savefig('M-T.png')   
        
            
def spec():
    RELAX_SWEEPS = 50
    lattice = 10#eval(input("Enter lattice size: "))
    sweeps = 10000#eval(input("Enter the number of Monte Carlo Sweeps: "))
    M1 = mag = [0 for i in range(sweeps + RELAX_SWEEPS)]
    E1 = energy_ever=[0 for i in range(sweeps + RELAX_SWEEPS)]
    M2 = mag2 = [0 for i in range(sweeps + RELAX_SWEEPS)]
    E2 = energy_ever2 = [0 for i in range(sweeps + RELAX_SWEEPS)]
    for H in [0]:
        for temperature in np.arange(0, 1.5, 0.05):
            spin_array = init_spin_array(lattice, lattice)
            for sweep in range(sweeps + RELAX_SWEEPS):
                [e, spin_array] = monte_carlo(spin_array, lattice, temperature, H)
                E1[sweep] = e 
                #M1[sweep] = sum(sum(spin_array))
                E2[sweep] =(e) ** 2 
                #M2[sweep] = (sum(sum(spin_array))) ** 2
            
            #能量和磁化强度
            #pl.plot(temperature, abs(sum(M1)) / (RELAX_SWEEPS + sweeps) / (lattice ** 2), 'rx-')
            #pl.plot(temperature, sum(E1) / (RELAX_SWEEPS + sweeps) / (lattice ** 2), 'rx-')
            
            #磁化率
            """
            pl.scatter(temperature, (sum(M2) / (RELAX_SWEEPS + sweeps) - sum(M1) \
                       ** 2 / (RELAX_SWEEPS + sweeps) ** 2) \
                        / (RELAX_SWEEPS + sweeps) / temperature ** 2)
            """
            
            #热容
            pl.plot(temperature, (sum(E2) / (RELAX_SWEEPS + sweeps) - sum(E1) \
                       ** 2 / (RELAX_SWEEPS + sweeps) ** 2) \
                        / (RELAX_SWEEPS + sweeps) / temperature ** 2,'*',color="red")

    pl.savefig('热容.png')
def ener():
    RELAX_SWEEPS = 50
    lattice = 10#eval(input("Enter lattice size: "))
    sweeps = 10000#eval(input("Enter the number of Monte Carlo Sweeps: "))
    M1 = mag = [0 for i in range(sweeps + RELAX_SWEEPS)]
    E1 = energy_ever=[0 for i in range(sweeps + RELAX_SWEEPS)]
    M2 = mag2 = [0 for i in range(sweeps + RELAX_SWEEPS)]
    E2 = energy_ever2 = [0 for i in range(sweeps + RELAX_SWEEPS)]
    for H in [0]:
        for temperature in np.arange(0, 1.5, 0.05):
            spin_array = init_spin_array(lattice, lattice)
            for sweep in range(sweeps + RELAX_SWEEPS):
                [e, spin_array] = monte_carlo(spin_array, lattice, temperature, H)
                E1[sweep] = e 
            
            #能量和磁化强度
            #pl.plot(temperature, abs(sum(M1)) / (RELAX_SWEEPS + sweeps) / (lattice ** 2), 'rx-')
            pl.plot(temperature, sum(E1) / (RELAX_SWEEPS + sweeps) / (lattice ** 2), 'o',color="blue")
            
            #磁化率
            """
            pl.scatter(temperature, (sum(M2) / (RELAX_SWEEPS + sweeps) - sum(M1) \
                       ** 2 / (RELAX_SWEEPS + sweeps) ** 2) \
                        / (RELAX_SWEEPS + sweeps) / temperature ** 2)
            """
    pl.savefig('E-T.png')

def susp():
    RELAX_SWEEPS = 50
    lattice = 10#eval(input("Enter lattice size: "))
    sweeps = 10000#eval(input("Enter the number of Monte Carlo Sweeps: "))
    M1 = mag = [0 for i in range(sweeps + RELAX_SWEEPS)]
    E1 = energy_ever=[0 for i in range(sweeps + RELAX_SWEEPS)]
    M2 = mag2 = [0 for i in range(sweeps + RELAX_SWEEPS)]
    E2 = energy_ever2 = [0 for i in range(sweeps + RELAX_SWEEPS)]
    for H in [0]:
        for temperature in np.arange(0, 1.5, 0.05):
            spin_array = init_spin_array(lattice, lattice)
            for sweep in range(sweeps + RELAX_SWEEPS):
                [e, spin_array] = monte_carlo(spin_array, lattice, temperature, H)
                #E1[sweep] = e 
                M1[sweep] = sum(sum(spin_array))
                #E2[sweep] =(e) ** 2 
                M2[sweep] = (sum(sum(spin_array))) ** 2
            #磁化率       
            pl.plot(temperature, (sum(M2) / (RELAX_SWEEPS + sweeps) - sum(M1) \
                       ** 2 / (RELAX_SWEEPS + sweeps) ** 2) \
                        / (RELAX_SWEEPS + sweeps) / temperature, '*',color="blue")
    pl.savefig('磁化率.png')
            
pl.figure()
pl.title('Ising model    Energy versus Temperature')
pl.ylabel('Energy')
pl.xlabel('Temperature')
ener()   
    
pl.figure()
pl.title('Ising model    Specific heat versus Temperature')
pl.ylabel('Specific heat per spin')
pl.xlabel('Temperature')
spec() 

pl.figure()
pl.title('Ising model    Magnetization versus Temperature')
pl.ylabel('Magnetization')
pl.xlabel('Temperature')
mag()

pl.figure()
pl.title('Ising model    $\\chi$ versus Temperature')
pl.ylabel('$\\chi$')
pl.xlabel('Temperature')
susp()
