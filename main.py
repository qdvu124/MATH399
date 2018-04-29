# %matplotlib inline                    
# comment out previous if not using ipython
from gasket import Gasket
from edge import Edge
from vertex import Vertex
from utility_functions import create_unicycle, cycle_length, unicycle_statistics
from wilsons_algorithm import main_algorithm

def component_count_main(iteration):
    with open("data.txt","a") as f:
        for graph_size in range(1, 6):
            for _ in range(10):
                f.write("Level %d with %d iterations: average of %.3f components\n" % (graph_size - 1, iteration, average_component_count(graph_size, iteration)))
            f.write("\n")
        f.close()

def cycle_length_count_main(iteration):
    with open("unicycle_length.txt", "a") as f:
        for graph_size in range(1, 6):
            for _ in range(10):
                (mean, std) = average_cycle_length(graph_size, iteration)
                f.write("Level %d with %d iterations: mean %.3f std %.3f\n" % (graph_size - 1, iteration, mean, std))
            f.write("\n")
        f.close()

def average_cycle_length(graph_size, iteration):
    cumulative_cycle_length = 0
    statistics = []
    for _ in range(iteration):
        gasket = Gasket()
        gasket.multiply(graph_size)
        vs = gasket.get_enum_vertices()
        current_span = main_algorithm(vs, 0)

        edge_set = set(current_span.edge_list)
        free_edge_list = set()

        for index in vs:
            for current_neighbor in vs[index].ns:
                current_edge = Edge(vs[index], current_neighbor)
                if not ((current_edge in edge_set) or (current_edge in free_edge_list)):
                    free_edge_list.add(current_edge)
        
        span_with_cycle = create_unicycle(free_edge_list, current_span)
        current_cycle_length = cycle_length(span_with_cycle)
        statistics.append(current_cycle_length)
        cumulative_cycle_length = cumulative_cycle_length + current_cycle_length

    frequency_map = dict()
    for length in statistics:
        if length in frequency_map:
            frequency_map[length] = frequency_map[length] + 1
        else:
            frequency_map[length] = 1

    with open("frequency.txt", "a") as f:
        for length in sorted(frequency_map, key=frequency_map.get):
            f.write("Level %d with %d iterations: length %d: frequency %d\n" % (graph_size - 1, iteration, length, frequency_map[length]))
        f.write("\n")
        f.close()

    return unicycle_statistics(statistics)
        
def average_component_count(graph_size, iteration):
    span_collection = []
    for _ in range(iteration):
        gasket = Gasket()
        gasket.multiply(graph_size)
        vs = gasket.get_enum_vertices()
        span_collection.append(main_algorithm(vs, 0))

    component_count = 0
    for span in span_collection:
        span.print()
        component_count =  component_count + span.component_count
        
    return component_count/iteration

average_component_count(5, 10)