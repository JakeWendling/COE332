import names

for x in range(5):
    name = names.get_full_name()
    length = len(name.replace(" ", ""))
    print(f'{name} {length}')
