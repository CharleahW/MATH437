from scipy.optimize import linprog

#maximizing profit as matrix +: minimize & -: maximize
#ugh: bp, bw, ws, wp, ps
c=[-150, 0, -200, 0, -230]
#molasses profit is just 35*400=14000

#constraint leq matrices
A= [[-1, 0, 0, 0, 0],
    [0, 0, -1, 0, 0],
    [0, 0, 0, 0, -1]
]
b= [-25, -25, -25]

#constraint eq matrices
Aeq=[[1, 1, 0, 0, 0],
     [0, -.8, 1, 1, 0],
     [0, 0, 0, -.95, 1]
]
beq=[1200, 0, 0]

res =linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, method='highs')

if res.success:
    print("Optimization completed!")
    print(f"Optimal brown sugar sold: {res.x[0]:.1f}")
    print(f"Optimal white sugar produced: {res.x[1]:.1f}")
    print(f"Optimal white sugar sold: {res.x[2]:.1f}")
    print(f"Optimal powdered sugar produced: {res.x[3]:.1f}")
    print(f"Maximum profit: {(-res.fun + 35*400):.1f}")
else:
    print("Optimization failed!")
    print(res.message)