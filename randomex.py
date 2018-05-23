#Randominfo.py

import random

a = [1,2,3,4,5,6,7,8,9,0]
c = random.choice(a)
print(c)
random.shuffle(a)
print(a)
random.seed(10)
s = random.random()
print(s)
