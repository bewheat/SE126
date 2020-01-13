#Desiree Davis
#Practice 1
#SE126.22
#1/1/20


#Prompt: Write a Fahrenheit-to-Celsius conversion program that allows the user to enter as many temperatures in Fahrenheit they would like. Ask how many temperatures the user is going to input at beginning of program and edit while loop accordingly. Add function to convert temp from F to C. 

#Variable Library:
#   sumtotalTemps: will hold sum of all Fahrenheit tems 
#   totalTemps: will hold total number of all Fahrenheit temps entered
#   answer: control variable for while loop to allow user to enter multiple temps
#   tempF: temp in Fahrenheit
#   tempC: temp in Celsius:
#           (tempF-32) * (5/9)
#   avgTempF: average of temperatures in Fahrenheit
#           sumtotalTemps / totalTemps
#   avgTempC: average of temperatures in Celsius
#           (avgTempF - 32) * (5/9)




#Functions
#conversion function
def ftoC(f):
    #convert from F to C
    tempC = (f-32) * (5/9)
    return tempC


#Program Start:

#variables:
sumtotalTemps = 0
totalTemps = 0

#greet user
print("Welcome to my Fahrenheit-to-Celcius conversion Program!")

#control variable for while loop
#add try/except to confirm number was entered
try:
    answer = int(input("How many temperatures do you plan on converting?: "))

except:
    print("You have to enter a number. Try Again")
    answer = int(input("How many temperatures do you plan on converting?: "))


#use if/else statement to ensure user entered a number greater than zero
if answer == 0:
    print("You don't plan on converting anything. Goodbye.")

else:
    #while loop to convert all the temps
    #while loop starts
    while answer > 0:
        #prompt user for temp
        tempF = float(input("Enter temperature in Fahrenheit here: "))
        print()
        print()

        #update sum total
        sumtotalTemps += tempF

        #update total number of temps
        totalTemps += 1.0

        #convert temp to Celsuis
        tempC = ftoC(tempF)

        #output total temps entered, tempF, & tempC rounded to the 1st decimal
        print()
        print()
        print("Total Temperatures Entered So Far: {0:5.0f} \nTemperature in Fahrenheit:            {1:5.1f} \nTemperature in Celsius:              {2:5.1f}".format(totalTemps, tempF, tempC))

        #control variable
        answer -= 1
#end while loop


    #average of Fahrenheit temps
    avgTempF = sumtotalTemps / totalTemps

    #average of Celsius Temps
    avgTempC = (avgTempF-32) * (5/9)

    #output total temps entered, avg of tempF, & avg of tempC
    print()
    print()
    print("Total Temperatures Entered:         {0:5.0f} \nAverage of Temperatures in Fahrenheit: {1:5.1f} \nAverage of Temperatures in Celsius:    {2:5.1f}".format(totalTemps, avgTempF, avgTempC))
