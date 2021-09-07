def mergeSort(nlist):
    
    # insert your code to complete the mergeSort function
    
    # initial split:
    print("Splitting ", nlist)
    list_length = len(nlist)
    mid_point = list_length // 2
    left_half = nlist[:mid_point]
    
    while len(left_half) != 1:
    
        # split the left side?:
        print("Splitting ", left_half)
        list_length = len(left_half)
        mid_point = list_length // 2
        left_half = nlist[:mid_point]
    

    #right_half = nlist[mid_point:]
    
    #print("Merging ", nlist)
    
    #print(merge(nlist, left_half, right_half))

def merge(nlist, lefthalf, righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

myList = [55, 31, 26 ,20 ,63 ,7 ,51 ,74 ,81 ,40]

#print('myList: ', myList)

mergeSort(myList)