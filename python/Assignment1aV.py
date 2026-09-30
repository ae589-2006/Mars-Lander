
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
