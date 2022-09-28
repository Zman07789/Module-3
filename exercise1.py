#Exercise 1: Rewrite your pay computation to give the employee 1.5 times 
# the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hrs = input("Please input how many hours you worked: ")
h = float(hrs)
rate= input("Please eneter the rate at which you get payed: ")
r = float(rate)
if h > 40 : 
    reg = (40.0 * r)
    otp = (h - 40.0)*(r * 1.5)
    pay = (reg + otp)
    print ("Your pay is: ")
    print (pay)
else:
    npay = (h*r)
    print ("Your pay is: ")
    print(npay)