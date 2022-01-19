fname = input("Enter file name: ")
fh = open(fname)
lest=[]
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line
    num = x.find("0")
    cut = x[num:]
    flip = float(cut)

    lest.append(flip)
    
for i in lest:
    count = count+1
    total = total+i
print("Average spam confidence:",total/count)
        
    
