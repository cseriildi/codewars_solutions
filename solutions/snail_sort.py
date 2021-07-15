# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
#array = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
#snail(array) #=> [1,2,3,6,9,8,7,4,5]

import numpy as np

def snail(snail_map):

    if len(snail_map) == 1: #if the input is 1x1 or empty array
        return snail_map[0] 
    else:
        snail_map = np.array(snail_map) #list to numpy array
        result = []
        isReverse = False
        
        while len(snail_map)>=1:
            if isReverse:
                result.extend(snail_map[-1][::-1]) # add to the result the reversed last row of the array
                snail_map = snail_map[:-1] # delete the last row from the array
            else:
                result.extend(snail_map[0]) # add to the result the first row of the array
                snail_map = snail_map[1:] # delete the first row from the array
                
            if isReverse:
                result.extend(snail_map[:,0][::-1]) # add to the result the reversed first column of the array
                snail_map = np.delete(snail_map, 0, 1) # delete the first column from the array
                
            else:
                result.extend(snail_map[:,-1]) # add to the result the last column of the array
                snail_map = np.delete(snail_map, -1, 1) # delete the last column from the array
                
            isReverse = not isReverse 
            
    return result