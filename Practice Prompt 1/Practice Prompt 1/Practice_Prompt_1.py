#Desiree Davis
#Practice 1
#SE126.22
#1/1/20


#Prompt: Write a Fahrenheit-to-Celsius conversion program that allows the user to enter as many temperatures in Fahrenheit they would like.

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


#Program Start:

#variables:
sumtotalTemps = 0
totalTemps = 0

#greet user
print("Welcome to my Fahrenheit-to-Celcius conversion Program!")

#control variable for while loop
answer = input("Would you like to enter a temperature in Fahrenheit to convert to Celsius? [y/n]: ")

#use while loop to allow user to enter as many temps as they want
#while loop starts
while answer =='y' or answer == 'Y':
    #prompt user for temp
    tempF = float(input("Enter temperature in Fahrenheit here: "))

    #update sum total
    sumtotalTemps += tempF

    #update total number of temps
    totalTemps += 1.0

    #convert temp to Celsuis
    tempC = (tempF-32) * (5/9)

    #output total temps entered, tempF, & tempC rounded to the 1st decimal
    print()
    print()
    print("Total Temperatures Entered So Far: {0:5.0f} \nTemperature in Fahrenheit:            {1:5.1f} \nTemperature in Celsius:               {2:5.1f}".format(totalTemps, tempF, tempC))

    #control variable
    print()
    print()
    answer = input("Would you like to convert another temperature? [y/n]: ")
#end while loop
if totalTemps == 0:
    print("You didn't convert anything. \nGoodbye.")
else:
    #average of Fahrenheit temps
    avgTempF = sumtotalTemps / totalTemps

    #average of Celsius Temps
    avgTempC = (avgTempF-32) * (5/9)

    #output total temps entered, avg of tempF, & avg of tempC
    print()
    print()
    print("Total Temperatures Entered:         {0:5.0f} \nAverage of Temperatures in Fahrenheit: {1:5.1f} \nAverage of Temperatures in Celsius:    {2:5.1f}".format(totalTemps, avgTempF, avgTempC))