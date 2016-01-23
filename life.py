
from lifeFuncs import *


import numpy as np

#Avalible Funcs:
    #generateArr(total,ones) returns a 1d array
    #arrToNum(arr) returns the num in base 10
    #toBaseN(num,base)  returns num in new base
    #fromBaseNToDec(string,base) returns num in base 10

    
#Built in function reminders:
    #arr.reshape((a,b))
    #np.sum(arr)


def appendToFile(name,a,b):
    testFile = open(filePath,'a')
    testFile.write('{}, {}\n'.format(a,b))
    testFile.close()


    


print('##'*50),
print('\n')

arr= generateArr(100,50)

name =toBaseN(arrToNum(arr),36)    #takes array, turns it into base 36 num
filePath = 'Output/'+name+ '.csv'          # Creates file with name

print(name)

i=0
while i <= 10:
    appendToFile(name,i,np.random.randint(0,10))
    i = i+1
    
new = arr.reshape((10,10))
print(new)

print(np.sum(new))

print('##'*50)
