import keys

INVALID = 0
NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4

def reverse(direction):
    if direction == NORTH:
        return SOUTH
    elif direction == EAST:
        return WEST
    elif direction == SOUTH:
        return NORTH
    elif direction == WEST:
        return EAST
    else:
        return INVALID

def delta(direction):
    if direction == NORTH:
        return (0, -1)
    elif direction == EAST:
        return (1, 0)
    elif direction == SOUTH:
        return (0, 1)
    elif direction == WEST:
        return (-1, 0)
    else:
        return (0, 0)

def from_key(key):
    if key == 'UP':
        return NORTH
    elif key == 'RIGHT':
        return EAST
    elif key == 'DOWN':
        return SOUTH
    elif key == 'LEFT':
        return WEST
    else:
        return INVALID
