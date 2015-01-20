## Chapter 7 notes - Decision Structures


##def Celsius_2_Fahrenheit():
##    print("I'm going to help you convert Celsius to Fahrenheit!")
##    print()
##    celsius = eval(input("What Celsius temp would you like to convert? "))
##    fahrenheit = 9 / 5 * celsius + 32
##    print("The temperature is " + str(fahrenheit) + " degrees fahrenheit ")
##
##Celsius_2_Fahrenheit()
##
##
##
##
##input the temp in Celsius
##
##Calculate fahrenheit
##
##Output fahrenheit
##
##If farenheit > 90
##    print a heat warning
##If farenheit < 30
##    print a cold warning



##
##def Celsius_2_Fahrenheit():
##    print("I'm going to help you convert Celsius to Fahrenheit!")
##    print()
##    celsius = eval(input("What Celsius temp would you like to convert? "))
##    fahrenheit = 9 / 5 * celsius + 32
##    print("The temperature is " + str(fahrenheit) + " degrees fahrenheit ")
##
##    if fahrenheit > 90:
##        print("It's hot, nigga")
##    if fahrenheit < 30:
##        print("It's cold, put on a jacket dummy")
##
##Celsius_2_Fahrenheit()


##import math #Makes the math library available
##
##def quadratic():
##    print("this program finds the real solutions to a quadratic")
##    print()
##
##    a, b, c = eval(input("Please enter the coeffients (a, b, c): "))
##
##    discrim = b ** 2 - 4 * a * c
##    if discrim > 0 :
##            discRoot = math.sqrt(b * b - 4 * a * c)
##            root1 = (-b + discRoot) / (2 * a)
##            root2 = (-b - discRoot) / (2 * a)
##            print()
##            print("The solutions are:", root1, root2)
##
##    elif discrim == 0:
##            discRoot = math.sqrt(b * b - 4 * a * c)
##            root1 = (-b + discRoot) / (2 * a)
##            print("The solution is", root1)
##
##    else:
##        print("The solution does not exist")
##quadratic()

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
##    print()
##    print("The solutions are:", root1, root2)
##
##    except ValueError:
##        print("The solution does not exist")
##quadratic()



def sort():
    x1, x2, x3 = eval(input("Please enter three values: "))

    


    # missing code sets max to the value of the largest)


    print("The largest value is", max)



    
