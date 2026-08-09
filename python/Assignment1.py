''' Assignment 1

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

