import numpy as np
from scipy.optimize import linprog

#maximizing profit as matrix
#x11 x12 x13 x21 x22 x23 x31 x32 x33
c=[-4.5, -4.5, -4.5, -5, -5, -5, -4, -4, -4]


#constraint  matrices
A= [[10, 6, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 8, 10, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 6, 9, 12]
]
b= [600, 600, 600]
res =linprog(c, A_ub=A, b_ub=b, method='highs')

if res.success:
    print("Optimization completed!")
    print(f"Optimal value for x11: {res.x[0]:.3f}")
    print(f"Optimal value for x12: {res.x[1]:.3f}")
    print(f"Optimal value for x13: {res.x[2]:.3f}")
    print(f"Optimal value for x21: {res.x[3]:.3f}")
    print(f"Optimal value for x22: {res.x[4]:.3f}")
    print(f"Optimal value for x23: {res.x[5]:.3f}")
    print(f"Optimal value for x31: {res.x[6]:.3f}")
    print(f"Optimal value for x32: {res.x[7]:.3f}")
    print(f"Optimal value for x33: {res.x[8]:.3f}")
    print(f"Optimal investment: {-res.fun:.3f}")
else:
    print("Optimization failed!")
    print(res.message)