import numpy as np
from scipy.optimize import linprog

#maximizing cost as matrix
c=[-1, -1, -1]


#constraint  matrices
A= [[3, 5, 6],
    [5, 3, 4],
    [-1, -1, -1]
]
b= [1000, 1200, 1500]
res =linprog(c, A_ub=A, b_ub=b, method='highs')

if res.success:
    print("Optimization completed!")
    print(f"Optimal value for x1: {res.x[0]:.1f}")
    print(f"Optimal value for x2: {res.x[1]:.1f}")
    print(f"Optimal value for x3: {res.x[2]:.1f}")
    print(f"Optimal investment: {-res.fun:.1f}")
else:
    print("Optimization failed!")
    print(res.message)