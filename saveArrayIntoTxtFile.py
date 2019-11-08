import numpy as np
import os
x=np.arange(12).reshape(3,4)
header="col1 col2 col3 col4"
np.savetxt('temp.txt',x, fmt="%d",header=header)
results=np.loadtxt('temp.txt')
print(results)