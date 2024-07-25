positions = [list(line) for line in open('examples\day23\input.txt', 'r').read().strip().split('\n')]

# Smeri
order = ['N', 'S', 'W', 'E']

# Funkcija, ki za določeno pozicijo dobi kordinate za prazne sosede
def get_empty_neighbors(cords: set, y: int, x: int) -> dict:
    neighbors: dict = {}

    if (y-1, x-1) in cords or (y-1, x) in cords or (y-1, x+1) in cords:
        neighbors['N'] = True
    else:
        neighbors['N'] = False 
    
    if (y+1, x-1) in cords or (y+1, x) in cords or (y+1, x+1) in cords:
        neighbors['S'] = True
    else:
        neighbors['S'] = False 

    if (y-1, x-1) in cords or (y, x-1) in cords or (y+1, x-1) in cords:
        neighbors['W'] = True
    else:
        neighbors['W'] = False 

    if (y+1, x+1) in cords or (y, x+1) in cords or (y-1, x+1) in cords:
        neighbors['E'] = True
    else:
        neighbors['E'] = False 
      
    return neighbors

# Funkcija za določitev premikov
def define_moves(cords: set, order: list) -> dict:
    moves: dict = {}

    for cord in cords:

        empty_neighbors = get_empty_neighbors(cords, cord[0], cord[1])

        # Če ni nobenega soseda na nobenih pozicijah preskočimo premik ni potreben
        if all(not value for value in empty_neighbors.values()):
            continue   

        # Če so sosedi v vseh smereh preskočimo premik ni mogoč
        if all(value for value in empty_neighbors.values()): 
            continue

        # Za vsako trenutno smer premika pregledamo, če je premik mogoč
        for direction in order:
            if direction == 'N' and not empty_neighbors['N']:
                moves[cord] = (cord[0]-1, cord[1])
                break
            elif direction == 'S' and not empty_neighbors['S']:
                moves[(cord)] = (cord[0]+1, cord[1])
                break
            elif direction == 'W' and not empty_neighbors['W']:
                moves[(cord)] = (cord[0], cord[1]-1)
                break
            elif direction == 'E' and not empty_neighbors['E']:
                moves[(cord)] = (cord[0], cord[1]+1)
                break    

    # Vzamemo vn prvi element v seznamu in ga damo v vrsto kot zadnjega
    order.append(order.pop(0))

    #pass
    return moves

# Funckija, ki izvede premike
def commit_moves(cords: set, order: list) -> set:
    # Dobimo možne premike
    moves = define_moves(cords, order)

    if len(moves) == 0:
        return False

    new_cords: set = set()
    
    # Za vsak kordinat preverimo, če je v možnih premikih
    for cord in cords:
        # Če ni ga dodamo v nove kordinate, saj se ne bo premaknil
        if cord not in moves.keys():
            new_cords.add(cord)
            continue
    
    # Za vsak ključ preverimo, če ima premik(Vrednost) enak kot kateri izmed drugih možnih premikov 
    for key, value in moves.items():
        if any(value == other_value for other_key, other_value in moves.items() if other_key != key):
            new_cords.add(key) # Če je sta dva elfa z enakim željenim premikom se trenutni elf ne premakne
        else:
            new_cords.add(value) # Če ni težav z enakimi premiki se elf premakne
    #pass
    return new_cords
    
# Funkcija, ki prešteje prazne pike v pravokotniku
def calculate_empty_tiles(cords: set) -> int:
    
    # Dobimo limite za pravokotnik
    min_x = min(x[1] for x in cords)
    max_x = max(x[1] for x in cords)
    min_y = min(y[0] for y in cords)
    max_y = max(y[0] for y in cords)
    
    #! Daljši način

    empty_tiles=0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (y, x) not in cords:
                empty_tiles += 1
    #pass
    return empty_tiles

# Ustvarimo seznam kordinatov glede na pozicije elf-ov
cords: set = set()
for y in range(len(positions)):
    for x in range(len(positions[y])):
        if positions[y][x] == "#":
            cords.add((y, x))    

# Program part1 and part2
no_move_round: int = 1

while True:
    cords = commit_moves(cords, order)

    if cords == False:
        break

    if no_move_round == 10:
        output = calculate_empty_tiles(cords)   
        print(f"Število praznih mest: {output}")

    no_move_round += 1

print(f"Krog v katerem se ni premaknil nobeden elf: {no_move_round}")