# binary search on a sorted list
def binary_search(list, term):
    
        size_of_list = len(list) - 1 

        index_of_first_element = 0 
        index_of_last_element = size_of_list 
    
        return False

list1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list2 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(binary_search(list1, 31))
print(binary_search(list1, 77))
print(binary_search(list2, "Delta"))