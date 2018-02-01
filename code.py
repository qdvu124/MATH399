import matplotlib.pyplot as plt
# %matplotlib inline                    
# comment out previous if not using ipython
import numpy as np
import random
from datetime import datetime
from enum import Enum
import time

class State(Enum):
    # Enumeration of possible states in Wilson's algorithm
    NOT_VISITED = 'NOT VISITED'
    EXPLORED = 'EXPLORED'
    VISITED = 'VISITED'

class Stack:
    # Stack to implement Wilson's algorithm
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class particle():
    # this class creates a particle object that walks around a graph. its only property is the vertex object it occupies
    
    def __init__(self, vs):
        self.pos = vs['1']
        
class vertex:
    # this class creates a vertex within the SG 
    
    def __init__(self,xpos, ypos):
        self.r = [xpos, ypos]
        self.ns = [] #this is list of the neighbors of the vertex
        self.d = random.randint(-2,1) #this is the direction that the edge is pointing in the rotor router algorithm
        self.state = State.NOT_VISITED #initialize the vertex as not being visited yet
        self.occ = False #this boolean property determines whether of or not the vertex is occupied by a particle
        self.level = int(round((self.r[0] + self.r[1]/np.sqrt(3)))+ 1) # this is the "sphere" that the vertex lies on
        self.row = int(round((self.r[0]-self.r[1]/np.sqrt(3)) + 1)) # this is the row intersecting the spheres
        
    def __eq__(self, other): 
        return self.r[0] == other.r[0] and self.r[1] == other.r[1]

def trisize(G):
    #This function determines the overall side length of the gasket G
    #
    # inputs: 
    #        G : a list of vertices of the generated SG
    # outputs:
    #        M : an integer telling the length of a side in vertex units of the generated SG 
    
    M = 0
    for coor in G:
        x = coor[0]
        if x > M:
            M = x
    return M

def tripler(G):
    # This functions takes a gasket and runs one recursive cycle to increase the size of the SG
    # inputs: 
    #        G : a list of vertices of the generated SG
    # outputs:
    #        trip_G : the new list of vertices once G is tripled
    
    trip_G = []
    size = trisize(G)
    for coor in G:
        x = coor[0]
        y = coor[1]
        # copy over G so far
        trip_G.append(coor)
        
    for coor in G:
        x = coor[0]
        y = coor[1]       
        # copy G to the right
        if x > 0: # as to not repeat vertices (.1 is just in case there are float point errors)
            x_new = size + x
            trip_G.append([x_new, y])
        
        # copy G above
        if x > 0 and x < size:
            x_new = x + size/2
            y_new = y + size*np.sqrt(3)/2
            trip_G.append([x_new, y_new])
    
    return trip_G

def generate(n):
    # this function generates the SG list of vertices
    # inputs: 
    #        n : (int) number of levels of recursion
    # outputs:
    #        G : (list) a lit of vertices of the generated SG
    
    G = [[0,0], [1,0], [.5, np.sqrt(3)/2]] #n = 1 Gasket
    for i in range(n-1):
        G = tripler(G)
    return G

def plotting(vs, G):
    # this function plots the SG with occupied vertices blue and unoccupied red.
    # inputs: 
    #        G : a list of vertices of the generated SG
    #        vs : (dictionary) dictionary of vertex objects
    #        size : side length of SG
    # outputs:
    #        figure(): plot of the SG
    
    size = trisize(G)
    
    for v in vs:
        if vs[v].occ:
            for v2 in vs[v].ns:
                if v2.occ:
                    xs = [vs[v].r[0], v2.r[0]]
                    ys = [vs[v].r[1], v2.r[1]]
                    plt.plot(xs, ys, color='blue', linewidth='1')

        if not(vs[v].occ):
            for v2 in vs[v].ns:
                if not(v2.occ):
                    xs = [vs[v].r[0], v2.r[0]]
                    ys = [vs[v].r[1], v2.r[1]]
                    plt.plot(xs, ys, color='red', linewidth='1')
    
    plt.xlim(-size*.1, size * 1.1)
    plt.ylim(-size*.1, size)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.draw()
    plt.show()

