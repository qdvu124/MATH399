import matplotlib.pyplot as plt

from edge import Edge

class Tree:
    def __init__(self):
        self.edge_list = []

    def add_edge(self, edge):
        self.edge_list.append(edge)

    def contains_edge(self, edge):
        for current_edge in self.edge_list:
            if edge == current_edge:
                return True
        return False

    def tree_size(self):
        number_of_vertices = len(self.edge_list) + 1
        current_count = 3
        size = 1
        while True:
            if (current_count == number_of_vertices):
                return size
            size = size + 1
            current_count = current_count + 2 * (current_count - 1) - 1

    def print(self):
        for edge in self.edge_list:
            x_s = [edge.starting_vertex.r[0], edge.ending_vertex.r[0]]
            y_s = [edge.starting_vertex.r[1], edge.ending_vertex.r[1]]
            plt.plot(x_s, y_s, color='red', linewidth='1')
        size = self.tree_size()
        plt.xlim(-size*.1, size * 1.1)
        plt.ylim(-size*.1, size)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.draw()
        plt.show()
