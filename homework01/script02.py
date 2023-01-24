import names

count = 0
while count < 5:
    name = names.get_full_name()
    if len(name.strip(' ')) == 8:
        print(name)
        count += 1
