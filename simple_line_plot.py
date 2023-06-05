import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,11)
y = 2*x

plt.plot(x,y, color="b", linestyle=":", linewidth=4)
plt.title("line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
