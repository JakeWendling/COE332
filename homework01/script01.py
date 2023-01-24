
with open('../../words', 'r') as wordFile:
    words = wordFile.read().splitlines()

words.sort(key=len, reverse=True) #words already sorted alphabetically so length is only key needed

for i in range(5):
    print(words[i])
