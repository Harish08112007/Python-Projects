n=int(input("Enter a Number: "))
d=1
x=[]
def multiply(x,d):
    for i in range(1,n+1):
        x.append(i)
    for a in x:
        d=d*a
    return d
print("The predisissors of entred number multiplied is", multiply(x,d))