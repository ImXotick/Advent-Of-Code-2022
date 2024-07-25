import json

# Funkcija, ki preverja elemente seznama
def compare_lists(list1, list2):
    #* print(f"List1: {list1} \nList2: {list2}")

    # Preverimo, če sta oba elementa tipa int
    if isinstance(list1, int) and isinstance(list2, int):
        # Preverimo, če sta elementa enaka, če sta vrnemo "Same"
        if list1 == list2:
            return "Same"
        # Če nista enaka vrnemo bool (True, False) glede na to, če je el1 manjši od el2 
        else: 
            return list1 < list2
        
    # Preverimo, če sta oba elementa tipa list
    if isinstance(list1, list) and isinstance(list2, list):
        # Iteriramo skozi oba seznama hkrati z uporabo zip
        for e1, e2 in zip(list1, list2):
            #* print(f"El1: {e1} | El2: {e2}")
            # Za vsak par recurzivno pokličemo compare_lists
            if (comparison := compare_lists(e1, e2)) is not "Same":
                return comparison # Vrnemo, če rezultat ni Same
        return compare_lists(len(list1), len(list2)) # Primerja dolžini seznamov in vrnemo rezultat primerjave dolžin
    # Če je list1 tipa int in list2 tipa list pretvorimo list1 v seznam z enim elementom in ponovno pokličemo compare_lists.
    if isinstance(list1, int):
        return compare_lists([list1], list2)
    # Če je list2 tipa int in list1 tipa list pretvorimo list2 v seznam z enim elementom in ponovno pokličemo compare_lists.
    else: 
        return compare_lists(list1, [list2])

pairs = [[json.loads(p) for p in e.splitlines()] for e in open(r'examples\day13\input.txt').read().split("\n\n")]

summed_val = 0
for i, (left, right) in enumerate(pairs, 1):
    # Če je levi del manjši od desnega se index para prišteje k spremenljivki sum
    if compare_lists(left, right):
        # Dodamo index v sum
        summed_val += i

# Izpišemo sum
print(summed_val)

#* print(pairs)
packets = []
for pair in pairs:
    for p in pair:
        packets.append(p)
#* print(packets)

# Sprehodimo se skozi vsak element v seznamu in preverimo, če funkcija compare_lists vrne True za ta element in seznam [[2]]
position1 = 1  # Začnemo z 1
for p in packets:
    if compare_lists(p, [[2]]):
        position1 += 1

# Sprehodimo se skozi vsak element v seznamu in preverimo, če funkcija compare_lists vrne True za ta element in seznam [[6]]
position2 = 2  # Začnemo z 2
for p in packets:
    if compare_lists(p, [[6]]): 
        position2 += 1

# Izračunamo produkt position1 in position2 ter ga izpišemo
result = position1 * position2
print(result)