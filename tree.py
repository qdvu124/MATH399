import matplotlib.pyplot as plt

from edge import Edge

class Tree:
    def __init__(self):
        self.edge_list = []

    def addEdge(self, edge):
        self.edge_list.append(edge)

    def print(self, size):
        for edge in self.edge_list:
            x_s = [edge.starting_vertex.r[0], edge.ending_vertex.r[0]]
            y_s = [edge.starting_vertex.r[1], edge.ending_vertex.r[1]]
            plt.plot(x_s, y_s, color='red', linewidth='1')

        plt.xlim(-size*.1, size * 1.1)
        plt.ylim(-size*.1, size)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.draw()
        plt.show()
