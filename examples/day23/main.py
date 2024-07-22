positions = [list(line) for line in open('examples\day23\input.txt', 'r').read().strip().split('\n')]

order = [('N', 'NE', 'NW', -1, 0), ('S', 'SE', 'SW', +1, 0), ('W', 'NW', 'SW', 0, -1), ('E', 'NE', 'SE', 0, +1)]

# Funkcija za izpis trenutnih pozicij
def current_positions(positions: list):
    output = ''
    for row in positions:
        output += ''.join(row) + '\n'

    return output

# Funkcija, ki za določeno pozicijo dobi kordinate za možne sosede
def get_possible_neighbor(x: int, y: int) -> dict:
    directions: dict = {}

    if positions[y-1][x-1] == "#":
        directions.update({'NW': True})
    else:
        directions.update({'NW': False})

    
    if positions[y-1][x] == "#":
        directions.update({'N': True})
    else:
        directions.update({'N': False})
    
    if positions[y-1][x+1] == "#":
        directions.update({'NE': True})
    else:
        directions.update({'NE': False})

    if positions[y][x-1] == "#":
        directions.update({'W': True})
    else:
        directions.update({'W': False})

    if positions[y][x+1] == "#":
        directions.update({'E': True})
    else:
        directions.update({'E': False})

    if positions[y+1][x-1] == "#":
        directions.update({'SW': True})
    else:
        directions.update({'SW': False})

    if positions[y+1][x] == "#":
        directions.update({'S': True})
    else:
        directions.update({'S': False})

    if positions[y+1][x+1] == "#":
        directions.update({'SE': True})
    else:
        directions.update({'SE': False})

    return directions

# Funkcija za določitev premikov
def define_moves(positions: list, order: list):
    moves: dict = {}

    for y in range(len(positions)):
        for x in range(len(positions[y])):
            #*print(f"Y: {y} | X: {x} | {input[y][x]}")
            if positions[y][x] == "#":

                possibilities = get_possible_neighbor(x, y)

                if not any(possibilities.values()):
                    continue

                if not possibilities[order[0][0]] and not possibilities[order[0][1]] and not possibilities[order[0][2]]:
                    moves.update({(y, x): (y + order[0][3], x + order[0][4])})
                    #*print(f"True: North | {x,y} | {possibilities['NW'], possibilities['N'], possibilities['NE']}")
                elif not possibilities[order[1][0]] and not possibilities[order[1][1]] and not possibilities[order[1][2]]:
                    moves.update({(y, x): (y + order[1][3], x + order[1][4])})
                    #*print(f"True: South | {x,y} | {possibilities['SW'], possibilities['S'], possibilities['SE']}")
                elif not possibilities[order[2][0]] and not possibilities[order[2][1]] and not possibilities[order[2][2]]: 
                    moves.update({(y, x): (y + order[2][3], x + order[2][4])})
                    #*print(f"True: West | {x,y} | {possibilities['NW'], possibilities['W'], possibilities['SW']}")
                elif not possibilities[order[3][0]] and not possibilities[order[3][1]] and not possibilities[order[3][2]]:
                    moves.update({(y, x): ((y + order[3][3], x + order[3][4]))})
                    #*print(f"True: West | {x,y} | {possibilities['NE'], possibilities['E'], possibilities['SE']}")

    # Vzamemo prvi vrsti red in ga dodamo kot zadnjega v vrsto
    order.append(order.pop(0))

    return moves

# Funckija, ki izvede premike
def commit_moves(positions: list, order: list):
    moves = define_moves(positions, order)
    
    for key, value in moves.items():
        if any(value == other_value for other_key, other_value in moves.items() if other_key != key):
            #*print("Skipping!")
            continue

        positions[key[0]][key[1]] = '.'
        positions[value[0]][value[1]] = "#"

# Funkcija, ki prešteje prazne pike v pravokotniku
def calculate_empty_tiles(positions: list):
    min_y, max_y, min_x, max_x = len(positions), 0, len(positions[0]), 0

    for y in range(len(positions)):
        for x in range(len(positions[y])):
            if positions[y][x] == '#':
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x  
                    
    empty_tiles = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if positions[y][x] == '.':
                empty_tiles += 1

    return empty_tiles

# Program
for i in range(10):
    commit_moves(positions, order)
    #*print(current_positions(positions))
print(calculate_empty_tiles(positions))




#TODO: Lažji način? boljši?
"""
# Funkcija, ki za določeno pozicijo dobi kordinate za možne sosede
def get_possible_neighbor(x: int, y: int) -> list:
    return [(x-1, y+1), (x, y+1), (x+1,y+1), 
            (x-1,y), (x+1,y), 
            (x-1,y-1), (x, y-1), (x+1, y-1)]
"""


"""
        if y != 0:
        if positions[y-1][x-1] == "#":
            directions.update({'NW': True})
        else:
            directions.update({'NW': False})
    else:
        directions.update({'NW': True})
    
    if y != 0:
        if positions[y-1][x] == "#":
            directions.update({'N': True})
        else:
            directions.update({'N': False})
    else:
        directions.update({'N': True})

    
    if y != 0:
        if positions[y-1][x+1] == "#":
            directions.update({'NE': True})
        else:
            directions.update({'NE': False})
    else:
        directions.update({'NE': True})

    if x != 0:
        if positions[y][x-1] == "#":
            directions.update({'W': True})
        else:
            directions.update({'W': False})
    else:
        directions.update({'W': True})

    if y != len(positions[0]):
        if positions[y][x+1] == "#":
            directions.update({'E': True})
        else:
            directions.update({'E': False})
    else:
        directions.update({'E': True})

    if y != len(positions):
        if positions[y+1][x-1] == "#":
            directions.update({'SW': True})
        else:
            directions.update({'SW': False})
    else:
        directions.update({'SW': True})

    if y != len(positions):
        if positions[y+1][x] == "#":
            directions.update({'S': True})
        else:
            directions.update({'S': False})
    else:
        directions.update({'S': True})

    if y != len(positions):
        if positions[y+1][x+1] == "#":
            directions.update({'SE': True})
        else:
            directions.update({'SE': False})
    else:
        directions.update({'SE': True})








"""