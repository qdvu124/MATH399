# %matplotlib inline                    
# comment out previous if not using ipython
import matplotlib.pyplot as plt

from gasket import Gasket
from edge import Edge
from vertex import Vertex
from wilsons_algorithm import main_algorithm

def main(iteration):
    with open("data.txt","a") as f:
        for graph_size in range(1, 6):
            for i in range(0, 10):
                f.write("Level %d with %d iterations: average of %.3f components\n" % (graph_size - 1, iteration, average_component_count(graph_size, iteration)))
            f.write("\n")

def average_component_count(graph_size, iteration):
    span_collection = []
    for _ in range(iteration):
        gasket = Gasket()
        gasket.multiply(graph_size)
        vs = gasket.get_enum_vertices()
        span_collection.append(main_algorithm(vs, 1))

        component_count = 0
        for span in span_collection:
            component_count =  component_count + span.component_count
        
    return component_count/iteration

main(1000)
