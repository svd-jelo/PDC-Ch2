import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Parameters
p = 900 #Density of the liquid (kg/m3)

#Define initial conditions
V0, x0, w10, w20, x10, x20 = 2, 0.5, 500, 200, 0.4, 0.75

#Derivative
def dxdt(x, t, w1, w2, x1, x2):
    """
    Returns the value of dxdt = f(x, w1, w2, w, x1, x2).
    
    x - outlet concentration (mass fraction)
    x1, x2 - inlet concentrations (mass fraction)
    w - outlet mass flowrate (kg/min)
    w1, w2 - inlet flowrates (kg/min)
    """
    w = w1 + w2
    dxdt = (x1*w1 + x2*w2 - x*w)/(p*V0)
    return dxdt

#Define the time grid
t = np.linspace(0, 25, 1000)

#Define the new values of w1, w2, and x1:
w1, w2, x1 = 400, 100, 0.6

#Solve the differential equation
x_a = odeint(dxdt, x0, t, args=(w1, w20, x10, x20)) #Case (a) w1 changes from 500 to 400
x_b = odeint(dxdt, x0, t, args=(w10, w2, x10, x20)) #Case (b) w2 changes (instead of w1) from 200 to 100
x_c = odeint(dxdt, x0, t, args=(w10, w2, x1, x20))#Case (c) x1 changes from 0.4 to 0.6 in addition to the change in w2

#Plot the solutions for analysis
fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (6,6))
ax.plot(t, x_a, 'b-', linewidth = 2, label = "Case (a)")
ax.plot(t, x_b, 'g--', linewidth = 2, label = "Case (b)")
ax.plot(t, x_c, 'r:', linewidth = 2, label = "Case (c)")
ax.set_xlabel("Time (min)")
ax.set_ylabel("Concentration (mass fraction)")
ax.legend()
plt.show()