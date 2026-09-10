from scipy.optimize import linprog

#maximizing cost as matrix
c=[-30, -20, -50]

#constraint leq matrices
A= [[-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1],
    [2, 3, 5],
    [4, 2, 7],
    [1, .5, .33]]
b= [-200, -200, -150, 4000, 6000, 1500]

#constraint eq matrices
Aeq =[
[-2, 3, 0],
[0, -5, 2]
]

beq= [0, 0]

res =linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, method='highs')

if res.success:
    print("Optimization completed!")
    print(f"Optimal value for x1: {res.x[0]:.1f}")
    print(f"Optimal value for x2: {res.x[1]:.1f}")
    print(f"Optimal value for x3: {res.x[2]:.1f}")
    print(f"Optimal profit: {-res.fun:.1f}")
else:
    print("Optimization failed!")
    print(res.message)