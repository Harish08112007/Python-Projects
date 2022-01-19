def computepay(h,r):
    if h<=40:
       return pay = h*r
    else:
        pay1 = r* 40
        remain = h-40
        pay2 = remain*(r*1.5)
        return total =pay1+pay2
        
hrs = input("enter the number of hours:")
h = float(hrs)
rate = input("enter the rate:")
r = float(rate)
p = computepay(h,r)
 

    
    
