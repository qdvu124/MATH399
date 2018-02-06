class Edge:
    def __init__(self, starting_vertex, ending_vertex):
        self.starting_vertex = starting_vertex
        self.ending_vertex = ending_vertex

    def __str__(self):
        return 'Starting vertex: ' + self.starting_vertex.str + '\n Ending vertex: ' + self.ending_vertex.str