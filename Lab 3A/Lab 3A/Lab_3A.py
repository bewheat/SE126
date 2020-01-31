#Desiree Davis
#Lab 3A
#SE 126.22
#1/21/20


#PROMPT: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2B) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.


#Variable Dictionary
#   records: number of records processed(I don't think I even actually used this variable in this program
#   replace_desk: # of desktops that need to be replaced
#   replace_lap: # of laptops that need to be replaced
#   file: file being read
#   desktop_cost: cost of replacing older desktops
#   laptop_cost: price of replacing older laptops

#LIST Dictionary
#   type: type of computer being processed (Desktop or Laptop)
#   brand: computer brand(dell,HP, Gateway)
#   cpu: computer CPU
#   ram: computers ram
#   first_disk: size of 1st/only hard drive
#   num_disk: number of hard drives
#   second_disk: size of 2nd disk(where there is one)
#   os: computer os
#   year: year computer was made


#Start Base Program

#Initialize variable to keep track of records
records = 0
#other variables
replace_desk = 0
replace_lap = 0


#initialize lists to store file data
type = []
brand = []
cpu = []
ram = []
first_disk = []
num_disk = []
second_disk = []
os = []
year = []

#open file
import csv

#WHEN USING MY LAPTOP
#with open("C:/Users/thewi/OneDrive - New England Institute of Technology/New England Tech/Term 2/SE 126/Lab Files/lab2b.csv") as csvfile:

#WHEN IN CLASS
with open("C:/Users/008006221/OneDrive - New England Institute of Technology/New England Tech/Term 2/SE 126/Lab Files/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        #store data in lists
        type.append(rec[0])
        brand.append(rec[1])
        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_disk.append(rec[5])

        #the rest of the data is relevent to # of hard drives in computer
        
        #IF ONE HARD DRIVE
        if int(rec[5]) == 1:
            second_disk.append("N/A")
            os.append(rec[6])
            year.append(rec[7])

        #IF TWO HARD DRIVES
        elif int(rec[5]) == 2:
            second_disk.append(rec[6])
            os.append(rec[7])
            year.append(rec[8])

#CLOSE FILE



#print processed files
print("         {0:8} {1:8} {2:4} {3:4}  {4:8}  {5:8} {6:8}   {7:8} {8:8}".format("Type", "Brand", "CPU", "RAM", "1st Disk", "Num HDD", "2nd Disk", "OS", "YR"))

for index in range(records):

    #print("INDEX: {0} \t {1}".format(index, brand[index]))
    print("INDEX:{9:3} {0:8} {1:8} {2:4} {3:2} \t{4:8} {5:8} {6:8} {7:8} {8:8}".format(type[index], brand[index], cpu[index], ram[index], first_disk[index], num_disk[index], second_disk[index], os[index], year[index], index))

print()
print()

#I know I could do it in the same for loop but for the sake of actually keeping track of what i'm doing:
#loop through list to determine how many laptops/desktops need to be replaced
for i in range(records):
    if type[i] == "D" and int(year[i]) <= 16:
        replace_desk += 1

    elif type[i] == "L" and int(year[i]) <= 16:
        replace_lap += 1
#end for Loop

desktop_cost = replace_desk * 2000
laptop_cost = replace_lap * 1500

print("{0} Desktops need to be replaced. It will cost ${1:5.2f}".format(replace_desk, desktop_cost))
print("{0} Laptops need to be replaced. It will cost ${1:5.2f}".format(replace_lap, laptop_cost))
