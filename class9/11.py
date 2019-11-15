#string input and length should be b/w 2 and 8 . if all 0 reject .only one decimal allow.
import re

pattern='[0-1]'

string=input("Enter Binary number b/w 2 and 8 ")

l=len(string)
check=re.search(pattern,string)
print(check)
if(l>8 or l<2):
    print("Not Reasonable")
elif(not(check)):
    print("Invalid")
elif(re.search('[0]',string)):
    print('Not Reasonable')

