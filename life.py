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
    #nextFile
    #nextGeneration(board,neighborArr,stayAlive,Born)

    
#Built in function reminders:
    #arr.reshape((H,W))
    #np.sum(arr)

##########
# Adjustable Variables
#########
create_file = True
generations = 50
num_of_simulations = 1
height = 10
width  = 10
numOfOnes = 50
maxBase = len(convertString) #~63 Largest base allowed 0-9, a-z, A-Z, _
wrap = True
#Rules : conwaylife.com/wiki/Cellular_automaton#Rules
stayAlive = [2,3,]
born= [3,]




        

######
##########.
# MAIN LOOP
#############
################

        
for x in range(num_of_simulations):
    print('Simulation number:',x)

      ##############################################
     ################################################
    #####     S E T   U P  C O D E               #####
     ################################################
       ############################################
       
    arr= generateArr(height*width,numOfOnes)

    board =arr.reshape((height,width))


    
    

    #Will create folders for different test cases
    if create_file:
        filePath ='Output/WxH{}x{}_{}Ones_WrapIs_{}_{}gens_stayAlive{}_born{}/'.format(
            width,height,numOfOnes,wrap,generations,str(stayAlive).replace(' ','').strip('[]'),str(born).replace(' ','').strip('[]'))

        #makes directory if needed
        mkdir_p(filePath)

        #Opens file and adds array to the top
        nextFileName = nextFileNameFunc(filePath)
        #uses numpy's function to get arround truncating arrays
        np.savetxt(filePath+nextFileName, board,fmt='%G')

    ##################################################
    ##################################################

    # Does actual game of life mechanics
    i=0
    while i <= generations:
        #adds current gen and total cells alive to file
        appendToFile(filePath,nextFileName,i,np.sum(board))
        #creates the neighbor array
        neighborArr=np.copy(countNeighbors(np.copy(board),height,width))
        #Generates the next generation
        board = nextGeneration(np.copy(board),neighborArr,stayAlive,born)

        i += 1


print('\n'*2)
print('##'*40)
