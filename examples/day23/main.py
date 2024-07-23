positions = [list(line) for line in open('examples\day23\input.txt', 'r').read().strip().split('\n')]

# Smeri
order = ['N', 'S', 'W', 'E']

# Funkcija, ki za določeno pozicijo dobi kordinate za prazne sosede
def get_empty_neighbors(cords: list, y: int, x: int) -> dict:
    neighbors: list = []

    # Premikamo se skozi y pozicije
    for change_y in [-1, 0, 1]:
        # Premikamo se skozi x pozicije
        for change_x in [-1, 0, 1]:
            # Spreminjamo x in y (+1, -1)
            new_x, new_y = x + change_x, y + change_y

            # Če sta nov x in y enaka trenutnim kordinatom elfa preskočimo
            if new_x == x and new_y == y:
                continue
            
            # V seznam dodamo samo kordinate, ki so prazni
            if (new_y, new_x) not in cords:
                neighbors.append((new_y, new_x))

    return neighbors

# Funckija, ki preveri, če je premik v določeno smer mogoč
def check_direction(empty_neighbors: list, y: int, x: int, direction: str) -> bool:

    # V praznih sosedih preverimo, če se glede na trenutno smer lahko elf premakne
    if direction == 'N':
        if (y-1, x-1) in empty_neighbors and (y-1, x) in empty_neighbors and (y-1, x+1) in empty_neighbors:
            return True
        else:
            return False
    elif direction == 'S': 
        if (y+1, x-1) in empty_neighbors and (y+1, x) in empty_neighbors and (y+1, x+1) in empty_neighbors:
            return True
        else:
            return False
    elif direction == 'W': 
        if (y-1, x-1) in empty_neighbors and (y, x-1) in empty_neighbors and (y+1, x-1) in empty_neighbors:
            return True
        else:
            return False
    elif direction == 'E': 
        if (y-1, x+1) in empty_neighbors and (y, x+1) in empty_neighbors and (y+1, x+1) in empty_neighbors:
            return True
        else:
            return False

# Funkcija za določitev premikov
def define_moves(cords: list, order: list) -> dict:
    moves: dict = {}

    for cord in cords:
        # Kličemo funkcijo, ki vrne kordinate praznih sosedov
        empty_neighbors = get_empty_neighbors(cords, cord[0], cord[1])

        # Če je število praznih sosedov enako 8 preskočimo, saj se elf ne premakne
        if len(empty_neighbors) == 8:
            continue   
        
        # Za vsako trenutno smer premika pregledamo, če je premik mogoč
        for direction in order:
            if direction == 'N' and check_direction(empty_neighbors, cord[0], cord[1], direction):
                moves[(cord[0], cord[1])] = (cord[0]-1, cord[1])
                break
            elif direction == 'S' and check_direction(empty_neighbors, cord[0], cord[1], direction):
                moves[(cord[0], cord[1])] = (cord[0]+1, cord[1])
                break
            elif direction == 'W' and check_direction(empty_neighbors, cord[0], cord[1], direction):
                moves[(cord[0], cord[1])] = (cord[0], cord[1]-1)
                break
            elif direction == 'E' and check_direction(empty_neighbors, cord[0], cord[1], direction):
                moves[(cord[0], cord[1])] = (cord[0], cord[1]+1)
                break    

    # Vzamemo vn prvi element v seznamu in ga damo v vrsto kot zadnjega
    order.append(order.pop(0))

    return moves

# Funckija, ki izvede premike
def commit_moves(cords: list, order: list) -> list:
    # Dobimo možne premike
    moves = define_moves(cords, order)

    new_cords: list = []

    # Za vsak kordinat preverimo, če je v možnih premikih
    for cord in cords:
        # Če ni ga dodamo v nove kordinate, saj se ne bo premaknil
        if cord not in moves.keys():
            new_cords.append(cord)
            continue
    
    # Za vsak ključ preverimo, če ima premik(Vrednost) enak kot kateri izmed drugih možnih premikov 
    for key, value in moves.items():
        if any(value == other_value for other_key, other_value in moves.items() if other_key != key):
            new_cords.append(key) # Če je sta dva elfa z enakim željenim premikom se trenutni elf ne premakne
        else:
            new_cords.append(value) # Če ni težav z enakimi premiki se elf premakne

    return new_cords
    
# Funkcija, ki prešteje prazne pike v pravokotniku
def calculate_empty_tiles(cords: list) -> int:
    
    # Dobimo limite za pravokotnik
    min_x = min(x[1] for x in cords)
    max_x = max(x[1] for x in cords)
    min_y = min(y[0] for y in cords)
    max_y = max(y[0] for y in cords)
    
    #! Daljši način
    """
    empty_tiles=0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (y, x) not in cords:
                empty_tiles += 1
    """

    empty_tiles = (max_x - min_x + 1) * (max_y - min_y + 1) - len(cords)
    
    return empty_tiles

# Ustvarimo seznam kordinatov glede na pozicije elf-ov
cords: list = []
for y in range(len(positions)):
    for x in range(len(positions[y])):
        if positions[y][x] == "#":
            cords.append((y, x))

# Program part1
for i in range(10):
    cords = commit_moves(cords, order)
print(calculate_empty_tiles(cords))