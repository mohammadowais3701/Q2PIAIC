import matplotlib.pyplot as plt
import numpy as np

#plt.plot(['a','b','c','d','e'],[2,6,8,5,1])
#x=np.arange(1,8,0.01)
#for i in x:
#    print(i)
#plt.plot(x,x)
#plt.plot(x,[i**2 for i in x ])
#plt.plot(x,[i**3 for i in x])


x=np.arange(1,5)
plt.plot(x,x*1.5,label='medium')
plt.plot(x,x*3.0,label='fast')
plt.plot(x,x/3.0,label='slow')
plt.axis([0,8,0,15])
plt.xlabel("X_AXIS")
plt.ylabel("Y_AXIS")
plt.title("Plotting")
plt.legend(loc=6)

plt.show()
