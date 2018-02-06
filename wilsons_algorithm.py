import numpy as np

from stack import Stack
from tree import Tree
from edge import Edge
from state import State

def main_algorithm(vs, size):
    wilson_stack = Stack()
    wilson_tree = Tree()
    starting_vertex = select_unvisited_vertex(vs)
    starting_vertex.state = State.VISITED
    cover_count = 1

    # while we still do not have a spanning tree yet, i.e some vertices are not yet covered
    while cover_count < len(vs):
        current_vertex = select_unvisited_vertex(vs)
        current_vertex.state = State.EXPLORED
        wilson_stack.push(current_vertex)
        # begin the random walk starting at this
        while True:
            current_vertex = select_neighbor(current_vertex)
            # we have encountered some vertex that we have already visited. Begin adding vertices to tree
            if current_vertex.state == State.VISITED:
                start = current_vertex
                while not(wilson_stack.isEmpty()):
                    end = wilson_stack.pop()
                    end.state = State.VISITED
                    cover_count = cover_count + 1
                    wilson_tree.addEdge(Edge(start, end))
                    start = end
                break
            # loop detected
            elif current_vertex.state == State.EXPLORED:
                while not(current_vertex == wilson_stack.peek()):
                    discarded_vertex = wilson_stack.pop()
                    discarded_vertex.state = State.NOT_VISITED
            # no problems here, keep adding to the stack
            elif current_vertex.state == State.NOT_VISITED:
                current_vertex.state = State.EXPLORED
                wilson_stack.push(current_vertex)

    wilson_tree.print(size)

def select_neighbor(current_vertex):
    position = np.random.randint(0, len(current_vertex.ns))
    return current_vertex.ns[position]

def select_unvisited_vertex(vs):
    unvisited_vertices = []
    for v in vs:
        if vs[v].state == State.NOT_VISITED:
            unvisited_vertices.append(vs[v])
    #print('Unvisted ' + str(len(unvisited_vertices)))
    position = np.random.randint(0, len(unvisited_vertices))
    return unvisited_vertices[position]
 