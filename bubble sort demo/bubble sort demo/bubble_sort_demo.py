#Week 8 Day 1 - bubble sort demo



#binary search can only be performed on ORDERED LISTS
#lists can be ordered numberically or alphabetically; increasing or decreasing


#FUNCTIONS---------------------------------

def swap(listName, index):

    #this function handles the swapping of values for bubble sort
    temp_var = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp_var

    #procesor has acces to the new sorted list so we do not need to return specific list value -- it is already updated and we can access in main/base program

#BASE PROGRAM------------------------------


#populate lists
name = ["Mary", "Cathy", "Tom", "Whitney", "Adam", "Sam", "Betty", "Ed"]
age = [21, 33, 24, 28, 30, 31, 40, 68]

records = len(name) #len() returns length of list

print("BEFORE SORTING-----------------------------")
for i in range(records):

    print("INDEX: {0} \t {1:10} \t {2}".format(i, name[i], age[i]))


#BUBBLE SORT-----------------------------------------------
for i in range(records - 1):#outer loop
    
    print("OUTTER LOOP! i = ", i)

    for k in range(records - 1): #inner loop

        print("\tINNER! k =", k)


        #if statement determines the sort
        #list used is the list being sorted
        #> is for increasing order, < is for decreasing order

        if name[k] > name[k + 1]:
            #first list value is greater tan second list value; if putting in increasing order, they need to SWAP places
            print("\t\tSWAP! ", name[k], "<----->", name[k + 1])

            #swap the values

            #temp = name[k] #save name1
            #name[k] = name[k + 1] #replace name1 w/ name2
            #name[k + 1] = temp #replace name2 w/ name1

            swap(name, k)

            #swap the remaining values of the full record
            #this keeps original data together -- stuff that belongs together
            #temp = age[k]
            #age[k] = age[k + 1]
            #age[k + 1] = temp

            swap(age, k)


        #end if statement
    #end inner loop
#end outer loop

print("End of bubble soring \n\n\n")

print("AFTER SORTING; ORDERED ALPHABETICALLY:")


for i in range(records):

    print("INDEX: {0} \t {1:10} \t {2}".format(i, name[i], age[i]))
#end for loop


#now that the NAMES are in increasing order, you could run a binary search for a NAME