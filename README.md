# Chapter 2 - Theoretical Models of Chemical Processes
## Example 1 - Blending Process
A stirred-tank blending process with a constant liquid hold up of $2~\text{m}^3$ is used to blend two streams whose densities are both approximately $900~\text{kg/m}^3$. The density does not change during mixing.<br/>
1. Assume that the process has been operating for a long period of time with flow rates of $w_1 = 500~\text{kg/min}$ and $w_2 = 200~\text{kg/min}$, and feed compositions (mass fraction) of $x_1 = 0.4$ and $x_2 = 0.75$. What is the steady-state value of $x$.
2. Suppose that $w_1$ changes suddenly from $500$ to $400~\text{kg/min}$ and remains at the new value. Determine an expression for $x(t)$ and plot it.
3. Repeat part 2 for the case where $w_2$ (insead of $w_1$) changes suddenly from $200$ to $100~\text{kg/min}$ and remains there.
4. Repeat part 3 for the case where $x_1$ suddenly changes from $0.4$ to $0.6$ (in addition to the change in $w_2$).
5. For parts 2 through 4, plot the normalized response $x_N(t)$,
$$x_N(t) = \frac{x(t)-x(0)}{x(\infty)-x(0)}$$
## Solution to Example 1
The "Systematic Approach for Developing Dynamic Models" will be followed, but some parts of it will be omitted: the degrees of freedom of analysis will be omitted since I have not learned that yet; inputs will not be classified as disturbance variables or as manipulated variables since these info will not be needed to solve the problem.
### Modelling Objectives
The goal is to model the stirred-tank blending process.
### Model end-use
- To determine the steady-state value of $x$. This steady-state value is denoted as $x(\infty)$
- To determine the response $x(t)$ for sudden changes in the inputes $w_1, w_2, x_1$.
### Schematic Diagram
(I dunno how to add images yet)
### Assumptions
- Constant holdup
- Constant density during mixing
- No reactions occur
### Conservation Equations
Why is this not working?

$x = 1.0 + y$

The only necessary conservation equation to be set up is the solute balance.
$$
\begin{align*}
    \frac{d\left(xw\right)}{dt} &= \left(x_1w_1 + x_2w_2\right)-xw\\
    \frac{d\left(x\cdot\rho V\right)}{dt} &= \left(x_1w_1 + x_2w_2 \right) - x\cdot\rho V\\
    \frac{dx}{dt} &= \frac{x_1w_1 + x_2w_2}{\rho V} - x
\end{align*}
$$
This is the general model; all variables are time-dependent. Special cases of the model will be used for parts 2 through 4. For instance, in part 2 all but $x$ and $w_1$ are constant, and $w_1$ is equivalent to a function involving the Heaviside function $u(t-a)$,

$$\begin{equation*}
    u(t-a)=
    \begin{cases}
        0, & \text{if } t < a\\
        1, & \text{if } t > a
    \end{cases}
\end{equation*}$$

### Steady state value of x
$$\begin{align*}
x
&= \frac{x_1w_1 + x_2w_2}{\rho V}\\
&= \frac{0.4(500) + 0.75(200)}{900(2)}\\
&= 0.1944
\end{align*}$$
### Response x(t) for sudden changes in w1, w2, x1
The following are the respective special cases of the general model corresponding to parts 2 through 4
$$\begin{align*}
    \frac{dx(t)}{dt} &= \frac{x_2w_2}{\rho V} + \frac{100x_1}{\rho V}\left[5-u(t-15)\right] - x(t)\\
    \frac{dx(t)}{dt} &= \frac{x_1w_1}{\rho V} + \frac{100x_2}{\rho V}\left[2-u(t-15)\right] - x(t)\\
    \frac{dx(t)}{dt} &= \frac{0.2w_1}{\rho V}\left[0.2 + u(t-15)\right] + \frac{100x_2}{\rho V}\left[2-u(t-15)\right] - x(t)
\end{align*}$$
These equations are easily solved using the Laplace transform method.<br/>
Math inline equation: $x_1, w_1, w_2$
