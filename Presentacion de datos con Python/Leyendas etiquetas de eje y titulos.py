import numpy as np
import matplotlib.pyplot as plt

fig, pan_1 = plt.subplots(1, 1)

x1 = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x)

pan_1.plot(x, y)
