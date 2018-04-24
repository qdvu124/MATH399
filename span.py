import matplotlib.pyplot as plt

from edge import Edge
from state import State

class Span:

    def __init__(self, vs):
        self.edge_list = []
        self.vs = vs
        self.component_count = 0

    def add_edge(self, edge):
        self.edge_list.append(edge)

    def contains_edge(self, edge):
        for current_edge in self.edge_list:
            if edge == current_edge:
                return True
        return False

    def span_size(self):
        current_count = 3
        size = 1
        while True:
            if (current_count == len(self.vs)):
                return size 
            size = size * 2
            current_count = current_count + 2 * (current_count - 1) - 1

    def print(self):
        for index in self.vs:
            if self.vs[index].state == State.VISITED:
                plt.scatter(self.vs[index].r[0], self.vs[index].r[1], c='r')
            else:
                plt.scatter(self.vs[index].r[0], self.vs[index].r[1], c='b')

        for edge in self.edge_list:
            x_s = [edge.starting_vertex.r[0], edge.ending_vertex.r[0]]
            y_s = [edge.starting_vertex.r[1], edge.ending_vertex.r[1]]
            plt.plot(x_s, y_s, color='red', linewidth='1')
        size = self.span_size()
        plt.xlim(-size*.1, size * 1.1)
        plt.ylim(-size*.1, size)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.draw()
        plt.show()
