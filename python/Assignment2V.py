'''
After modifying your Euler and Verlet programs as described above, check them by simulating:
1. Straight down descent 3. Elliptical orbit
2. Circular orbit 4. Hyperbolic escape
For simplicity, take the centre of the planet to be the origin of the coordinate system, and the direction of
the initial velocity to be perpendicular to the initial position vector of the body for Scenarios 2–4. Use zero
initial velocity for Scenario 1. You will obtain different orbits by adjusting the magnitude of the initial
velocity. It might help if you first calculate the required speed for a circular orbit, and the escape velocity
(use the principle of conservation of energy). For Scenario 1, plot altitude as a function of time. For
Scenarios 2–4, plot the trajectory in the orbital plane.
'''

import numpy as np
import matplotlib.pyplot as plt



# Euler Program

#Force Constants

G = 6.6743 * (10**-11)
M = 6.42 * (10**23)

pos_negt = [0, -4.4e6, 0]

velcalc = np.sqrt(G*M / 4.4e6)
vel = [velcalc*1.44, 0, 0]



dt = 0.1
t_max = 40000

t_array = np.arange(0, t_max, dt)

pos_list = []
vel_list = []

pos = pos_negt + np.multiply(vel, dt)

for t in t_array:
    cnst = - G * M * (1/(np.linalg.norm(pos))**3)

    pos_new = 2* pos - pos_negt + np.multiply(pos, (dt**2)*cnst)

    vel = np.multiply(pos_new-pos, 1/dt)

    pos_list.append(pos_new)
    vel_list.append(vel)

    pos_negt = pos
    pos = pos_new

#Scenario 1 pos = [1, 2, 3], vel = [0, 0, 0]
altitude = []

for i in pos_list:
    altitude.append(i[1])

altitude_array = np.array(altitude)

#Scenario 2, 3, 4 varying vel
x_list = []
y_list = []

for i in pos_list:
    x_list.append(i[0])
    y_list.append(i[1])

x_array = np.array(x_list)
y_array = np.array(y_list)

plt.figure(2)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(x_array, y_array, label='x (m)')
plt.axis('equal')
plt.legend()
plt.show()