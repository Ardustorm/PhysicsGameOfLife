
import numpy as np

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
    convertString= "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num < base:
        return convertString[num]  #returns when single digit
    else:
        return toBaseN(num//base,base) + convertString[num%base]

def fromBaseNToDec(string,base,position=1):
    #positon keeps track of the (1's, 10's, 100's, etc)
    #position is used internally, the user doesnot see/use it
    #it also can do binary (2's, 4's, 8's,etc)
    convertString= "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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


