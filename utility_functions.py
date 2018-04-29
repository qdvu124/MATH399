import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

import random

def norm(v1, v2):
    # this function finds the Euclidean distance between two 2D vectors
    # inputs: 
    #        v1 : (list) coordinates of vector 1
    #        v2 : (list) coordinates of vector 2
    # outputs:
    #        dist : (float) the Euclidean distance between v1 & v2
    
    dist =  np.sqrt((v1[0]- v2[0])**2 + (v2[1]-v1[1])**2)
    return dist

def create_unicycle(free_edge_list, current_span):
    random_edge = random.sample(free_edge_list, 1)[0]
    current_span.add_edge(random_edge)
    return current_span 

def cycle_length(span_with_cycle):
    graph = nx.Graph()
    for edge in span_with_cycle.edge_list:
        graph.add_edge(edge.starting_vertex, edge.ending_vertex)
    return len(list(nx.find_cycle(graph)))

def calculate_statistics(statistics):
    if len(np.unique(statistics)) == 1:
        mean = np.unique(statistics)[0]
        plt.hist(statistics)
        plt.show()
        return (mean, 0)
    d = np.diff(np.unique(statistics)).min()
    left_of_first_bin = min(statistics) - float(d)/2
    right_of_last_bin = max(statistics) + float(d)/2
    # uncomment these 2 lines for showing histogram
    plt.hist(statistics, np.arange(left_of_first_bin, right_of_last_bin + d, d))
    plt.show()
    return (np.mean(statistics), np.std(statistics))
