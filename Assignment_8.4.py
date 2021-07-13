fname = input('Enter file name: ')
fh = open(fname)
lst = list()

for line in fh :
    line = line.strip()
    list_words = line.split()

    for word in list_words :
        if word in lst : continue
        else :
            lst.append(word)
lst.sort()
print(lst)
