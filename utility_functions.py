import numpy as np

def norm(v1, v2):
    # this function finds the Euclidean distance between two 2D vectors
    # inputs: 
    #        v1 : (list) coordinates of vector 1
    #        v2 : (list) coordinates of vector 2
    # outputs:
    #        dist : (float) the Euclidean distance between v1 & v2
    
    dist =  np.sqrt((v1[0]- v2[0])**2 + (v2[1]-v1[1])**2)
    return dist

