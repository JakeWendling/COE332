import names

with open('words', 'r') as infile:
    words = infile.read().splitlines()
    count = 0
    for word in words:
        if len(word.strip(' ')) == 8 and count < 5:
            print(word)
            count += 1
        
