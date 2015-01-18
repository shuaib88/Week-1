## - #1 
##A program to convert Celsius temps into Fahrenheit

## - #2
##def Celsius_2_Fahrenheit():
##    print("I'm going to help you convert Celsius to Fahrenheit!")
##    print()
##    celsius = eval(input("What Celsius temp would you like to convert? "))
##    fahrenheit = celsius * 9 / 5 + 32
##    print("The temperature is " + str(fahrenheit) + " degrees fahrenheit ")
##
##Celsius_2_Fahrenheit()

## - #3
##def average_calculator():
##    print("This program computes the average of three exam scores ")
##    print()
##
##    score1, score2, score3 = eval(input("First score?: ")), eval(input("Second score?: ")), eval(input("Third score?: "))
##    average = (score1 + score2 + score3)/ 3
##
##    print("The average of the score is: ", average)
##
##average_calculator()


## - #8

def Fahrenheit_2_Celsius():
    print("I'm going to help you convert Fahrenheit to Celsius!")
    print()
    fahrenheit = eval(input("What Fahrenheit temp would you like to convert? "))
    celsius = (fahrenheit - 32) * 5 / 9 
    print("The temperature is " + str(celsius) + " degrees celsius ")

Fahrenheit_2_Celsius()
