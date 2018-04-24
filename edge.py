class Edge:
    def __init__(self, starting_vertex, ending_vertex):
        self.id = frozenset([starting_vertex.id, ending_vertex.id])
        self.starting_vertex = starting_vertex
        self.ending_vertex = ending_vertex

    def __str__(self):
        return 'Starting vertex: ' + str(self.starting_vertex) + '\n Ending vertex: ' + str(self.ending_vertex)

    def __eq__(self, other):
        if ((self.starting_vertex == other.starting_vertex and self.ending_vertex == other.ending_vertex) 
        or (self.ending_vertex == other.starting_vertex and self.starting_vertex == other.ending_vertex)):
            return True
        return False

    def __key(self):
        return self.id

    def __hash__(self):
        return hash(self.__key())

    def contains(self, vertex):
        return (self.starting_vertex == vertex or self.ending_vertex == vertex)