'''
import numpy as np
import matplotlib.pyplot as plt

k = 1
m = 1 
x_negt = 0
v = 1

dt_max = 3
t_max = 100

xE_list = []
vE_list = []

xV_list = []
vV_list = []

maxX = []
maxV = []

dt_array = np.arange(0.1, dt_max, 0.1)

for dt in dt_array:

    t_array = np.arange(0, t_max, dt)

    x_E = x_negt + dt * v
    x_V = x_negt + dt * v

    for t in t_array:

      

        # calculate new position and velocity
        a_E = -k * x_E / m
        v_E = v_E + dt * a_E
        x_E = x_E + dt * v_E
        

        # append current state to trajectories
        xE_list.append(x_E)
        vE_list.append(v_E)

        x_dt = 2*x - x_negt - (dt*dt) * (k*x)/m
        v = (1/dt) * (x_dt - x)

        xE_list.append(x_dt)
        vV_list.append(v)

        x_negt = x
        x = x_dt

    maxX.append(max(xE_list))
    maxV.append(max(xV_list))

plt.figure(1)
plt.clf()
plt.xlabel('dt (s)')
plt.grid()
plt.plot(dt_array, maxX, label='x (m)')
plt.plot(dt_array, maxV, label='v (m/s)')
plt.legend()
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt

k = 1
m = 1

x = 0
v = 1

dt_max = 2.2
t_max = 1000

dt_array = np.arange(0.8, dt_max, 0.1)

# Maximum values for each dt
maxXE = []
maxVE = []

maxXV = []
maxVV = []


for dt in dt_array:

    t_array = np.arange(0, t_max, dt)


    x_E = x
    v_E = v

    xE_list = []
    vE_list = []


    x_V_negt = x
    x_V = x + dt * v

    xV_list = []
    vV_list = []


    for t in t_array:

        # ---- Euler ----

        a_E = -k * x_E / m

        x_E = x_E + dt * v_E
        v_E = v_E + dt * a_E

        xE_list.append(x_E)
        vE_list.append(v_E)


        x_V_dt = 2*x_V - x_V_negt - dt**2 * (k/m) * x_V

        v_V = (x_V_dt - x_V) / dt

        xV_list.append(x_V_negt)
        vV_list.append(v_V)

        x_V_negt = x_V
        x_V = x_V_dt

    maxXE.append(max(abs(np.array(xE_list))))
    maxVE.append(max(abs(np.array(vE_list))))

    maxXV.append(max(abs(np.array(xV_list))))
    maxVV.append(max(abs(np.array(vV_list))))

plt.figure()
plt.xlabel('dt (s)')
plt.ylabel('Maximum absolute value')
plt.grid()

plt.plot(dt_array, maxXE, label='Euler x')
plt.plot(dt_array, maxVE, label='Euler v')

plt.plot(dt_array, maxXV, label='Verlet x')
plt.plot(dt_array, maxVV, label='Verlet v')

plt.legend()
plt.show()