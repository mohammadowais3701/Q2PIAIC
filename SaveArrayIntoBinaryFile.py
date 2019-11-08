import numpy as np
import os
a=np.arange(20)
np.save('temp_arr.npy',a)
if os.path.exists('temp_arr.npy'):
    x2=np.load('temp_arr.npy')
    print(np.array_equal(a,x2))
    print(x2)