# %matplotlib inline                    
# comment out previous if not using ipython
import matplotlib.pyplot as plt

from gasket import Gasket
from edge import Edge
from vertex import Vertex
from utility_functions import create_unicycle, cycle_length 
from wilsons_algorithm import main_algorithm

def component_count_main(iteration):
    with open("data.txt","a") as f:
        for graph_size in range(1, 6):
            for _ in range(10):
                f.write("Level %d with %d iterations: average of %.3f components\n" % (graph_size - 1, iteration, average_component_count(graph_size, iteration)))
            f.write("\n")

def cycle_length_count(iteration):
    with open("unicycle_length.txt", "a") as f:
        for graph_size in range(1, 3):
            for _ in range(10):
                f.write("Level %d with %d iterations: average length of cycle of %.3f\n" % (graph_size - 1, iteration, average_cycle_length(graph_size, iteration)))
            f.write("\n")

def average_cycle_length(graph_size, iteration):
    cumulative_cycle_length = 0
    for _ in range(iteration):
        gasket = Gasket()
        gasket.multiply(graph_size)
        vs = gasket.get_enum_vertices()
        current_span = main_algorithm(vs, 0)

        edge_set = set(current_span.edge_list)
        free_edge_list = set()

        for vertex in vs:
            for current_neighbor in vertex.ns:
                current_edge = Edge(vertex, current_neighbor)
                if not ((current_edge in edge_set) or (current_edge in free_edge_list)):
                    free_edge_list.add(current_edge)
        
        span_with_cycle = create_unicycle(free_edge_list, current_span)
        span_with_cycle.print()
        current_cycle_length = cycle_length(span_with_cycle)
        print(current_cycle_length)
        cumulative_cycle_length = cumulative_cycle_length + current_cycle_length

    return cumulative_cycle_length/iteration
        
def average_component_count(graph_size, iteration):
    span_collection = []
    for _ in range(iteration):
        gasket = Gasket()
        gasket.multiply(graph_size)
        vs = gasket.get_enum_vertices()
        span_collection.append(main_algorithm(vs, 0.01))

    component_count = 0
    for span in span_collection:
        component_count =  component_count + span.component_count
        
    return component_count/iteration

average_cycle_length(3, 10)
