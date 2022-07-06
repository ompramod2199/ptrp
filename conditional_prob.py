#PROGRAM ON CONDITIONAL PROBABILITY
import random

a = [0, 1]
b = [0, 1]
atleast = 0
head_count = 0
notr = int(input())
for i in range(notr):
    n1 = random.choice(a)
    if(n1 == 0):
        n2 = 1
        atleast += 1
        continue
    else:
        n2 = random.choice(b)
        if(n2 == 1):
            head_count += 1
        else:
            atleast += 1
            continue
print((head_count/atleast)*100)
