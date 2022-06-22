from  array import *

vals= array('i',[2,3,4,5,6,7,8])
newArr = array(vals.typecode, (a*a for a in vals))

i = 0
while i<len(newArr):
    print(newArr[i])
    i+=1