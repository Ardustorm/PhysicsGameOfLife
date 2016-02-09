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
    #appendToFile(filePath,name,first column, second column)
        #mkdir_p(path) checks and creates path if it doesn't exist
    #locateNeighbors(cell,height,width) returns location of neighbors
    #countNeighbors(board,height,width) returns arr w/ # of neighbors @ each cell

    
#Built in function reminders:
    #arr.reshape((H,W))
    #np.sum(arr)

##########
# Adjustable Variables
#########
create_file = True
generations = 500
height = 50
width  = 50
numOfOnes = 1200
maxBase = len(convertString) #~63 Largest base allowed 0-9, a-z, A-Z, _
wrap = True

stayAlive = [2,3,]
born= [3,]
    
################
#############
# SET UP
##########
######


arr= generateArr(height*width,numOfOnes)
#print('1D array: {}'.format(arr))



# testBoard = [[0, 1, 0, 0, 0, 0],
#              [0, 0, 1, 0, 0, 0],
#              [1, 1, 1, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0]]

#board = np.array(testBoard)
board =arr.reshape((height,width))


name =toBaseN(arrToNum(arr),maxBase)    #takes array, turns it into max base num
name = name+ '.csv'          # Creates file with name

#Will create folders for different test cases
if create_file:
    filePath = 'Output/WxH'+str(width)+'x'+str(height) + \
               '_'+ str(numOfOnes)+'Ones_wrapIs_' + str(wrap) + str(generations)+ 'gens/'

    #makes directory if needed
    mkdir_p(filePath)

    #Opens file and adds array to the top
    nextFileName = nextFileName(filePath)
    #uses numpy's function to get arround truncating arrays
    np.savetxt(filePath+nextFileName, board,fmt='%G')

# testFile = open(filePath+nextFileName,'a')
# testFile.write('{}\n'.format(name))
# testFile.write('{}\n'.format(board))
# testFile.close()


print('##'*40),
print('filename: {}'.format(name))
print('\n')
print('Starting Board:\n{}'.format(board))
print('\n')

######
##########.
# MAIN LOOP
#############
################
      
def nextGeneration(board,neighborArr):
    # Goes through board array and checks neighbor array against the stay Alive
    # values. Then checks the dead cells to see if they come alive

    
    #https://docs.scipy.org/doc/numpy/reference/arrays.nditer.html
    current_cell = np.nditer(board, flags=['multi_index'])
    while not current_cell.finished:      # Wait till it goes through it all,


        if(current_cell[0] == 1 and (neighborArr[current_cell.multi_index] in stayAlive)):
           #print('it stays alive')
            board[current_cell.multi_index]=1
        elif(current_cell[0] == 1 and (neighborArr[current_cell.multi_index] not in stayAlive)):
            #rint('its dead')
            board[current_cell.multi_index]=0
        elif(current_cell[0] == 0 and (neighborArr[current_cell.multi_index] in born)):
            board[current_cell.multi_index]=1
           #print('Its born')
        else:
           #print('i broke it')
            pass
             
        current_cell.iternext()
    return board


i=0
while i <= generations:
    #adds current gen and total cells alive to file
    appendToFile(filePath,nextFileName,i,np.sum(board))
    #creates the neighbor array
    neighborArr=np.copy(countNeighbors(np.copy(board),height,width))
    #Generates the next generation
    board = nextGeneration(np.copy(board),neighborArr)

    i += 1


    
#print(neighbors)          

print('\n'*2)
print (board)


print('##'*50)
