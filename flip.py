import random
random.seed(0)

N = 1000
H = 0
T = 0
while H+T < N:
    x=random.uniform(0.0, 1.0)
    if x < 0.5:
        H += 1
    else:
        T += 1
print(f"After {N} attempts, there were {H} heads and {T} tails.")