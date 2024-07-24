
#* X: kocka po X osi. (Desna & Leva ploskev ostaneta enaka)
#* y : kocka po Y osi. (Zgornja & Spodnja ploskev ostaneta enaka)
#* z : kocka po Z osi. (Sprednja & Zadnja ploskev ostaneta enaka)

# Preberemo vsako vrstico in jih skupaj shranimo v set
cubes = set(tuple(map(int, line.split(','))) for line in open(r'examples\day18\input.txt').read().splitlines())

def calculate_non_connected_sides_part1()-> int:
    # Možne smeri
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)] # levo, desno, spredaj, zadaj, gor, dol
    # Celotno število odkritih ploskev kock
    total_surface_area: int = 0 
    
    # Premikamo so čez vse kocke
    for cube in cubes:
        # Za vsako kocko imamo na začetku 6 ne zakritih ploskev
        sides_exposed = 6 
        # Za vsako kocko pogledamo 6 možnih sosedov
        for direction in directions:
            neighbor = (cube[0] + direction[0], cube[1] + direction[1], cube[2] + direction[2])
            #* print(f"Cube: {cube} | neighbor: {neighbor}")
            # za vsakega soseda zmanjšamo število odkritih ploskev za 1
            if neighbor in cubes:
                sides_exposed -= 1
                #* print(f"{True} neighbor exists!")
        # Za vsako kocko seštevamo skupno število odkritih ploskev
        total_surface_area += sides_exposed
    
    return total_surface_area

def calculate_non_connected_sides_part2()-> int:
    # Možne smeri
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    # Celotno število odkritih ploskev kock
    total_surface_area: int = 0 

    # Definiramo meje prostora
    min_x = min(cube[0] for cube in cubes) - 1
    max_x = max(cube[0] for cube in cubes) + 1
    min_y = min(cube[1] for cube in cubes) - 1
    max_y = max(cube[1] for cube in cubes) + 1
    min_z = min(cube[2] for cube in cubes) - 1
    max_z = max(cube[2] for cube in cubes) + 1

    #* print(f"{min_x} | {min_y} | {min_z}")
    #* print(f"{max_x} | {max_y} | {max_z}")

    checked = set() # Zunanja meja zraka
    queue: list = ([(min_x, min_y, min_z)]) # Začnemo z najmanjšo možno pozicijo

    # Premikamo se 
    while queue:
        # Vzamemo prvi položaj
        x, y, z = queue.pop(0)

        # Preverimo, če je položaj že znan ali pa je del kock, če je preskočimo
        if (x, y, z) in checked or (x, y, z) in cubes:
            continue

        # Preverimo, če je trenutni položaj znotraj naših meja
        if x < min_x or x > max_x or y < min_y or y > max_y or z < min_z or z > max_z:
            continue
        
        # Drugače dodamo, da je trenutni položaj znotraj in je že pregledan
        checked.add((x, y, z))
        
        # Za vsak od šestih možnih smeri izračunamo sosednji položaj in ga dodamo v vrsto
        for direction in directions:
            neighbor = (x + direction[0], y + direction[1], z + direction[2])
            queue.append(neighbor)

    #* print(f"Vse meje: {checked}")

    # Premikamo so čez vse kocke
    for cube in cubes:
        # Za vsako kocko preverimo vseh šest sosednjih položajev v vseh šestih smereh
        for direction in directions:
            # Izračunamo položaj sosednje kocke tako, da dodamo trenutno smer k trenutni kocki
            neighbor = (cube[0] + direction[0], cube[1] + direction[1], cube[2] + direction[2])
            # Če sosednja kocka na položaju ne obstaja in je del zunanjega zraka (Ploskev izpostavljena zunanjem zraku) 
            if neighbor not in cubes and neighbor in checked:
                # Povečamo za 1
                total_surface_area += 1

    return total_surface_area

# Part1
output = calculate_non_connected_sides_part1()
print(f"Total number of uncovered sides: {output}")

# Part2
output = calculate_non_connected_sides_part2()
print(f"Total number of uncovered sides: {output}")