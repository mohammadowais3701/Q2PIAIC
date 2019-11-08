import numpy as np
string="Sarah: Hello Jason, how are you, it's been a long time since we last met Jason: Oh, hi Ms. Sarah I'm have got a new job now and is going great."
list1=string.split(" ")
arr=np.array(list1)

lnth=np.vectorize(len)
print(lnth)
print(arr[lnth(arr)<6])
#print(arr[(np.vectorize(len))(arr)<5])
#list3=len(arr)<5
#print(list3)
#for i in list1:

 #   list3=list3+i.split(" ")
#for i in range(len(list3)):
 #   if(len(list3[i])<5 and len(list3[i])>0 ):
       # print(list3[i])
#list2=np.array(list3)

#print(list3)

list3=np.empty([2,3])
arr1=np.array([[1,2,3],[6,7,8]])#yaha broadcasting ho rahi hai 
arr2=np.array([2,3,4])
arr3=arr1*arr2
#print(arr3)
#print ntlk 
arr=np.array([2,3,4,0])
print(arr)
m=[2,3,]
b=arr>2
print(b.all(),arr.all())
