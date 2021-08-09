Data1 = (7, False, "Apple", True, 7, 98.6) #Tuple
Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"} #Set
Data3 = ["A", 7, -1, 3.14, True, 7] #List
Data4 = {"name" : "Joe",  "age" : 26,   "active" : True,  "hourly_wage" : 14.75} #Dictionary

#Dataset 1 (Tuple) -----------------------

print(len(Data1)) #Count the number of items

print(Data1[3]) #Find the value of the fourth item stored in the data set

print(Data1.count(7)) #Count the number of times 7 appears

#Dataset 2 (Set) -----------------------

Data2.pop() #Remove a random element from the data set

Data2.add("Alpha") #Add "Alpha" to the data set

print(Data2) #Print data set

#Dataset 3 (List) -----------------------

Data3.reverse() #Dataset in reverse order

Data3[1]='B' #Change the second value in the data set to ‘B’

Data3.pop() #Remove the last item

print(Data3) # Print the data set

#Dataset 4 (Dictionary) -----------------------

Data4['active']=False #Change "active" to False

Data4['address']='123 West Main Street' #Add "address" with a value of "123 West Main Street"

print(Data4['hourly_wage'] * 40) #Print the weekly salary for Joe if he worked a full 40 hour week.

print(Data4) #Print the data set