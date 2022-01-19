fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for w in fh:
    strip = w.rstrip().split()
    for word in strip:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
    
