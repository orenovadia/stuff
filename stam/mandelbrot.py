import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3, 3, 0.005)
y = np.arange(-3, 3, 0.005)
xx, yy = np.meshgrid(x, y)
z = xx + yy*1j
z0 = z.copy()
m = np.zeros_like(z)
onez = np.ones_like(z)
zeroz = np.zeros_like(z)

for i in range(12):
    z = z**2 + z0
    m += np.where(abs(z)>10,onez,zeroz)
plt.figure(1)
plt.clf()
plt.imshow(abs(m), interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')
plt.show()