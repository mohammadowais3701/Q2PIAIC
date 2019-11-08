import numpy as np

arr1=np.empty(9).reshape(3,3)
arr2=np.ones(9).reshape(3,3)
arr1=arr2+5
print(arr1)
print(arr2)
list1=[0,12,45.12,34,99.91]
arr3=np.array(list1)
arr4=np.empty(len(arr3))
for i in range(len(arr4)):
    arr4[i]=arr4[i]+(arr3[i]*1.8000+32.00)
print(arr3)
print(arr4)