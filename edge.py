class Edge:
    def __init__(self, starting_vertex, ending_vertex):
        self.starting_vertex = starting_vertex
        self.ending_vertex = ending_vertex

    def __str__(self):
        return 'Starting vertex: ' + str(self.starting_vertex) + '\n Ending vertex: ' + str(self.ending_vertex)

    def __eq__(self, other):
        if ((self.starting_vertex == other.starting_vertex and self.ending_vertex == other.ending_vertex) 
        or (self.ending_vertex == other.starting_vertex and self.starting_vertex == other.ending_vertex)):
            return True
        return False