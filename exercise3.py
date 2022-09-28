#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, 
# print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
# < 0.6     F

#Enter score: 0.95
#A
#Enter score: perfect
#Bad score
#Enter score: 10.0
#Bad score
#Enter score: 0.75
#C
#Enter score: 0.5
#F

#Run the program repeatedly as shown above to test the various different values for input.

while True:
    testResult = input("Please input the grade you recievd on the test as a decimal: ")
    grade = float(testResult)
    if grade > 1.0:
        print("Bad Score, Please enter a score between 0.0 and 1.0 ")
        continue
    break
if grade >= .9:
    print("A")
    print("Perfect Score")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
else:
    print ("F")




