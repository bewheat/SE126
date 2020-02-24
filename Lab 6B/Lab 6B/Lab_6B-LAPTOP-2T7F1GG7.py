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



#---------------------FUNCTIONS----------------------

#ask user if they want to continue or stop
def menu():
    answer = input("Would you like to choose another seat? [y/n]: ")

    if answer.lower() != "y" and answer.lower() != "n":
        
        answer = input("Would you like to choose another seat? [y/n]: ")

    return answer

def seatnum():
    r = input("What row would you like to sit in? (1-7): ")
        
    n = input("What seat would you like to sit in? (a, b, c, d): ")
    n.upper()

    return




#-----------------START BASE PROGRAM-------------------------

ans = "y"

#initialize lists
colA = ["A","A","A","A","A","A","A"]
colB = ["B","B","B","B","B","B","B"]
colC = ["C","C","C","C","C","C","C"]
colD = ["D","D","D","D","D","D","D"]

for i in range(7):
    print("{4}:{0} {1}   {2} {3}".format(colA[i],colB[i],colC[i],colD[i],(i + 1)))

while ans == "y":
    seat = seatnum()
    print(seat)

    ans = menu()
