#Desiree Davis
#Lab 1C
#SE 126.22
#1/6/20


#Prompt: Write a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend.  If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations.  The user should be allowed to enter as many rooms as the want. 



#Variable Dictionary:
#   answer: control variable for while loop. Asks user if they would like to enter additional rooms
#   cap: Room capacity
#   attending: Amount of people attending meeting
#   rem_space: Amount of space remaining.
#              [cap - attending]
#   overcap: How far over capacity room is
#            [attending - cap]


#Program Start:

#Control variable for while loop
answer = "y"


#use while loop to allow user to enter as many rooms as they'd like to
while answer == "y" or answer == "Y":
    #Ask user for room capacity and number of attendees
    cap = int(input("What is the rooms capacity? "))

    attending = int(input("How many people will be attending? "))

    #use if statement to determine if more people can attend
    if attending < cap:
        #subtract attending from cap to determine remaining space
        rem_space = cap - attending

        print("You can allow {0} additional people to attend without violating fire regulations.".format(rem_space))
        print()
        print()
    #end if statement

    #use elif statement to determine if room is at capacity
    elif attending == cap:
        print("You are at capacity. No one needs to be excluded but no one else can attend.")
        print()
        print()
    #end elif statement

    #use else statement to determine if room is over capacity
    else:
        #subtract cap from attending to determine how many people need to be excluded
        overcap = attending - cap

        print("You are over capacity. You will have to exclude {0} people to meet fire regulations".format(overcap))
        print()
        print()
    #end else statement

    #Ask if user would like to enter another room
    answer = input("Would you like to check another room? [y/n]: ")

    #put in while loop to ensure user answers with either "y", "Y", "n", or "N"
    while answer != "y" and answer != "Y" and answer != "N" and answer != "n":
        answer = input("Would you like to check another room? [y/n]: ")
    #end inner while loop

#end while loop

