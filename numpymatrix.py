import numpy as np
m1=[[1,2],[3,4]]
m2=[[3,4],[8,9]]
result=np.dot(m1,m2)
print(result)
vectorPro=np.outer(m1,m2)
print(vectorPro)
crossPro=np.cross(m2,m1)
print(crossPro)
det=np.linalg.det(m1)
print("determinant")
print(det)