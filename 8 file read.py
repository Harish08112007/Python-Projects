fname = input("Enter a file name:")
fh = open(fname)
inp = fh.read()
inp = inp.upper()
inp = inp.rstrip()
print(inp)