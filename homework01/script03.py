import names

def nameLength(name):
    return len(name.replace(" ", ""))

for x in range(5):
    name = names.get_full_name()
    length = nameLength(name)
    print(f'{name} {length}')
