
def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop1rec(i, odd_sum):
    print('function call')
    if i >= 20:
        return odd_sum
    elif (i % 2) == 1:
        odd_sum += i
    return loop1rec(i+1,odd_sum)

print(loop1())
i=0
odd_sum=0
print(loop1rec(i,odd_sum))

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

#def loop1Rec(num,odd_sum):
    # Duplicate the loop1 function using recursion

    

#def loop2Rec(num,even_sum):
    # Duplicate the loop2 function using recursion
