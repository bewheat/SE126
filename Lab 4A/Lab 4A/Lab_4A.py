
#Desiree Davis
#Lab 4A
#SE 126.22
#1/28/20


#PROMPT:  In Python, process the text file “lab5.txt” to store each field into its own corresponding list.
    #Process the lists to print the them as they appear in the file
    #Re-process the lists to add the House Motto (dependent on Field4/Allegiance)
    #Re-process the lists to find the average age within the list, then
        #Print the total number of people in the list
        #Print the average age
        #Print tallies for each allegiance (Field4)


#BASE CODE START

#initialize variables
count = 0
age_sum = 0
stark = 0
baratheon = 0
tully = 0
nightswatch = 0
lannister = 0
targaryen = 0


#initialize lists
firstname = []
lastname = []
age = []
nickname = []
house_allegience = []
motto = []

#open file
import csv


#AT SCHOOL
with open("C:/Users/008006221/OneDrive - New England Institute of Technology/New England Tech/Term 2/SE 126/Lab Files/lab4A_GOT.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #count number of records in file
        count += 1

        #process file to store fields into lists
        firstname.append(rec[0])
        lastname.append(rec[1])
        age.append(rec[2])
        nickname.append(rec[3])
        house_allegience.append(rec[4])
        #print(count)TESTING
        
#close file

#process lists to print them as they appear in the file

print("{0:10} {1:9} {2:3} {3:17}  {4:15}".format("First Name", "Last Name", "Age", "Nickname", "House"))

for i in range(count):
    print("{0:10} {1:9} {2:3} {3:17} {4:15}".format(firstname[i],lastname[i],age[i],nickname[i],house_allegience[i]))

#process lists to add the house motto
#   also tallying up num of people in each house
for i in range(count):
    if house_allegience[i] == "House Stark":
        motto.append("Winter is Coming")
        stark += 1

    elif house_allegience[i] == "House Baratheon":
        motto.append("Ours is the fury.")
        baratheon += 1

    elif house_allegience[i] == "House Tully":
        motto.append("Family. Duty. Honor.")
        tully += 1

    elif house_allegience[i] == "Night's Watch":
        motto.append("And now my watch begins.")
        nightswatch += 1

    elif house_allegience[i] == "House Lannister":
        motto.append("Hear me roar!")
        lannister += 1

    elif house_allegience[i] == "House Targaryen":
        motto.append("Fire & Blood")
        targaryen += 1

    else:
        motto.append("*ERROR*")

#end for loop
#print(motto)TESTING

print()
print()
print("-------------------------------------------------------------------------------------------------------------------------------------")
print()
print()

#reprint with house mottos
print("{0:10} {1:9} {2:3} {3:17}  {4:15}  {5:21}".format("First Name", "Last Name", "Age", "Nickname", "House", "Motto"))

for i in range(count):
    print("{0:10} {1:9} {2:3} {3:17} {4:15}  {5:21}".format(firstname[i],lastname[i],age[i],nickname[i],house_allegience[i],motto[i]))
    #print(i)   TESTING
    #print(motto[i])    TESTING

#end for loop
print()
print()


#find average age
for i in range(count):
    age_sum += int(age[i])
    #print(i, age[i], age_sum)  FOR TESTING

avg_age = age_sum / count

print("Total People: ", count)
print("Average Age: {0:.1f}".format(avg_age))
print()
print("House Stark:", stark) #I realize I could put this all in one print statement. This is just easier for me to look at
print("House Baratheon:", baratheon)
print("House Tully:", tully)
print("Night's Watch:", nightswatch)
print("House Lannister:", lannister)
print("House Targaryen:", targaryen)