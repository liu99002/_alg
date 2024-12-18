import numpy as np
import random
step = 0.01

def f(x,y,z):
    return 3*x**2+y**2+2*z**2

def int3(f ,rx,ry,rz):
    area = 0.0
    for x in np.arange(rx[0], rx[1], step):
        for y in np.arange(ry[0], ry[1], step):
            for z in np.arange(rz[0], rz[1], step):
                area += f(x,y,z)*step**3
    return area

print(int3(f,[0,1],[0,1],[0,1]))


upper = 10
lower = 0

def mcInt(f, rfrom, rto, n=100000):
    hits = 0
    for i in range(0, n):
        x = random.uniform(rfrom[0], rto[0])
        y = random.uniform(rfrom[1], rto[1])
        z = random.uniform(rfrom[2], rto[2])
        fz = random.uniform(0, upper)
        if f(x,y,z)>fz:
            hits += 1
    return (rto[0]-rfrom[0])*(rto[1]-rfrom[1])*(rto[2]-rfrom[2])*(upper-lower)*hits/n

print(mcInt(f, [0,0,0], [1,1,1]))