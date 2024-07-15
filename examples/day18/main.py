# Rotacije:
#* X: Rotiramo kocko po X osi. (Desna & Leva poskev ostaneta enaka)
#* y : Rotiramo kocko po Y osi. (Zgornja & Spodnja faces remain intact)
#* z : Rotiramo kocko po Z osi. (Sprednja & Zadnja faces remain intact)

# Preberemo vsako vrstico in jih skupaj shranimo v set
cubes = set(tuple(map(int, line.split(','))) for line in open(r'examples\day18\input.txt').read().splitlines())

def calculate_non_connected_sides()-> int:
    # Možne smeri
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    # Celotno število odkritih ploskev kock
    total_surface_area: int = 0 
    
    # Premikamo so čez vse kocke
    for cube in cubes:
        # Za vsako kocko imamo na začetku 6 ne zakritih ploskev
        sides_exposed = 6 
        # Za vsako kocko pogledamo 6 možnih sosedov
        for direction in directions:
            neighbor = (cube[0] + direction[0], cube[1] + direction[1], cube[2] + direction[2])
            #!print(f"Cube: {cube} | neighbor: {neighbor}")
            # za vsakega soseda zmanjšamo število odkritih ploskev za 1
            if neighbor in cubes:
                sides_exposed -= 1
                #!print(f"{True} neighbor exists!")
        # Za vsako kocko seštevamo skupno število odkritih ploskev
        total_surface_area += sides_exposed
    
    return total_surface_area

# Part1
output = calculate_non_connected_sides()
print(f"Total number of uncovered sides: {output}")

