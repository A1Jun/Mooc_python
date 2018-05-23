#CalPiV1.py

from random import random

from time import perf_counter

DARTS = 1000*1000

hits = 0.0

start = perf_counter()

for i in range(1, DARTS+1):

    x, y = random(), random() #随机点的坐标

    dist = pow(x ** 2 + y ** 2, 0.5) #点到圆心的距离

    if dist <= 1.0:   #判断点是否在圆里

        hits = hits + 1   #圆内点数量

pi = 4 * (hits/DARTS)

print("圆周率值是:{}".format(pi))

print("运算时间是: {:.5f}s".format(perf_counter()-start))
