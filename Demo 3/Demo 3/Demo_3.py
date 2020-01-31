#Desiree Davis
#Lab 2B
#SE 126.22
#1/14/20



#PROMPT: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. The last line should print the number of computers in the file.


#Variable Dictionary
#   records = keep count of records processed
#   comp_list = file being read
#   rec = record being processed
#   column1: computer type
#   column2: computer brand
#   column3: computer CPU
#   column4: computer RAM
#   column5: 1st hard drive size
#   column6: number of hard drives
#   column7: 2nd hard drive size(if two drives)
#   column8: computer OS
#   column9: computer year

#START BASE PROGRAM--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#initialize variables for later use
records = 0

#import csv to read files
import csv


#LISTS -- first we need to prep some empty lists so the processer doesn't see one and think its a variable

brand = [] #brand is now an empty list
type = []
cpu = []
ram = []
first_disk = []
num_disk = []
second_disk = []
os = []
year = []



#print column names
#print("{0:8} {1:8} {2:4} {3:4}  {4:8}  {5:8} {6:8}   {7:8} {8:8}".format("Type", "Brand", "CPU", "RAM", "1st Disk", "Num HDD", "2nd Disk", "OS", "YR"))

#WHEN IN CLASS:
with open ("C:/Users/008006221/OneDrive - New England Institute of Technology/New England Tech/Term 2/SE 126/Lab Files/lab2b.csv") as lab2b:

#ON MY LAPTOP:
#with open ("C:/Users/thewi/OneDrive - New England Institute of Technology/New England Tech/Term 2/SE 126/Lab Files/lab2b.csv") as lab2b: #using different variable name for the hell of it
    comp_list = csv.reader(lab2b)

    #for loop
    for rec in comp_list:
        records += 1


        #column 1 - laptop or desktop
        if rec[0] == "D":
            column1 = "Desktop"

        elif rec[0]:
            column1 = "Laptop"

        type.append(column1) #<--- append column1 value into the type list
                             #IF WE HADN'T CREATED VARIABLES for each field
                             #type.append(rec[0])



        #column 2 - Brand
        if rec[1] == "DL":
            column2 = "Dell"

        elif rec[1] == "HP":
            column2 = "HP"

        elif rec[1] == "GW":
            column2 = "Gateway"


        brand.append(column2)

        

        #column 3 - CPU - Will print as is
        column3 = rec[2]

        cpu.append(column3)

        #column 4 - RAM - add formatting to make 2 digits when printed to screen
        column4 = int(rec[3])

        ram.append(column4)

        #column 5 - 1st disk size - will print as is
        column5 = rec[4]

        first_disk.append(column5)

        #column 6 - # of hard drives - will print as is
        column6 = rec[5]

        num_disk.append(column6)

        #************************************************EVERYTHING FROM HERE ON DEPENDS ON # OF HARD DRIVES**********************************************************************************

        #ONE DISK DRIVE
        
        if column6 == "1":
            
            #column 7 - Empty Space
            column7 = ""

            #column 8 - operating system
            column8 = rec[6]

            #column 9 - year - will print as is
            column9 = rec[7]


        #TWO DISK DRIVES

        #column 7 - 2nd disk size (if 2nd disk is there)
        elif column6 == "2":
            column7 = rec[6]
            
            #column 8 - operating system
            column8 = rec[7]
        
            #column 9 - year - will print as is
            column9 = rec[8]


        second_disk.append(column7)
        os.append(column8)
        year.append(column9)
        
        #output information:
        #print("{0:8} {1:8} {2:4} {3:2} \t{4:8} {5:8} {6:8} {7:8} {8:8}".format(column1, column2, column3, column4, column5, column6, column8, column8, column9))
#close file

print()
print()
print("{0} Computers in File".format(records))
print()
print()

#AFTER EXITING the FILE HANDLING AREA
#we no longer need to be accessing the file because all of the file data is stored in lists

#process the list data
#list processing = FOR LOOP
print("         {0:8} {1:8} {2:4} {3:4}  {4:8}  {5:8} {6:8}   {7:8} {8:8}".format("Type", "Brand", "CPU", "RAM", "1st Disk", "Num HDD", "2nd Disk", "OS", "YR"))
for index in range(records):

    #print("INDEX: {0} \t {1}".format(index, brand[index]))
    print("INDEX:{9:3} {0:8} {1:8} {2:4} {3:2} \t{4:8} {5:8} {6:8} {7:8} {8:8}".format(type[index], brand[index], cpu[index], ram[index], first_disk[index], num_disk[index], second_disk[index], os[index], year[index], index))