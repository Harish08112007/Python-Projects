import re
fil=input('enter file')
if len(fil)<1:
    fil='actual.txt'
file=open(fil)
sum=0
sl=list()
for line in file:
    line.rstrip()
    numbers=re.findall('[0-9]+',line)
    for number in numbers: 
        sum = sum + int(number)
print(sum)
