import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx**2+yy**2)/(xx**2+yy**2)

plt.figure(1)
plt.clf()
print xx.min(), xx.max(), yy.min(), yy.max()
plt.imshow(z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')
plt.show()