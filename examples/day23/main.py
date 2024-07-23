positions = [list(line) for line in open('examples\day23\input.txt', 'r').read().strip().split('\n')]

order = ['N', 'S', 'W', 'E']

# Funkcija za izpis trenutnih pozicij
def current_positions(positions: list):
    output = ''
    for row in positions:
        output += ''.join(row) + '\n'

    return output

# Funkcija, ki za določeno pozicijo dobi kordinate za možne sosede
def get_possible_neighbor(x: int, y: int, limit_x, limit_y) -> dict:
    directions: list = []

    for change_y in [-1, 0, 1]:
        for change_x in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue

            new_x, new_y = x + change_x, y + change_y

            if new_x == x and new_y == y:
                continue

            if 0 <= new_x < limit_x and 0 <= new_y < limit_y:
                directions.append((new_y, new_x))

    return directions

# Funckija, ki preveri, če je premik v določeno smer mogoč
def check_direction(empty_neighbors: list, y: int, x: int, limit_y: int, limit_x: int, direction: str):

    if direction == 'N':
        if y <= 0:
            return False
        if (y-1, x-1) in empty_neighbors and (y-1, x) in empty_neighbors and (y-1, x+1) in empty_neighbors:
            return True
        return False
    
    elif direction == 'S': 
        if y >= limit_y - 1:
            return False
        if (y+1, x-1) in empty_neighbors and (y+1, x) in empty_neighbors and (y+1, x+1) in empty_neighbors:
            return True
        return False
    
    elif direction == 'W': 
        if x <= 0:
            return False
        if (y-1, x-1) in empty_neighbors and (y, x-1) in empty_neighbors and (y+1, x-1) in empty_neighbors:
            return True
        return False
    
    elif direction == 'E': 
        if x >= limit_x - 1:
            return False
        if (y-1, x+1) in empty_neighbors and (y, x+1) in empty_neighbors and (y+1, x+1) in empty_neighbors:
            return True
        return False

# Funkcija za določitev premikov
def define_moves(positions: list, order: list):
    moves: dict = {}
    limit_y, limit_x = len(positions), len(positions[0])

    for y in range(len(positions)):
        for x in range(len(positions[y])):
            #*print(f"Y: {y} | X: {x} | {input[y][x]}")
            if positions[y][x] == "#":
            
                possibilities = get_possible_neighbor(x, y, limit_x, limit_y)

                # Poiščemo vse kordinate praznih sosedov v možnih sosedih
                empty_neighbors = []

                for pos in possibilities:
                    if positions[pos[0]][pos[1]] == ".":
                        empty_neighbors.append(pos)
                    
                # Če je število praznih sosedov enaka vsem možnim sosedom pozicijo preskočimo
                if len(empty_neighbors) == len(possibilities):
                    continue

                for direction in order:
                    if direction == 'N' and check_direction(empty_neighbors, y, x, limit_y, limit_x, direction):
                        moves[(y, x)] = (y-1, x)
                        break
                    elif direction == 'S' and check_direction(empty_neighbors, y, x, limit_y, limit_x, direction):
                        moves[(y, x)] = (y+1, x)
                        break
                    elif direction == 'W' and check_direction(empty_neighbors, y, x, limit_y, limit_x, direction):
                        moves[(y, x)] = (y, x-1)
                        break
                    elif direction == 'E' and check_direction(empty_neighbors, y, x, limit_y, limit_x, direction):
                        moves[(y, x)] = (y, x+1)
                        break

    # Vzamemo prvi vrsti red in ga dodamo kot zadnjega v vrsto
    order.append(order.pop(0))

    return moves

""" TODO:
# Funckija, ki izvede premike
def commit_moves(positions: list, order: list):
    moves = define_moves(positions, order)
    #*print(moves)
    for key, value in moves.items():
        if any(value == other_value for other_key, other_value in moves.items() if other_key != key):
            #*print("Skipping!")
            continue

        positions[key[0]][key[1]] = '.'
        positions[value[0]][value[1]] = "#"
"""

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
for i in range(2):
    commit_moves(positions, order)
    #print(current_positions(positions))
#print(calculate_empty_tiles(positions))
#print(current_positions(positions))
