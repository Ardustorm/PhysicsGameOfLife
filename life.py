#NOTES
# Have a padding arround the array to do wrapping
# This is much faster then trying to check the otherside
# http://www.gamedev.net/page/resources/_/technical
# /graphics-programming-and-theory/graphics-programming-black-book-r1698
from lifeFuncs import *

from operator import add

import numpy as np

#Avalible Funcs:
    #generateArr(total,ones) returns a 1d array
    #arrToNum(arr) returns the num in base 10
    #toBaseN(num,base)  returns num in new base
    #fromBaseNToDec(string,base) returns # in base10  Should make it return array
    #appendToFile(filePath,first column, second column)
        #mkdir_p(path) checks and creates path if it doesn't exist
    #locateNeighbors(cell,height,width) returns location of neighbors
    #countNeighbors(board,height,width) returns arr w/ # of neighbors @ each cell

    
#Built in function reminders:
    #arr.reshape((H,W))
    #np.sum(arr)

##########
# Adjustable Variables
#########
height = 50
width  = 50
numOfOnes = 2400
maxBase = len(convertString) #~63 Largest base allowed 0-9, a-z, A-Z, _
wrap = True

stayAlive = [2,3,]
born= [3,]
    
################
#############
# SET UP
##########
######

print('##'*40),

arr= generateArr(height*width,numOfOnes)
#print('1D array: {}'.format(arr))

name =toBaseN(arrToNum(arr),maxBase)    #takes array, turns it into max base num

#Will create folders for different test cases
filePath = 'Output/WxH'+str(width)+'x'+str(height) + \
'_Ones'+ str(numOfOnes)+ '_wrapIs' + str(wrap) + '/'
name = name+ '.csv'          # Creates file with name

print('filename: {}'.format(name))
print('\n')

testBoard = [[1, 1, 1, 1, 1, 1],
             [1, 0, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 0]]

#board = np.array(testBoard)
board =arr.reshape((height,width))

print('Starting Board:\n{}'.format(board))
print('\n')

######
##########
# MAIN LOOP
#############
################

i=0
while i <= 1:
    #appendToFile(filePath,name,i,np.sum(board))
    neighborsArr=countNeighbors(board,height,width)
    print('Neighbors:\n{}'.format(neighborsArr))

 
    
    i += 10


#print(neighbors)          

print('\n'*2)
print('number of neighbors each cell has:')
print (board)
print(np.sum(board))

print('##'*50)
