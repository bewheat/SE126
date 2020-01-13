#Desiree Davis
#Lab 1C
#SE 126.22
#1/6/20


#Prompt: Write a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend.  If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations.  The user should be allowed to enter as many rooms as the want. 



#Variable Dictionary:
#   again: control variable for while loop. Asks user if they would like to enter additional rooms
#   cap: Room capacity
#   attending: Amount of people attending meeting
#   rem_space: Amount of space remaining.
#              [cap - attending]
#   overcap: How far over capacity room is
#            [attending - cap]





#FUNCTIONS:

#ask for capacity and return value
def capacity():
    maxcap = int(input("What is the rooms capacity? "))
    return maxcap
#END capacity

#ask for number of people attending and return value
def attendees():
    att = int(input("How many people will be attending? "))
    return att
#END attendees

#return the difference between room capacity and attendees
def register(x,y):
    difference = x - y
    return difference
#END register

#ask user if they want to check anymore rooms
def check():
    answer = input("Would you like to check another room? [y/n]: ")
    answer = answer.lower()

    #put in while loop to ensure user answers with either "y", "Y", "n", or "N"
    while answer != "y" and answer != "n":
        answer = input("Would you like to check another room? [y/n]: ")
        answer = answer.lower()
    return answer
    #end while loop
#END check




#PROGRAM START:

#Control variable for while loop
again = "y"


#use while loop to allow user to enter as many rooms as they'd like to
while again == "y":
    #Ask user for room capacity and number of attendees
    cap = capacity()
    attending = attendees()

    #use if statement to determine if more people can attend
    if attending < cap:
        #subtract attending from cap to determine remaining space
        rem_space = register(cap, attending)

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
        overcap = register(attending, cap)

        print("You are over capacity. You will have to exclude {0} people to meet fire regulations".format(overcap))
        print()
        print()
    #end else statement

    #Ask if user would like to enter another room
    again = check()

#end while loop

