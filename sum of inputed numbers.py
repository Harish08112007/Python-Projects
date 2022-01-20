l=list(input("Enter a number more than two digit: "))
print(l)
f=0
for i in range(0,len(l)):
    a=int(l[i])
    f+=a
print(f)