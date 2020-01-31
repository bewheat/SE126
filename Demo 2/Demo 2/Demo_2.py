#Week 2 Day 1: Importing Data from a file

#YOU MUST IMPORT THE CSV LIBRARY IN ORDER FOR FILES TO BE ACCESSED


#CSV: Comma Seperated Values
#RECORDS: rows of the file, different types of data all belonging together
#FIELDS: columns of the files, sets of data (all data in a column is the same "type" ie: names, ages, salaries, email addresses, etc)

#BASE CODE-----------------------------------------------------------------


import csv #import csv library so we can read file

total_records = 0 #you should ALWAYS have a total records var for your first few attempts at file reading

total_salary = 0 #holds all salaries in file for total print at end

#print header:
print("{0:} \t {1} \t {2}".format("NAME", "AGE", "SALARY"))


#right-click the text/csv file in folder view ->. "properties to find the file location( no shit sherlock)

#flip all '\' to '/'

with open("C:/Users/008006221/Documents/SE126/example.csv") as csvfile:
    #notice : everything must be indented until we're ready to close the file


    file = csv.reader(csvfile)
    #now the file we have connected is known in the program as file
    #file has seeral records, each record has several fields

    for rec in file:

        total_records += 1

        #print(rec) #print entire record of file


        #print only the names in the file
        #print("RECORD #:{0} \t {1} \t ${2}".format(total_records, rec[0], rec[2]))


        #add all salaries to total_salary
        total_salary += float(rec[2])

        
        print("{0} \t {1} \t ${2:.2f}".format(rec[0], rec[1], float(rec[2])))
        #add field width to ensure columns stay aligned FOR FUCKS SAKE DON'T FORGET



print("Total Records", total_records)
print("Total Salary: ${0:.2f}".format(total_salary))