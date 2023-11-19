#this is a simple question where we give some list as a parameter; it will calculate the distance of the first two terms, then the third and fourth terms, and so on, and then sum them all.
#if there is an odd number of elements in the list, then we need to sum up the even number and multiply it by the last term.

def distance_sum(lst):
    n = len(lst) 
    if n % 2 == 1:
        last_element = lst[-1]
        n -= 1
    else:
        last_element = 1
    
    distance_sum = 0
    for i in range(0, n, 2):
        distance_sum += abs(lst[i] - lst[i + 1])
    
    result = distance_sum * last_element
    return result
print(distance_sum(lst))
