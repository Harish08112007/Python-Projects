#generate a random number which is multiple of a number and print the result as a multiplication
import random
a=int(input("Enter a multile of a number"))
b=random.randrange(1,100,a)
print(a,"x",b//a,"=",b)