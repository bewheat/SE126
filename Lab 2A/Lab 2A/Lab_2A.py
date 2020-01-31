#Desiree Davis
#Lab 2A
#SE 126.22
#1/14/20


#PROMPT: Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list.

#Variable Dictionary:
#   records: number of records in file
#   rooms: number of rooms over capacity. Not the most descriptive variable name but it does the trick
#   room_name: name of room program is processing
#   room_limit: capacity of room program is processing
#   people_registered: number of people registering to attend
#   waitlist: number of people who cannot attend/must be put on a waitlist
#           [people_registered - room_limit]






#START BASE PROGRAM:

#initialize variables for later use
records = 0
rooms = 0



#Header
print("{0:18} \t\t {1}".format("ROOM:", "OVER CAPACITY:"))

import csv #use to read file

#open file

#ON MY LAPTOP:**********************************************************************
#with open("C:/Users/thewi/OneDrive - New England Institute of Technology/New England Tech/Term 2/SE 126/Lab Files/lab2a.csv") as csvfile:


#ON SCHOOL COMPUTER*******************************************************************************
with open("C:/Users/008006221/OneDrive - New England Institute of Technology/New England Tech/Term 2/SE 126/Lab Files/lab2a.csv") as csvfile:
    file = csv.reader(csvfile)
    
    #iterate through file
    for rec in file:
        #keep track of number of times file is looped through
        records += 1
        
        
        #print(records) #for testing

        #put fields into their own variables for the sake of my thought process(it's late ok leave me alone)
        room_name = rec[0]
        room_limit = int(rec[1])
        people_registered = int(rec[2])
        
        #use if statement to print room if it's over capacity
        if room_limit < people_registered:
            #count rooms that are over capacity
            rooms += 1
            
            #calculate how many people need to be uninvited, i'm sorry, 'waitlisted'
            waitlist = people_registered - room_limit

            print("{0:18} \t\t {1:3}".format(room_name, waitlist))

#close file
#print("End of the line") #for testing

print()
print()
print("Rooms Processed: {0} \nOver Capacity: {1}".format(records, rooms))