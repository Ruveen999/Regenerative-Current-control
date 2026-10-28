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
plt.plot(time, ref_current)
plt.xlabel("Time (s)")
plt.ylabel("Reference current (A)")
plt.title("Desired Current Waveform")
plt.grid(True)
plt.tight_layout()
plt.show()
