#Desiree Davis
#Practice 1C
#SE126.22
#1/4/20


#PROMPT: Write a temperature conversion treatment with a menu with opetions for F,C, & K. 

#Start Program:

#count temps:
totalCtemps = 0
totalFtemps = 0
totalKtemps = 0

print("Welcome to my Temperature Conversion Program!")
print()
print()
#control variable for while loop

answer = input("Would you like to enter a temperature?[y/n]: ")
print()
print()
#while loop to function as menu -------set up function maybe?---------
#start while loop
while answer == "y" or answer == "Y":
    #output menu
    print("Conversion Menu: \n1.Enter Temp in Fahrenheit\n2.EnteEr Temp in Celsius\n3.Enter Temp in Kelvin\n4.Current Counts\n5.EXIT")
    print()
    #use try/except block to ensure user enters a number
    try:
        choice = int(input("What would you like to do? [enter 1-5] "))
        print()
    except:
        print("You must enter a number between 1 and 5. Try Again.")#control variable for if/else statement
        
        #reprint menu
        print("Conversion Menu: \n1.Enter Temp in Fahrenheit\n2.EnteEr Temp in Celsius\n3.Enter Temp in Kelvin\n4.Current Counts\n5.EXIT")
        print()
        
        #ask for input again
        choice = int(input("What would you like to do? [enter 1-5] ")) #control variable for if/else statement
        print()

    #if user enters 1.Enter Temp in Fahrenheit:
    if choice == 1:
        #enter temp
        temp = float(input("Enter temp here: "))
        
        #update sum total for tempF
        totalFtemps += 1

        #convert to celsius
        tempC = (temp - 32) * (5 / 9)

        #convert to kelvin
        tempK = tempC + 273.15

        #print converted temps
        print("Fahrenheit: {0:.1f}\nCelsius: {1:.1f}\nKelvin: {2:.1f}".format(temp, tempC, tempK))

    #if user enters 2. Enter Temp in Celsius
    elif choice == 2:
        #enter temp
        temp = float(input("Enter temp here: "))

        #update sum total for tempC
        totalCtemps += 1
        
        #convert to F and K
        tempF = (temp * (9 / 5)) + 32
        tempK = temp + 273.15

        #print converted temps
        print("Celsius: {0:.1f}\nFahrenheit: {1:.1f}\nKelvin: {2:.1f}".format(temp, tempF, tempK))

    #if user enters 3. Enter Temp in Kelvin
    elif choice == 3:
        #enter temp
        temp = float(input("Enter temp here: "))

        #update sum total for tempK
        totalKtemps += 1

        #convert to F and C
        tempC = temp - 273.15
        tempF = (temp - 273.15) * (9 / 5) + 32

        #print converted temps

    #if user enters 4.Current Counts
    elif choice == 4:
        print()
        print()
        print("Total Fahrenheit conversions: {0}".format(totalFtemps))
        print("Total Celsius conversions: {0}".format(totalCtemps))
        print("Total Kelvin conversions: {0}".format(totalKtemps))

    elif choice == 5:
        print("Thank you for using my program. Goodbye!")
        answer = "n"

    elif choice < 0 or choice > 5:
        print("You must enter a number between 1 and 5. Try Again.")