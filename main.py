# %matplotlib inline                    
# comment out previous if not using ipython
  
from gasket import Gasket
from wilsons_algorithm import main_algorithm

def main(graph_size):
    gasket = Gasket()
    gasket.multiply(graph_size)
    vs = gasket.get_enum_vertices()
    size = gasket.trisize()
    #plotting(vs, G)
    main_algorithm(vs, size)

main(5)