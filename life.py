#NOTES
# Have a padding arround the array to do wrapping
# This is much faster then trying to check the otherside
# http://www.gamedev.net/page/resources/_/technical
# /graphics-programming-and-theory/graphics-programming-black-book-r1698
from lifeFuncs import *


import numpy as np

#Avalible Funcs:
    #generateArr(total,ones) returns a 1d array
    #arrToNum(arr) returns the num in base 10
    #toBaseN(num,base)  returns num in new base
    #fromBaseNToDec(string,base) returns num in base 10    Should make it return array
    #appendToFile(filePath,first column, second column)
        #mkdir_p(path) checks and creates path if it doesn't exist
    #

    
#Built in function reminders:
    #arr.reshape((H,W))
    #np.sum(arr)

##########
# Adjustable Variables
#########
height = 10
width  = 20
numOfOnes = 50
maxBase = len(convertString) #~63 Largest base allowed 0-9, a-z, A-Z, _
wrap = False

    


print('##'*50),
print('\n')

arr= generateArr(height*width,numOfOnes)

name =toBaseN(arrToNum(arr),maxBase)    #takes array, turns it into max base num

#Will create folders for different test cases
filePath = 'Output/WxH'+str(width)+'x'+str(height) + \
'_Ones'+ str(numOfOnes)+ '_wrapIs' + str(wrap) + '/'
name = name+ '.csv'          # Creates file with name

print(name)
board = arr.reshape((height,width))


i=0
while i <= 10:
    appendToFile(filePath,name,i,np.sum(board))
    i += 1
    
print (board)
print(np.sum(board))

print('##'*50)
