import numpy as np 
import matplotlib.pyplot as plt
time = np.arange(0,0.4,0.001)
ref_current = []

for i in time:
    if i >= 0 and i <= 0.1:
        current = 20 * i    #case for ramp up
    elif i> 0.1 and i< 0.2 :
        current = 2         # case for hold
    elif i>= 0.2 and i< 0.3:
        current = 2 - 20*(i - 0.2)
    else:
        current = 0
    ref_current.append(current)
ref_current = np.array(ref_current)

Initial_Current = 0

Actual_Current = np.zeros(len(time))

Actual_Current[0] = Initial_Current

error = np.zeros(len(time))

for i in range(len(time) -1 ):
    error[i] = ref_current[i] - Actual_Current[i]








