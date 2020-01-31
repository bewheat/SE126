#Desiree Daviw
#List Demo
#SE 126.22
#1/29/20


#PROMPT: Write a program that reads the data file (below) and stores the data into lists.  then, process the lists to reprint the file data, record by record. Next, reprocess the lists to find each student's current average score along with the class average.  Store each student's average into a new list called 'avg' and reprint the records to include the average.  Reprocess the lists one more time to find the letter equivalent of the average and store this into a new list called 'let_avg'.  Reprint the lists for a third and final time, record by record including average score and average letter equivalent.  After this third print, print to the console the total number of student's in the class along with the class numeric average. 


#initialize variables
count = 0

#initialize lists
first = []
last = []
test1 = []
test2 = []
test3 = []

#read file
import csv

with open("C:/Users/thewi/OneDrive - New England Institute of Technology/New England Tech/Term 2/SE 126/Lab Files/listPractice1.txt") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        count += 1

        first.append(rec[0])
        last.append(rec[1])
        test1.append(rec[2])
        test2.append(rec[3])
        test3.append(rec[4])

#close file

#print file data
print("{0}  {1}  {2}  {3}  {4}".format("First Name", "Last Name", "Test 1", "Test 2", "Test 3"))

for i in range(count):
    print("{0}  {1}  {2}  {3}  {4}".format(first[i], last[i], test1[i], test2[i], test3[i]))

#end for loop

