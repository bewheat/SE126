#Desiree Davis
#Lab 6B
#SE 126.22
#2/18/2020

#------------------------PROMPT---------------------
#           Write a Python program to assign passengers seats in an airplane.  Assume a small airplane.
#           The program should display the seat pattern, with an ‘X’ making the seats already assigned.
#           After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  
#           This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the 
#           program should say that the seat is occupied and ask for another choice.
#               --You must use FUNCTIONS that allows the user to enter the row and seat number.  The row should be asked for separately from the seat number (two inputs)
#               --You must use a FUNCTION that asks the user in they want to continue or stop. The function should only accept an uppercase or lowercase y or n.


#---------------VARIABLE LIBRARY--------------------
#           ans: would user like to choose another seat or exit program
#           seat: seat chosen by user



#------------------LIST LIBRARY---------------------
#           colA: column A
#           colB: column B
#           colC: column C
#           colD: column D
#           taken: seats user has decided to pick


#---------------------FUNCTIONS----------------------

#ask user if they want to continue or stop
def menu():
    
    #--PROMPT--
    #   allow user to choose another seat or exit the program

    #--VARIABLE LIBRARY--
    #   answer: user's response


    answer = input("Would you like to choose another seat? [y/n]: ")

    while answer.lower() != "y" and answer.lower() != "n":
        
        answer = input("Would you like to choose another seat? [y/n]: ")

    return answer

def seatnum():

    #--PROMPT--
    #   ask user where they want to sit

    #--VARIABLE LIBRARY--
    #   r = seat row (number between 1 and 7; 7 rows)
    #   n = seat in row (letter between A,B,C,D)


    r = input("What row would you like to sit in? (1-7): ")
        
    n = input("What seat would you like to sit in? (a, b, c, d): ")
    n = n.upper()

    #return("{0}[{1}]".format(n,r))
    return r,n




#-----------------START BASE PROGRAM-------------------------

#initial control variable for while loop
ans = "y"

#initialize lists
colA = ["A","A","A","A","A","A","A"]
colB = ["B","B","B","B","B","B","B"]
colC = ["C","C","C","C","C","C","C"]
colD = ["D","D","D","D","D","D","D"]
taken = []


#print seat map
print("ROW")
for i in range(7):
    print("{4}:   {0} {1}   {2} {3}".format(colA[i],colB[i],colC[i],colD[i],(i + 1)))

while ans.lower() == "y":
    seat = seatnum()
    #print(seat) #TESTING

    for x in range(len(taken)):
        if seat == taken[x]:
            print("\n\nSeat is already taken :( Try Again.")
    
    #add chosen seat to list of seats chosen by user
    taken.append(seat)

    #iterate through list of taken seats
    for s in taken:
         
        #print(s) #TESTING
        #search for seat #
        for i in range(len(colA)):
            
            #print(i) #TESTING
            #if the chosen row == index find seat
            if int(s[0]) == i + 1:

                #search for seat in row
                #if seat is found exchange seat letter with X to show it is taken

                #column A
                if s[1] == "A":

                    colA[i] = "X"

                #column B
                elif s[1] == "B":

                    colB[i] = "X"

                #column C
                elif s[1] == "C":

                    colC[i] = "X"

                #column D
                elif s[1] == "D":

                    colD[i] = "X"
                #end of if/else statement. No more seats to search through
            #end if/else statement
        #end inner loop
    #end outter search loop

    print()
    print()
    print("ROW")
    for i in range(7):
        print("{4}:   {0} {1}   {2} {3}".format(colA[i],colB[i],colC[i],colD[i],(i + 1)))


    ans = menu()
#end while loop
print()
print()
print("Goodbye!")