def wilson(vs, G):
    size = trisize(G)
    wilson_stack = Stack()

    # color the graph blue first
    for v in vs:
        for v2 in vs[v].ns:
            xs = [vs[v].r[0], v2.r[0]]
            ys = [vs[v].r[1], v2.r[1]]
            plt.plot(xs, ys, color='white', linewidth='1')
    
    starting_vertex = select_unvisited_vertex(vs)
    starting_vertex.state = State.VISITED
    cover_count = 1

    # while we still do not have a spanning tree yet, i.e some vertices are not yet covered
    while cover_count < len(vs):
        current_vertex = select_unvisited_vertex(vs)
        current_vertex.state = State.EXPLORED
        wilson_stack.push(current_vertex)
        # begin the random walk starting at this
        while True:
            current_vertex = select_neighbor(current_vertex)
            # we have encountered some vertex that we have already visited. Begin adding vertices to tree
            if current_vertex.state == State.VISITED:
                start = current_vertex
                while not(wilson_stack.isEmpty()):
                    end = wilson_stack.pop()
                    end.state = State.VISITED
                    cover_count = cover_count + 1
                    xs = [start.r[0], end.r[0]]
                    ys = [start.r[1], end.r[1]]
                    plt.plot(xs, ys, color='red', linewidth='1')
                    start = end
                break
            # loop detected
            elif current_vertex.state == State.EXPLORED:
                while not(current_vertex == wilson_stack.peek()):
                    discarded_vertex = wilson_stack.pop()
                    discarded_vertex.state = State.NOT_VISITED
            # no problems here, keep adding to the stack
            elif current_vertex.state == State.NOT_VISITED:
                current_vertex.state = State.EXPLORED
                wilson_stack.push(current_vertex)

    plt.xlim(-size*.1, size * 1.1)
    plt.ylim(-size*.1, size)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.draw()
    plt.show()

def select_neighbor(current_vertex):
    position = np.random.randint(0, len(current_vertex.ns))
    return current_vertex.ns[position]

def select_unvisited_vertex(vs):
    unvisited_vertices = []
    for v in vs:
        if vs[v].state == State.NOT_VISITED:
            unvisited_vertices.append(vs[v])
    #print('Unvisted ' + str(len(unvisited_vertices)))
    position = np.random.randint(0, len(unvisited_vertices))
    return unvisited_vertices[position]
    
def norm(v1, v2):
    # this function finds the Euclidean distance between two 2D vectors
    # inputs: 
    #        v1 : (list) coordinates of vector 1
    #        v2 : (list) coordinates of vector 2
    # outputs:
    #        dist : (float) the Euclidean distance between v1 & v2
    
    dist =  np.sqrt((v1[0]- v2[0])**2 + (v2[1]-v1[1])**2)
    return dist

def initialize(G):
    # this function creates the dictionary where the names are enumerated and the values are vertex objects
    # inputs: 
    #        G : a list of vertices of the generated SG
    # outputs:
    #        vertices : (dictionary) contains enumerated names (e.g. '1', '234', etc.) and vertex object values
    
    vertices = {} # dictionary of vertices
    counter = 1
    for coor in G:
        vertices[str(counter)] = vertex(coor[0], coor[1])
        counter += 1
    
    for i in vertices:
        for j in vertices:
            d = norm(vertices[i].r, vertices[j].r)
            if d < 1.1 and d > .9:
                if not(vertices[j] in vertices[i].ns):
                    vertices[i].ns.append(vertices[j]) 
                if not(vertices[i] in vertices[j].ns):
                    vertices[j].ns.append(vertices[i])
    removes = []
    
    for i in vertices:
        if len(vertices[i].ns) == 6:
            for j in vertices[i].ns:
                if len(j.ns) == 6: 
                    removes.append([vertices[i], j])
    
    for pair in removes:
        i = pair[0]
        j = pair[1]
        if i in j.ns:
            j.ns.remove(i)
        if j in i.ns:
            i.ns.remove(j)
                    
    for i in vertices:
        if len(vertices[i].ns) == 5:
            for j in vertices[i].ns:
                if len(j.ns) == 5: 
                    vertices[i].ns.remove(j)
                    j.ns.remove(vertices[i])
        
    return vertices
    
def main(graph_size):
    n = graph_size #This will change the size
    G = generate(n)
    vs = initialize(G)
    #plotting(vs, G)
    wilson(vs, G)

main(5)    
