import numpy as np
import matplotlib.pyplot as plt
import math
V= 20
R = 2
L = 0.1
Initial_Current = 0
t = np.linspace(0,0.3,601)
tau = L/R
Transient_Current = (V/R)*(1 - np.exp(-t/tau))
print(f"The final current is: {Transient_Current}")
print(F"Value of time constant is: {tau}")
plt.plot(t, Transient_Current, label="Analytical current")
plt.axhline(V / R, color="gray", linestyle="--", label="Steady-state current")

plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("Current Response of a Series RL Circuit")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()