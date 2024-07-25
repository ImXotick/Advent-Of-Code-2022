# Preberemo vsako vrstico in jih skupaj shranimo v list
input = [tuple(line.split(' ')) for line in open(r'examples\day10\input.txt').read().splitlines()]

# Funkcija, ki kreira nov sprite
def create_sprint(register: int):
    sprite: str = ""

    for i in range(40):
        if i == register - 1 or i == register or i == register + 1:
            sprite += "#"
        else:
            sprite += "."

    return sprite

# Funkcija, ki skrbi za zapisovanje CRT-ja
def write_CRT(sprite: str, CRT: str, saver: list):
    crtLength: int = len(CRT)
    
    if sprite[crtLength] == "#":
        CRT += "#"
    else:
        CRT += "."
    if len(CRT) == 40:
        saver.append(CRT)
        CRT = ""
    return CRT

# Funkcija, ki dobi signal
def get_signal_and_CRT(input: list):
    signalStrength: int = 0 # Moč singala
    register: int = 1 # Trenutni register
    cycle: int = 0 # Trenutni cikel
    prev: int = 0 # Prejšnji cikel
    sprite: str = "###....................................." # Trenutni sprite
    saver: list = [] # CRT shranjevalec
    CRT: str =  "" # Trenutni CRT

    for item in input: 
        
        # Preverimo, če je trenutna operacija noop
        if item[0] == "noop":
            cycle += 1
            """
            #! Ni potrebno
            # Preverimo trenutni cikel
            if cycle == 20 or cycle == prev + 40:
                signalStrength += register * cycle
                prev = cycle 
            """
            # Ob noop-u samo zapišemo CRT brez kreiranja sprita
            CRT = write_CRT(sprite, CRT, saver)
        else:
            # Izvajanje navodila
            for i in range(2):
                cycle += 1

                # Preverimo trenutni cikel
                if cycle == 20 or cycle == prev + 40:
                    signalStrength += register * cycle
                    prev = cycle 
                    #* print(f"| Cycle: {cycle} | Register: {register} | Total Strength: {signalStrength} |")
                # Če se izvajanje začne zapišemo CRT s trenutnim spriteom
                if i == 0:
                    CRT = write_CRT(sprite, CRT, saver)
                # Če se izvajanje, končuje zapišemo CRT s trenutnim spriteom in kreiramo nov sprite    
                else:
                    register += int(item[1])
                    CRT = write_CRT(sprite, CRT, saver)
                    sprite = create_sprint(register)

    return { 'signal': signalStrength, 'CRT': saver}

#Izpis
output = get_signal_and_CRT(input)

print(f"Total signal strength: {output['signal']}")
for item in output['CRT']:
    print(item)