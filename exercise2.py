#Rewrite your pay program using try and except so that your program handles 
# non-numeric input gracefully by printing a message and exiting the program. 
# The following shows two executions of the program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

try:
    hrs = input("Please enter your hours worked: ")
    h = float(hrs)
except:
    print("Error, please enter a numeric input")
try:
    rate = input("Please enter the rate you get payed per hour: ")
    r = float(rate)
except:
    print("Error, please enter numeric input")

if h > 40 :
    basePay = ( 40.0 * r)
    otp = (h - 40.0) * (r * 1.5)
    totalPay = (basePay + otp)
    print("Your total pay is: ")
    print (totalPay)
else:
    print("Your total pay is: ")
    print( h * r )