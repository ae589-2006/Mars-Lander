''' 
Assignment 1

Specific tasks
1. Write a program to execute the Euler and Verlet algorithms for the mass on the spring, and plot the
trajectories of the dynamical variables as functions of time. Convince yourself that the programs work by
solving the equation of motion analytically. To get you started, a Python script for the Euler method is
provided on the Moodle course page.

2. Investigate the numerical solution for various different values of the time step ∆t. Compare the performance of the two algorithms over several thousand oscillations, both with each other and also with the
exact analytical solution. For example, if you take m = k = v0 = 1 and calculate the trajectory from t = 0
to t = 1000, you should find that the Verlet integrator is stable for ∆t = 1 but not for ∆t = 2.

3. Find, by trial and error, the critical value of ∆t for the Verlet case, above which it becomes unstable.
The first order Euler integrator is never completely stable, but gets better for smaller values of ∆t.
'''

import numpy as np
import matplotlib.pyplot as plt

# Euler Integration

k = 1
m = 1 
x_negt = 0
v = 1
dt = 0.1
t_max = 100

t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []

x = x_negt + dt * v


for t in t_array:

    x_dt = 2*x - x_negt - (dt*dt) * (k*x)/m
    v = (1/dt) * (x_dt - x)

    x_list.append(x_dt)
    v_list.append(v)

    x_negt = x
    x = x_dt
    

    
print("The final value of x: " + str(x))
print("The final value of v: " + str(v))


x_array = np.array(x_list)
v_array = np.array(v_list)

print(x_array[:5])


plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()
