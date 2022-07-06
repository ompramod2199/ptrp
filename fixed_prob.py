#PROGRAM ON FIXED PROBABILITY HEADS AND TAILS
import random
li = [0, 1]
head = 0
tail = 0
# input1=int(input("Enter"))
for i in range(0, 1000):
    n = random.choice(li)
    if(n):
        head += 1
    else:
        tail += 1

print("Probability of head count in percentage:", head/1000*100)

for i in range(0, 10000):
    n = random.choice(li)
    if(n):
        head += 1
    else:
        tail += 1

print("Probability of head count in percentage:", head/10000*100)

for i in range(0, 100000):
    n = random.choice(li)
    if(n):
        head += 1
    else:
        tail += 1

print("Probability of head count in percentage:", head/100000*100)