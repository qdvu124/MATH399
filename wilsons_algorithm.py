import numpy as np

from stack import Stack
from tree import Tree
from edge import Edge
from state import State

# Wilson's algorithm on the list of vertices, and with loop rentention probability p
def main_algorithm(vs, p):
    if (p < 0 or p > 1):
        print('Invalid value for loop retention probability')
        return

    wilson_stack = Stack()
    wilson_tree = Tree(vs)
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
                wilson_stack.push(current_vertex)
                cover_count = cover_count + add_stack_to_tree(wilson_stack, wilson_tree)
                break
            # loop detected
            elif current_vertex.state == State.EXPLORED:
                if (np.random.uniform() < p):
                    wilson_stack.push(current_vertex)
                    cover_count = cover_count + add_stack_to_tree(wilson_stack, wilson_tree) 
                else:
                    discard_loop(current_vertex, wilson_stack)
            # no problems here, keep adding to the stack
            elif current_vertex.state == State.NOT_VISITED:
                current_vertex.state = State.EXPLORED
                wilson_stack.push(current_vertex)
    return wilson_tree

def discard_loop(current_vertex, wilson_stack):
    while not(current_vertex == wilson_stack.peek()):
        discarded_vertex = wilson_stack.pop()
        discarded_vertex.state = State.NOT_VISITED

def add_stack_to_tree(wilson_stack, wilson_tree):
    partial_cover_count = 0
    start = wilson_stack.pop()
    while not(wilson_stack.isEmpty()):
        end = wilson_stack.pop()
        end.state = State.VISITED
        partial_cover_count = partial_cover_count + 1
        wilson_tree.add_edge(Edge(start, end))
        start = end
    return partial_cover_count
 
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
 