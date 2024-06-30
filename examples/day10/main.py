# Preberemo vsako vrstico in jih skupaj shranimo v list
input = [line.split(' ') for line in open(r'examples\day10\input.txt').read().splitlines()]

# Funkcija, ki dobi signal
def get_signal_strength():
    signalStrength = 0 # Moč singala
    register = 1 # Trenutni register
    cycle = 0 # Trenutni cikel
    prev = 0 # Prejšnji cikel

    for item in input: 
        # Preverimo, če je trenutni element(item) na mestu 0 noop
        if(item[0] == "noop"):
            # Preverimo trenutni cikel
            if(cycle == 20 or cycle == prev + 40):
                signalStrength += register * cycle
                prev = cycle
                print(f"| Cycle: {cycle} | Register: {register} | Strength: {signalStrength} |")
            cycle += 1
        else:
            # Izvajanje navodila
            for i in range(2):
                cycle += 1
                # Preverimo trenutni cikel
                if(cycle == 20 or cycle == prev + 40):
                    signalStrength += register * cycle
                    prev = cycle 
                    print(f"| Cycle: {cycle} | Register: {register} | Strength: {signalStrength} |")
                if(i == 1):
                    register += int(item[1])
    return signalStrength

#Izpis
output = get_signal_strength()
print(output)