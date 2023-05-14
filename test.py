f = open("5Letter.txt")
words = f.read().split("\n")

for i in range(len(words)):
    words[i] = words[i].upper()

with open(r'trial.txt', 'w') as fp:
    for item in words:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')
