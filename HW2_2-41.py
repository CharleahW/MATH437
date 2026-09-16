import numpy as np
from scipy.optimize import linprog

#maximizing cost as matrix
c=[-1.2, -1.3, -0.8, -0.95, 0, 0, 0, -1.065, 0]

A= [[1, 1, 0, 1, 1, 0, 0, 0, 0]]
b= [10000]

#constraint  matrices
Aeq =[
[.5, .6, -1, 0.4, 1.065, -1, 0, 0, 0],
[.3, .2, .8, .6, 0, 1.065, -1, 0, 0],
[1.8, 1.5, 1.9, 1.8, 0, 0, 1.065, -1, 0],
[1.2, 1.3, .8, .95, 0, 0, 0, 1.065, -1],
]

beq= [0, 0, 0, 0]

res =linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, method='highs')

if res.success:
    print("Optimization completed!")
    print(f"Optimal value for x1: {res.x[0]:.1f}")
    print(f"Optimal value for x2: {res.x[1]:.1f}")
    print(f"Optimal value for x3: {res.x[2]:.1f}")
    print(f"Optimal value for x4: {res.x[3]:.1f}")
    print(f"Optimal value for y1: {res.x[4]:.1f}")
    print(f"Optimal value for y2: {res.x[5]:.1f}")
    print(f"Optimal value for y3: {res.x[6]:.1f}")
    print(f"Optimal value for y4: {res.x[7]:.1f}")
    print(f"Optimal investment: {-res.fun:.1f}")
else:
    print("Optimization failed!")
    print(res.message)