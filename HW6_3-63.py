import numpy as np
from scipy.optimize import linprog

#maximizing cost as matrix
c=[-2, -3]


#constraint  matrices
A= [[3, -2],
    [2, 6],
]
b= [8, 18]
res =linprog(c, A_ub=A, b_ub=b, method='highs')

if res.success:
    print("Optimization completed!")
    print(f"Optimal value for x1: {res.x[0]:.3f}")
    print(f"Optimal value for x2: {res.x[1]:.3f}")
    print(f"Optimal investment: {-res.fun:.3f}")
else:
    print("Optimization failed!")
    print(res.message)