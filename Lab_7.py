#Desiree Davis
#Lab 7
#SE 126.22
#2/24/20

#------------------------PROMTP----------------------
#           Write a program that gives the user a menu of options to search through the file.
#           Depending on how the user wants to search, you may need to sort the searched-through list before 
#           performing Binary Search.  Binary Search should be used for Menu Options 1 (First Name) and 2 (ID codes)  
#           and the full record for the individual searched should be included if found (the user should be alerted if the 
#           person cannot be found).  If the user chooses options 3 or 4, you must print a list of everyone and their full 
#           record that fits the searched item (think: sequential search!) that has that Last Name or Allegiance.  Use the 
#           GOT_bubble_sort_7.txt file (you may change the name if you wish but you may NOT edit the text file outside 
#           of checking for and deleting empty end records).  The user should be able to search as many times as they 
#           would like.  If the user enters an option that does not exist, the program must tell them this before asking if 
#           the user would like to search for a new record
#                   STIPULATIONS
#                           >The menu should be printed from a function that returns the user’s search selection
#                           >A function must be used to swap values for bubble sort. 
#                           >A function must be used to ask the user if they would like to search again. 
#                                   |This function should only accept the following values from the user: Y,y,N,n
#                           > function to print a goodbye message when the user decides to exit.
#                                   |    10pt BONUS: Add something GOT related to your goodbye message.  This could be a quote, a 
#                                   picture ... get creative (sliding scale bonus points so 1 – 10 based on what you do :] )
#                           >The console screen should clear before each new search.



#-----------------VARIABLE DICTIONARY-----------------
#       count: number of records in file
#       file: file being processed


#------------------LIST DICTIONARY------------------
#       idCode: list of id codes
#       lastName: last names
#       firstName: first names
#       age: ages
#       allegiance: allegiances

#------------------------FUNCTIONS--------------------

def menu():
    #--PROMPT--
    #function to print menu and return the user's selection

    #--VARIABLE DICTIONARY--
    #a: user's menu selection

    print()
    print("---SEARCH MENU---")
    print("1.search by FIRST NAME")
    print("2.search by ID CODE")
    print("3.search by LAST NAME")
    print("4.search by ALLEGIANCE")
    print("5.EXIT")
    a = int(input("Enter selection(1-5): ")

    return a
#end menu()

def swap(listName, index):

    #--PROMPT--
    #swap function for bubble sort

    #--VARIABLE DICTIONARY--
    #   listName: name of list being sorted
    #   index: index value being sorted

    temp_var = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp_var
#end swap()

def again():
    #--PROMPT--
    #asks user if they would like to search again. Only excepts Y,y,N,n

    #--VARIABLE DICTIONARY
    #ans: user's answer

    ans = input("Would you like to search again? [y/n]: ")

    while ans.lower() != "y" and ans.lower() != "n":
        ans = "Would you like to search again? [y/n]: "

#end again()

def goodbye():
    #--PROMPT--
    #   function to print a goodbye message when the user decides to exit.
    #       10pt BONUS: Add something GOT related to your goodbye message.  This could be a quote, a 
    #       picture ... get creative (sliding scale bonus points so 1 – 10 based on what you do :] )

    print("Goodbye") #add something creative later
#end goodbye()


#-----------------------START BASE CODE-------------------------

#initialize variables
count = 0

#initialize lists
idCode = []
lastName = []
firstName = []
age = []
allegiance = []

#open file
import csv

#AT HOME - ARCHLABS
with open("/home/d/Downloads/GOT_bubble_sort_7.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #count records
        count += 1

        #populate lists
        idCode.append(rec[0])
        lastName.append(rec[1])
        firstName.append(rec[2])
        age.append(rec[3])
        allegiance.append(rec[4])
#close file

#print file data
print("{0:10}\t{1:10}\t{2:10}\t{3:10}\t{4:10}".format("ID CODE", "LAST NAME", "FIRST NAME", "AGE", "ALLEGIANCE"))
for i in range(count):
    print("{0:10}\t{1:10}\t{2:10}\t{3:10}\t{4:10}".format(idCode[i], lastName[i], firstName[i], age[i], allegiance[i]))
#end for loop

