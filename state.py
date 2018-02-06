from enum import Enum

class State(Enum):
    # Enumeration of possible states in Wilson's algorithm
    NOT_VISITED = 'NOT VISITED'
    EXPLORED = 'EXPLORED'
    VISITED = 'VISITED'

