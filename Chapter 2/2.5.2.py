##x, y = eval(input("what would you like to evaluate? ")), eval(input("what else would you like to evaluate? "))
## 
##
##x, y = y, x 
##
##sum, diff = x + y, x - y
 
### avg2.py
##A simple program to average two exam scores
##Illustrates use of multiple input

##def main():
##    print("This program computes the average of two exam scores.")
##
##    score1, score2 = eval(input("Enter two scores separated by a comma: "))
##    average = (score1 + score2)/ 2
##
##    print("The average of the score is: ", average)
##
##main()

##def yoName():
##    FirstName, LastName = input("what is your first name? "), input ("last name? ")
##    print(FirstName + " " + LastName)
##
##yoName()

##program interest calculator

def interest():
    print("This program will calculate your future loan obligation")
    principal = eval(input("How much is your house worth currently? "))
    years = eval(input("How many years in the future do you want to predict? "))
    apr = eval(input("What is your annual percent rate? "))

    for years in range(years):
        principal = principal * (1 + (apr / 100))

    principal = int(principal)

    print(principal)


interest()

