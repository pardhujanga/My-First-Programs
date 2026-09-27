import numpy as np
from matplotlib import pyplot as plt

p0 = 3
dt = 0.0001
p =p0
dp = 0
positions = []
for n in  range(1000000):
    ddp = -np.sin(p)
    p += dp*dt
    positions.append(p)
    dp += ddp*dt

plt.xlabel("10^-4 seconds")
plt.plot(positions)
plt.show()