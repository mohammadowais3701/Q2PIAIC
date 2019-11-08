import numpy as np
import matplotlib.pyplot as p
x=np.arange(0,3*np.pi,0.01)
print(x)
y=np.sin(x)
print(y)
p.plot(y)
p.show()