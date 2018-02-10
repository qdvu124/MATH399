# %matplotlib inline                    
# comment out previous if not using ipython
  
from gasket import Gasket
from edge import Edge
from vertex import Vertex
from wilsons_algorithm import main_algorithm

def main(graph_size, iteration):
    tree_collection = []

    for _ in range(iteration):
        gasket = Gasket()
        gasket.multiply(graph_size)
        vs = gasket.get_enum_vertices()
        #plotting(vs, G)
        tree_collection.append(main_algorithm(vs))

    edge = Edge(Vertex(0, 0), Vertex(1, 0))
    count = 0
    for tree in tree_collection:
        if tree.contains_edge(edge):
            count = count + 1

    print(count/float (iteration))

main(3, 100000)
