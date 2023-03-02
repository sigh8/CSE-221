import time
import math
import matplotlib.pyplot as plt
import numpy as np
import task3a as ba
import task3b as ha
inp = open('input3.txt', mode='r')
data = inp.readlines()
q= []
n = 30
x = [i for i in range(n)]
y = [0 for i in range(n)]
z = [0 for i in range(n)]
for i in range(n-1):
    start = time.time()
    ba.appointment(data, q)
    y[i+1]= time.time()-start
    start = time.time()
    ha.appointment(data, q)
    z[i+1]= time.time()-start
x_interval = math.ceil(n/10)
plt.plot(x, y, 'r')
plt.plot(x, z, 'b')
plt.xticks(np.arange(min(x), max(x)+1, x_interval))
plt.xlabel('n-th position')
plt.ylabel('time')
plt.title('Comparing Time Complexity!')
plt.show()