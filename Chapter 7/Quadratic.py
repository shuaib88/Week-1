
import math #Makes the math library available

def quadratic():
    print("this program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coeffients (a, b, c): "))

    discrim = b ** 2 - 4 * a * c
    if discrim >= 0 : 
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print()
        print("The solutions are:", root1, root2)

    if discrim < 0:
        print("The solution does not exist")

vs.

def quadratic():
    print("this program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coeffients (a, b, c): "))

    discrim = b ** 2 - 4 * a * c
    if discrim >= 0 : 
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print()
        print("The solutions are:", root1, root2)

    else :
        print("The solution does not exist")
quadratic()

