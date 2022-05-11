def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE',
                  'S', 'SW', 'W', 'NW']
    steps = turn/45
    face = directions.index(facing)
    return directions[face + steps]

# Further create static variables at the
# beginning, capitalized (ex: 'DIRECTIONS')
