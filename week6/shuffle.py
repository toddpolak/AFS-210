import random

def myShuffle(nlist):
    
    # Time Complexity of this Algorithm: O(1) - Constant Time
    
    list_length = len(nlist)
    
    # pop off the first number and append it to the end of the list
    first_number = nlist.pop(0)
    nlist.append(first_number)
    
    # pop off the middle number and append it to the end of the list
    mid_point = list_length // 2
    mid_number = nlist.pop(mid_point)
    nlist.append(mid_number)
    
    # generate a random number based on the size of the list
    random_num = random.randint(0, list_length - 1)
    
    # pop off that random element and append to the end of the list
    list_element = nlist.pop(random_num)
    nlist.append(list_element)
    
    return nlist

myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

print('\nBefore Shuffle:\n')
print(myList)
print('\nShuffled:\n')
print(myShuffle(myList))
print(myShuffle(myList))
print(myShuffle(myList))
print(myShuffle(myList))
print(myShuffle(myList))
print('\n')