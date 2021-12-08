# -*- coding: utf-8 -*-
"""Gambler's Ruin.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QVXbilHS8zwF3f4_NeL-SH8gy1nwFPHy
"""

import numpy as np
import random
import matplotlib.pyplot as plt

N = 100
q = 0.6
p = 1 - q
init = np.arange(0,101,1)

prob = [q,p]

times = []
went_to_N = []
for i in init:
  time = []
  vals = []
  runs = 100
  for j in range(runs):
    next_val = i
    k = 0
    while(True):
      if(next_val==0):
        break
      if(next_val==N):
        break
      rr = random.random()
      if(rr<prob[0]):
        next_val -= 1
      else:
        next_val += 1
      k += 1
    time.append(k)
    vals.append(next_val)
  j = 0
  for val in vals:
    if(val==N):
      j+=1
  went_to_N.append(j/runs)
  times.append(sum(time)/len(time))
plt.plot(init,times)
plt.title('Initial money at hand v/s \n Average number of steps required to reach 0 or $N$')
plt.xlabel('Initial money at hand')
plt.ylabel('Average number of steps \n required to reach 0 or $N$')
plt.show()

runs = 1000
N = 100
q = 0.6
n = 500
vals = np.zeros(n)
dict = {True:1, False:-1}       
for num in range(n):
  for r in range(runs):
    next_val = 25
    for j in range(num):
      next_val += dict[random.uniform(0,1)>q]
      if((next_val == 0) or (next_val == N)):
        vals[num] += 1
        break
probs = duration/runs
plt.plot(np.arange(n), probs)
plt.xlabel('n (Step number)')
plt.title('Step number v/s $a_{kn}+b_{kn}$')
plt.ylabel('$a_{kn}+b_{kn}$')
plt.show()
plt.hist(probs)
plt.xlabel('n (Step number)')
plt.title('Step number v/s $a_{kn}+b_{kn}$')
plt.ylabel('$a_{kn}+b_{kn}$')
plt.show()