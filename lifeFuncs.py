import errno    #these 2 lines are needed to make subdirectories that don't exist
import os

import numpy as np

# Used when converting arrays to filenames. Results in bas ~63
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



def locateNeighbors(cell,height,width):
    
    # a 3x3 array to store which neighbors to check
    #                     (horizontal, vertical)
    neighbors =np.array( [[[-1, -1], [-1, 0], [-1, 1]],
                          [[0, -1], [0, 0], [0, 1]],
                          [[1, -1], [1, 0], [1, 1]]])
    
    #replaces all values with location related to cell
    neighbors[:,:,0] += cell[0]
    neighbors[:,:,1] += cell[1]

    # Then we check to see if it is on the edge and fix it if it is
    
    #0th row in array
    if(cell[0]==0):
        #Replace the 0th row of nighbor with the bottom row
        neighbors[0, :, 0] =  (height-1)


    #last row in array
    elif(cell[0] == height-1):
        #if cell is on bottom, its neigbor below are in the first row
        # make the value -cell so that when i add cell to everything,
        # it equals zero
        neighbors[2, :, 0] = 0


  #0th column in array
    if(cell[1]==0): 
        #Replace the 0th column of nighbor with the 0th col (-cell #)
        #I subtract cell so that I can just add cell to everything
        # without needing to check first
        neighbors[:, 0, 1] =  (width-1)

    #0th column in array
    elif(cell[1]==width-1): 
        #Replace the 0th column of nighbor with the 0th col (-cell #)
        #I subtract cell so that I can just add cell to everything
        # without needing to check first
        neighbors[:, 2, 1] = 0

    return neighbors






def countNeighbors(board,height,width):
    oldBoard = np.copy(board) # stores a copy of the board while writing
    
    for cell, state in np.ndenumerate(oldBoard):
        neighborLocations = locateNeighbors(cell,height,width)
       
        totalNeighbors=0 #Resets for each cell
        for neighborRow in neighborLocations:
            for currentNeighbor in neighborRow:
                #This loop runs through each neighbor and sums them
                if not(np.array_equal(currentNeighbor, cell)): #ignores itself
                    totalNeighbors +=  oldBoard[currentNeighbor[0],
                                                currentNeighbor[1]]

            board[cell]=totalNeighbors #sets board to represent neighbors
    return board
