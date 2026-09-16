from scipy.optimize import linprog

#maximizing profit as matrix +: minimize & -: maximize
#i dont know if im smart enough to be here, why is my obj func longer thna the matrix?
c=[-1.0775, -1.19, -1.153]
#do i need to substract cost of can from profit?

#constraint leq matrices
A= [[0.5, 0.25, 0],
    [0, 0.25, 0.4],
    [0.5, 0.5, 0.6]
]
b= [400000, 200000, 300000]

#constraint eq matrices
Aeq=[[1, 1, ]

]

res =linprog(c, A_ub=A, b_ub=b, method='highs')

if res.success:
    print("Optimization completed!")
    print(f"Optimal cans produced for Drink A: {res.x[0]:.1f}")
    print(f"Optimal cans produced for Drink B: {res.x[1]:.1f}")
    print(f"Optimal cans produced for Drink C: {res.x[2]:.1f}")
    print(f"Maximum profit: {-res.fun:.1f}")
else:
    print("Optimization failed!")
    print(res.message)