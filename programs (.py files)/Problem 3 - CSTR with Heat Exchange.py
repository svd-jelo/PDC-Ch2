import numpy as np
from scipy.integrate import odeint
from scipy import optimize
import matplotlib.pyplot as plt

# Define parameters
k0 = 7.2e+10 #Pre-exponential factor for the Arrhenious equation (1/min)
E_R = 8750 #Activation energy divided by the universal gas constant
p = 1000 #Liquid density (g/L)
C = 0.239 #Liquid heat capacity (J/g-K)
Hrxn = 5.0e+4 #Negative of the heat of reaction (J/mol)
UA = 5.0e+4 #Overall heat transfer coefficient times the heat transfer surface area (J/min-K)

# Define system of differential equations
def dydt(y, t, Tc, Ti, cai, q, V):
    """
    Return the value of dydt at time t. Here, is the response vector y=[y1,y2] with y1 = cA(t), y2 = T(t).

    Inputs:
    cai - Inlet concentration of A (mol/L)
    q - Outlet (and inlet) flowrate (L/m)
    V - Volume of liquid in the CSTR (L)
    Tc - Temperature of the coolant (K)
    Ti - Inlet temperature (K)
    """

    y1, y2 = y
    dy1dt = (q/V)*(cai - y1) - k0*y1*np.exp(-E_R/y2)
    dy2dt = (UA/(p*V*C))*(Tc - y2) + (q/V)*(Ti - y2) + ((k0*Hrxn)/(p*C))*y1*np.exp(-E_R/y2)
    return dy1dt, dy2dt

# Define operating conditions (initial conditions)
ca0, T0, Tc0, cai0, q0, V0 = 0.5, 350, 300, 1, 100, 100
Ti0 = T0 + (-(UA/(p*V0*C))*(Tc0 - T0) - ((k0*Hrxn)/(p*C))*ca0*np.exp(-E_R/T0))/(q0/V0)

# Time gird
t = np.linspace(0, 10, 1000)

#Integrate differential equations
y0 = ca0, T0
Tc1, Tc2 = 290, 305
y11, y12 = odeint(dydt, y0, t, args=(Tc1, Ti0, cai0, q0, V0)).T
y21, y22 = odeint(dydt, y0, t, args=(Tc2, Ti0, cai0, q0, V0)).T

#Temperature vs time plot
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (8,8))
axes[0].plot(t, np.ones(len(t))*T0,'r:', linewidth=2, label="300 K")
axes[0].plot(t, y12,'g--', linewidth=2, label="290 K")
axes[0].plot(t, y22,'b-', linewidth=2, label="350 K")
axes[0].set_ylabel('Temperature (K)')
axes[0].legend()

axes[1].plot(t, np.ones(len(t))*ca0, 'r:', linewidth=2, label="300 K")
axes[1].plot(t, y11, 'g--', linewidth=2, label="290 K")
axes[1].plot(t, y21, 'b-', linewidth=2, label="305 K")
axes[1].set_ylabel('Concentration (mol/L)')
axes[1].set_xlabel('Time (min)')
plt.show()
