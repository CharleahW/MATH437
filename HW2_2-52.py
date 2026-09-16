from scipy.optimize import linprog

#minimizing cost as matrix +: minimize & -: maximize
c=[30, 30, 30, 28, 28, 28, .9, .9, .9, .75, .75, .75]

#constraint leq matrices
A= [[.75, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, .75, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, .75, 0, 0, 1, 0, 0, 0, 0, 0, 0],
]
b= [3000, 3500, 3000]

#constraint eq matrices
Aeq =[
[1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -1, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
]

#is 5000[2] even the right number? lemme check
beq= [500, 5000, 750, 1000, 1200, 1200]

res =linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, method='highs')

if res.success:
    print("Optimization completed!")
    print(f"Optimal value for a1: {res.x[0]:.1f}")
    print(f"Optimal value for a2: {res.x[1]:.1f}")
    print(f"Optimal value for a3: {res.x[2]:.1f}")
    print(f"Optimal value for b1: {res.x[3]:.1f}")
    print(f"Optimal value for b2: {res.x[4]:.1f}")
    print(f"Optimal value for b3: {res.x[5]:.1f}")
    print(f"Optimal value for z1: {res.x[6]:.1f}")
    print(f"Optimal value for z2: {res.x[7]:.1f}")
    print(f"Optimal value for z3: {res.x[8]:.1f}")
    print(f"Optimal value for w1: {res.x[9]:.1f}")
    print(f"Optimal value for w2: {res.x[10]:.1f}")
    print(f"Optimal value for w3: {res.x[11]:.1f}")
    print(f"Minimum cost: {res.fun:.1f}")
else:
    print("Optimization failed!")
    print(res.message)