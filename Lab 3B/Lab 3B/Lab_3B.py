#Desiree Davis
#Lab 3B
#SE126.22
#1/22/20

#ORIGINAL PROMPT: 5B Construct a Program that will analyze potential voters. The program should generate the following totals:
# 
#1.   Number of males not eligible to register.
#2.   Number of females not eligible to register.
#3.   Number of males who are old enough to vote but have not registered.
#4.   Number of females who are old enough to vote but have not registered.
#5.   Number of individuals who are eligible to vote but did not vote.
#6.   Number of individuals who did vote.#7.   Number of records processed.

#The program must prompt the user for the ID number, age, gender, if the person is registered to vote, and if the person voted.  You will also have to prompt to see if the user has more data to enter. 

#PROMPT: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective lists, and then process the lists to determine the 7 final output values. This final solution should have NO input() statements and when the console is ran it should print all 7 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 7 totals. 

#SIDENOTE: This lab wasn't assigned when I took SE116 but I have some free time so I'm just gonna write this one up from scratch

#VARIABLE DICTIONARY:
#   records: Num of records(people) processed
#   male_underage: Num of males to young to vote( < 18)
#   female_underage: Num of females to young to vote
#   male_unregistered: Num of males old enough to vote who haven't registered
#   female_unregistered: Num of females old enough to vote who haven't registered
#   no_vote: Num of people registered to vote but didn't
#   total_vote:Num of people wo did vote
#   file: file being processed

#LIST DICTIONARY:
#   id = voter ID num
#   age = person's age
#   gender = person's gender
#   registered = whether person is registered to vote or not
#   voted = whether person voted or not



#START BASE PROGRAM

#initialize count variables
records = 0
male_underage = 0
female_underage = 0
male_unregistered = 0
female_unregistered = 0
no_vote = 0
total_vote = 0


#initialize lists
id = []
age = []
gender = []
registered = []
voted = []

#open file
import csv

print("{0}\t{1}\t{2}\t{3}\t{4}".format("ID","Age","Gender","Registered?","Voted?"))


#NEIT
with open("C:/Users/008006221/OneDrive - New England Institute of Technology/New England Tech/Term 2/SE 126/Lab Files/voters.csv") as csvfile:

#MY LAPTOP
#with open("C:/Users/thewi/OneDrive - New England Institute of Technology/New England Tech/Term 2/SE 126/Lab Files/voters.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1


        id.append(rec[0])
        age.append(int(rec[1]))
        gender.append(rec[2])
        registered.append(rec[3])
        voted.append(rec[4])


        print("{0}\t{1}\t  {2:6}     {3:10}\t  {4}".format(rec[0],rec[1],rec[2],rec[3],rec[4]))
#END OF FILE

#process voters
for i in range(records):


    #seperate voters based on gender
    if gender[i] == "M":
        
        #count underage males
        if age[i] < 18:
            male_underage += 1
        
            #count males not registered to vote
        if registered[i] == "N" and age[i] >= 18:
            male_unregistered += 1

    #females
    if gender[i] == "F":

        #count underage females
        if age[i] < 18:
            female_underage += 1

        #count unregistered females
        if registered[i] == "N" and age[i] >= 18:
            female_unregistered += 1

    #count who didn't vote but could
    if age[i] >= 18 and registered[i] == "Y" and voted[i] == "N":
        no_vote += 1
    
    #count who did vote
    elif voted[i] =="Y":
        total_vote += 1


#end for loop

print()
print()
print("Total Processed: {0}\nUnderage Males: {1}\nUnderage Females: {2}\nUnregistered Males: {3}\nUnregistered Females: {4}\nVoted: {5}\nDidn't Vote: {6}".format(records, male_underage, female_underage, male_unregistered,female_unregistered, total_vote, no_vote))