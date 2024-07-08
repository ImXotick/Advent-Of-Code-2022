import json

# Funkcija, ki preverja posamezne elemente v različnih listih
def compare_list(list1, list2):
    for elem1 in list1:
        for elem2 in list2:
            if(elem1 == elem2):
                continue
            else:
                print(f"False: {elem1} | {elem2}")      
                return False
    return True

# Funkcija, ki skrbi za preveranje celotnega lista
def compare_nested_lists(list1, list2):
    # Premikamo se skozi oba list-a
    for i in range(min(len(list1), len(list2))):
        elem1: list = list1[i]
        elem2: list = list2[i]

        # Preverimo, če je leva stran manjša
        if(len(list1) < len(list2)):
            print(f"List Smaller: {False}")
            return False 
        # Preverimo posamezne elemente
        if not compare_list(elem1, elem2):
            print(f"List Different: {False}")
            return False
    return True

# Tester:
list1 = [[1], [4, 4, 4]]
list2 = [[1], [4]]

pairs = [[json.loads(p) for p in e.splitlines()] for e in open(r'examples\day13\input.txt').read().split("\n\n")]

result = compare_nested_lists(list1, list2)
print(result)
