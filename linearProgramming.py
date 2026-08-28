import random
random.seed(0)

n= 1000
h=0
t=0

for _ in range(n):
    flip = random.choice(['H', 'T'])
    if flip =='H':
        h += 1
    else:
        t += 1

print(f"After {n} flips, there were {h} heads and {t} tails.")