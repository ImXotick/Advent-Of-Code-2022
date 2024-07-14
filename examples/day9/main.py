class Position:

    # x in y pozicija
    x: int
    y: int

    # Constructor
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    # Spremenimo trenutno pozicijo in dodamo pozicija tail-a kot že obiskano
    def change_cord(self, x: int, y: int):
        self.x = x
        self.y = y

    # Izpiše trenutno pozicijo
    def display_cord(self):
        print(f"X: {self.x} | Y: {self.y}")

# Funckcija, ki vrne število že obiskanih kordinatov
def get_tail_positions(H_position: Position, T_position: Position) -> int:
    visited_cords = set() # Shranjuje že obiskane kordinate

    # Za vsako pot vzamemo smer in število premikov
    for direction, move_amount in paths:
        # Premikamo se za vsak premik
        for _ in range(int(move_amount)):
            # Preverjamo glede na smer
            if direction == "U":
                H_position.change_cord(H_position.x, H_position.y + 1)
            elif direction == "D":
                H_position.change_cord(H_position.x, H_position.y - 1)
            elif direction == "L":
                H_position.change_cord(H_position.x - 1, H_position.y)
            else:
                H_position.change_cord(H_position.x + 1, H_position.y)

            # Preverimo, če je razlika večja od 1 med pozicijami Hx - Tx ali Hy - Ty
            if not (abs(H_position.x - T_position.x) > 1 or abs(H_position.y - T_position.y) > 1):
                continue

            # Če je razlika spremenimo kordinate T in ga dodamo v visited_cords set za shrambo
            if direction == "U":
                T_position.change_cord(H_position.x, H_position.y - 1)
            elif direction == "D":
                T_position.change_cord(H_position.x, H_position.y + 1)
            elif direction == "L":
                T_position.change_cord(H_position.x + 1, H_position.y)
            else: 
                T_position.change_cord(H_position.x - 1, H_position.y)
            visited_cords.add((T_position.x, T_position.y))

    # Izpišemo število obiskanih kordinat + 1, zaradi začetnega mesta
    return len(visited_cords) + 1

paths = [tuple(line.split(' ')) for line in open(r'examples\day9\path.txt').read().splitlines()]

H_position = Position(1, 1)
T_position = Position(1, 1)

# Part 1
result = get_tail_positions(H_position, T_position)
print(result)

