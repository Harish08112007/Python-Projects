hrs = input("enter the number of hours:")
h= float(hrs)
rate = input("enter the rate:")
r= float(rate)
if h<=40:
    pay = float(h*r)
    print(pay)
else:
    pay = 40*r
    remain = h-40
    pay1= remain*(r*1.5)
    tot= pay+pay1
    print(tot)
    

