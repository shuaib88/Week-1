## Chapter 3 Notes

# change.py
##A program to calculate the value of some change in dollars


##def change_counter():
##    print("Change Counter")
##    print()
##    print("Please enter the count of each coin type.")
##
##    quarters = eval(input("Quarters: "))
##    dimes = eval(input("Dimes: "))
##    nickels = eval(input("Nickels: "))
##    pennies = eval(input("Pennies: "))
##
##    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
##
##    print()
##    print("The total value of your change is ", total)
##    return(total)
##
##change_counter()


##quadratic.py
##a program that determines te real roots of a quadratic equation
##illustrates use of math library
##note this program crashes if the equation has no real roots


##import math #Makes the math library available
##
##def quadratic():
##    print("this program finds the real solutions to a quadratic")
##    print()
##
##    a, b, c = eval(input("Please enter the coeffients (a, b, c): "))
##
##    discRoot = math.sqrt(b * b - 4 * a * c)
##    root1 = (-b + discRoot) / (2 * a)
##    root2 = (-b - discRoot) / (2 * a)
##
##    print()
##    print("The solutions are:", root1, root2)
##
##quadratic()

##def factorialize ():
##
##    fact = eval(input("what number you like to factorialize? "))
##
##    for i in (list(range(1, fact))):
##        fact = fact * i
##
##    print(fact)
##    return(fact)
##
##factorialize()

def main():
    x = 2
    y = 10
    for j in range(0, y, x):
        print(j, end= "")
        print(x + y)
        
    print("done")

main()

   
