import errno    #these 2 lines are needed to make subdirectories that don't exist
import os

import numpy as np

convertString= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"

def mkdir_p(path):
    #stackoverflow.com/questions/600268
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def appendToFile(filePath,name,a,b):
    mkdir_p(filePath)
    testFile = open(filePath+name,'a')
    testFile.write('{}, {}\n'.format(a,b))
    testFile.close()



def generateArr(total,ones):
    #
    #based on code from:
    #stackoverflow.com/questions/19597473/
    arr = np.array([1]*ones + [0]*(total-ones))
    np.random.shuffle(arr)
    return arr

def arrToNum(arr):
#converts array to number
    #Based of of code from here:
    #stackoverflow.com/questions/489999/
    num = map(str,arr) #['1','2','3']
    num = ''.join(num) # '123'
    num = int(num,2)     #  123
    return num

def toBaseN(num,base):
#converts number to a string of base N:
    if num < base:
        return convertString[num]  #returns when single digit
    else:
        return toBaseN(num//base,base) + convertString[num%base]

def fromBaseNToDec(string,base,position=1):
    #positon keeps track of the (1's, 10's, 100's, etc)
    #position is used internally, the user doesnot see/use it
    #it also can do binary (2's, 4's, 8's,etc)
    if len(string)<=1:
        return convertString.find(string[-1])*position
    else:
        return fromBaseNToDec(string[:-1],base,position*base) + \
            convertString.find(string[-1])*position

"""
test = input('num  ')
base = int(input('base '))

print(fromBaseNToDec(test,base))

    ##1T3
"""


