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

def unicycle_statistics(unicycles, level):
    statistics = []
    for unicycle in unicycles:
        # unicycle_labels = graph_labels(unicycle)
        # nx.draw_networkx(unicycle, labels=unicycle_labels, font_size=16)
        # plt.show()
        cycle = list(nx.find_cycle(unicycle))
        statistics.append(len(cycle))

    # plt.hist(statistics, range=(0, 2**level), density=False, bins=binSeq(level))
    #plt.yticks(range(1, statistics.count(4)))
    plt.show()
    f = open("statistics.txt", 'a')
    descriptor = "level " + str(level-1) + "\n"
    f.write(descriptor)
    counts = dict()
    for i in statistics:
        counts[i] = counts.get(i, 0) + 1
    f.write(str(counts)+"\n")
    f.close()
    return (np.mean(statistics), np.std(statistics))