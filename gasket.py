import numpy as np
from utility_functions import norm
from vertex import Vertex

class Gasket:

    def __init__(self):
        self.graph = [[0,0], [1,0], [.5, np.sqrt(3)/2]] #n = 1 Gasket

    def multiply(self, level):
        # this function generates the SG list of vertices
        # inputs: 
        #        level : (int) number of levels of recursion
        # outputs:
        #        G : (list) a lit of vertices of the generated SG
        for i in range(level - 1):
            self.tripler()

    def trisize(self):
    #This function determines the overall side length of the gasket G
    #        M : an integer telling the length of a side in vertex units of the generated SG 
        maximum = 0
        for coor in self.graph:
            x = coor[0]
            if x > maximum:
                maximum = x
        return maximum

    def tripler(self):
        # This functions takes a gasket and runs one recursive cycle to increase the size of the SG
        # inputs: 
        #        G : a list of vertices of the generated SG
        # outputs:
        #        trip_G : the new list of vertices once G is tripled
        trip_graph = []
        size = self.trisize()
        for coor in self.graph:
            x = coor[0]
            y = coor[1]
            # copy over G so far
            trip_graph.append(coor)
            
        for coor in self.graph:
            x = coor[0]
            y = coor[1]       
            # copy G to the right
            if x > 0: # as to not repeat vertices (.1 is just in case there are float point errors)
                x_new = size + x
                trip_graph.append([x_new, y])
            
            # copy G above
            if x > 0 and x < size:
                x_new = x + size/2
                y_new = y + size*np.sqrt(3)/2
                trip_graph.append([x_new, y_new])
        self.graph = trip_graph

    def get_enum_vertices(self):
        # this function creates the dictionary where the names are enumerated and the values are vertex objects
        # inputs: 
        #        G : a list of vertices of the generated SG
        # outputs:
        #        vertices : (dictionary) contains enumerated names (e.g. '1', '234', etc.) and vertex object values
        
        vertices = {} # dictionary of vertices
        counter = 1
        for coor in self.graph:
            vertices[str(counter)] = Vertex(coor[0], coor[1], counter)
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
    