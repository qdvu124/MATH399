import numpy as np
from state import State

class Vertex:
    # this class creates a vertex within the SG 
    
    def __init__(self, xpos, ypos):
        self.r = [xpos, ypos]
        self.ns = [] #this is list of the neighbors of the vertex
        self.d = np.random.randint(-2,1) #this is the direction that the edge is pointing in the rotor router algorithm
        self.state = State.NOT_VISITED #initialize the vertex as not being visited yet
        self.occ = False #this boolean property determines whether of or not the vertex is occupied by a particle
        self.level = int(round((self.r[0] + self.r[1]/np.sqrt(3)))+ 1) # this is the "sphere" that the vertex lies on
        self.row = int(round((self.r[0]-self.r[1]/np.sqrt(3)) + 1)) # this is the row intersecting the spheres

    def __str__(self):
        return 'x: ' +str(self.r[0]) + ' y: ' + str(self.r[1])
        
    def __eq__(self, other): 
        return self.r[0] == other.r[0] and self.r[1] == other.r[1]

