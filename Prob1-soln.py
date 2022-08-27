from sympy import *
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
sp.init_printing()

t, s = sp.symbols('t,s')
a = sp.symbols('a', real=True, positive=True)
X = sp.exp(-15*s)/s

def invL(F):
    return sp.inverse_laplace_transform(F,s,t)

#constants
w1 = 500 #stream 1 flowrate (kg/min)
w2 = 200 #stream 2 flowrate (kg/min)
x1 = 0.4 #stream 1 composition (mass frac)
x2 = 0.75 #stream 2 composition (mass frac)

w = w1 + w2 #exit stream flowrate (kg/min)
p = 900 #density (kg/m3)
V = 2 #liquid holdup (m3)
tau = p*V/w #some constant

alpha1 = x2*w2/w
alpha2 = x1*w1/w
alpha3 = 0.2*w1/w

beta1 = 100*x1/w
beta2 = 100*x2/w
beta3 = 100*x2/w

#inputs
u1_ = alpha1 + beta1*(5-sp.Heaviside(t-15))
u2_ = alpha2 + beta2*(2-sp.Heaviside(t-15))
u3_ = alpha3*(2 + sp.Heaviside(t-15)) + beta3*(2-sp.Heaviside(t-15))

#initial conditions
x01 = 0
x02 = 0
x03 = 0

#Subsidiary Equation
Q = 1/(tau*s + 1)

R1 = sp.laplace_transform(u1_,t,s,noconds=true)
R2 = sp.laplace_transform(u2_,t,s,noconds=true)
R3 = sp.laplace_transform(u3_,t,s,noconds=true)

X1 = (tau*x01 + R1)*Q
X2 = (tau*x02 + R2)*Q
X3 = (tau*x03 + R3)*Q

#Solutions
x1_ = invL(X1)
x2_ = invL(X2)
x3_ = invL(X3)

#Time interval
a = np.linspace(0,25,250)

#w1, w2, x
w1_v = np.ones(len(a))*500
w1_v[150:] = 400

w2_v = np.ones(len(a))*200
w2_v[150:] = 100

x1_v = np.ones(len(a))*0.4
x1_v[150:] = 0.6

#Lambdified solutions
x1 = lambdify(t, x1_, "numpy")
x2 = lambdify(t, x2_, "numpy")
x3 = lambdify(t, x3_, "numpy")

#Plot
fig, ax = plt.subplots(nrows=3,ncols=2,figsize=(14,14))

#row1
ax[0,0].plot(a,w1_v,'r--',linewidth=2,label='input w1(t)')
ax[0,0].set_ylabel('flowrate 1 (kg/min)')
ax[0,0].legend()

ax[0,1].plot(a,x1(a),'b-',linewidth=2,label='response x(t)')
ax[0,1].legend()

#row2
ax[1,0].plot(a,w2_v,'g--',linewidth=2,label='input w2(t)')
ax[1,0].set_ylabel('flowrate 2 (kg/min)')
ax[1,0].legend()

ax[1,1].plot(a,x2(a),'b-',linewidth=2,label='response x(t)')
ax[1,1].set_ylabel('composition of x (mass frac)')
ax[1,1].legend()

#row3
ax[2,0].plot(a,x1_v,'y--',linewidth=2,label='input x1(t)')
ax[2,0].set_ylabel('composition 1 (mass frac)')
ax[2,0].set_xlabel('time (min)')
ax[2,0].legend()

ax[2,1].plot(a,x3(a),'b-',linewidth=2,label='response x(t)')
ax[2,1].set_xlabel('time (min)')
ax[2,1].legend()

plt.show()

