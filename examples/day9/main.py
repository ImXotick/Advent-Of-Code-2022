class Position:

    # x in y pozicija
    x: int
    y: int

    # Constructor
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Izpiše trenutno pozicijo
    def display_cord(self):
        return f"X: {self.x} | Y: {self.y}"

# Funkcija za določitev strani premika
def get_add_number(prev_num: int, cur_num: int) -> int:
    if prev_num > cur_num:
        return -1
    elif prev_num < cur_num:
        return 1
    else:
        return 0

# Funckcija, ki vrne število že obiskanih kordinatov
def get_unique_tail_positions(tail_length) -> int:
    visited_cords = set() # Shranjuje že obiskane kordinate
    positions: list = [] # Shranjuje vse kordinate
    
    # kreiramo "Tails" in jim dodamo začetno pozicijo
    for _ in range(tail_length):
        position = Position(0, 0)
        positions.append(position)

    # Za vsako pot vzamemo smer in število premikov
    for direction, move_amount in paths:
        # Premikamo se za vsak premik
        for _ in range(int(move_amount)):
            if direction == "U":
                positions[0].y += 1
            elif direction == "D":
                positions[0].y -= 1
            elif direction == "R":
                positions[0].x += 1
            else:
                positions[0].x -= 1

            # Premikamo vsak "tail" 
            for i in range(len(positions)):
                if i == 0: continue # Če je head začnemo drug krog z i = 1

                # Preverimo, če je razlika med pozicijami večja od 1
                x_diff = abs(positions[i - 1].x - positions[i].x)
                y_diff = abs(positions[i - 1].y - positions[i].y)
                
                if not x_diff > 1 or y_diff > 1:
                    continue

                # Preverimo razliko med pozicijami in premikamo "tali-e" glede na razmike
                if x_diff > y_diff:
                    new_x = get_add_number(positions[i - 1].x, positions[i].x)
                    positions[i].x = positions[i - 1].x + new_x
                    positions[i].y = positions[i - 1].y
                elif x_diff < y_diff:
                    new_y = get_add_number(positions[i - 1].y, positions[i].y)
                    positions[i].x = positions[i - 1].x
                    positions[i].y = positions[i - 1].y + new_y
                else:
                    new_x = get_add_number(positions[i - 1].x, positions[i].x)
                    new_y = get_add_number(positions[i - 1].y, positions[i].y)
                    positions[i].x = positions[i - 1].x + new_x
                    positions[i].y = positions[i - 1].y + new_y

                # Če se i enak zadnjemu "tail-u" zabeležimo njegovo pozicijo 
                if i == len(positions) - 1:
                    visited_cords.add((positions[i].x, positions[i].y))

    # Izpišemo število obiskanih kordinat + 1, zaradi začetnega mesta
    return len(visited_cords) + 1

paths = [tuple(line.split(' ')) for line in open(r'examples\day9\path.txt').read().splitlines()]

# Part 1
result = get_unique_tail_positions(2)
print(f"Number of visited positions for part1: {result}")

# Part 2
result = get_unique_tail_positions(10)
print(f"Number of visited positions for part2: {result}")
