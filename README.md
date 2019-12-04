### Simulation of RLC Series Circuit using Numerical Methods
<p align='center'>
<img src='circuit.png' height=200>
</p>
This repositoy focuses on solving for the current of the above circuit during the transient state.

The differential equation obtained for solving the current is as follows.

<a href="https://www.codecogs.com/eqnedit.php?latex=L\frac{\mathrm{d}^2&space;i(t)}{\mathrm{d}&space;t^2}&space;&plus;&space;R\frac{\mathrm{d}&space;i(t)}{\mathrm{d}&space;t}&space;&plus;&space;\frac{i(t)}{c}&space;=&space;\frac{\mathrm{d}&space;v(t)}{\mathrm{d}&space;t}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?L\frac{\mathrm{d}^2&space;i(t)}{\mathrm{d}&space;t^2}&space;&plus;&space;R\frac{\mathrm{d}&space;i(t)}{\mathrm{d}&space;t}&space;&plus;&space;\frac{i(t)}{c}&space;=&space;\frac{\mathrm{d}&space;v(t)}{\mathrm{d}&space;t}" title="L\frac{\mathrm{d}^2 i(t)}{\mathrm{d} t^2} + R\frac{\mathrm{d} i(t)}{\mathrm{d} t} + \frac{i(t)}{c} = \frac{\mathrm{d} v(t)}{\mathrm{d} t}" /></a>

### Exact Solution
The exact solution of the above differential equation according to wolfram alpha is:
<p align='center'>
<img src='Exact Solution.png' height=200>
</p>

[Euler's method](https://en.wikipedia.org/wiki/Euler_method) is used to implement the numerical solution for the above equation which after a certain extent outputs nearly exact solution with not much computational power. 
This [article](https://medium.com/@afhamaflal9/numerical-solution-to-rlc-series-circuit-with-constant-and-varying-source-11637e05e8c) contains further information.
