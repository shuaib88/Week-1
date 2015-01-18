## - #8 page 54
##The following program will convert celsius temperatures into fahrenheit

def Fahrenheit_2_Celsius():
    print("I'm going to help you convert Fahrenheit to Celsius!")
    print()
    fahrenheit = eval(input("What Fahrenheit temp would you like to convert? "))
    celsius = (fahrenheit - 32) * 5 / 9 
    print("The temperature is " + str(celsius) + " degrees celsius ")

Fahrenheit_2_Celsius()



