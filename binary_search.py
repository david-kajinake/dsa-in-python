numbers = [10, 12, 15, 18, 20, 22, 25]
target = 18

"""
We take the container / list and divide it into a half and go straight to the middle index( value ).
if we find the target we simply return its index.
if the middle is higher than the target we let go of the right side from the middle ,  and divide the left side into a half and search fro there.
if the middle is lower than the target , we let go of the left side from the middle , and divide the right side into half and search from there.
if , at the end of the loop , no match is found , we return None  
"""

def binary_search(iterable):
    low = 0
    high = len(iterable) - 1
    while low <= high: #The loop runs as long as low avlue is less than or equals high value
        middle_number = ( low + high ) // 2 #Divide the list into half
        guessed = iterable[middle_number]
        if guessed == target: 
            return middle_number
        elif guessed > target:
            high = middle_number - 1 #Throw away the right side
        else:
            low = middle_number + 1 #Throw away the left side
    return None
print( binary_search(numbers) )


#EXAMPLE2:
#Find the target's index in a list of 10000 ( Ten thousands ) numbers
number_list = list(range(0,10000))
#number_list = [ 0,1,2,3,..10...20...50...100..1000..1500..2000..5000..9000..10000 ]
#If it is not sorted , you sort first in ascending order
target = 750

def binary_search_two(iterable):
    low = 0
    high = len(iterable) - 1
    while low <= high:
        middle_index = ( low + high ) // 2
        number_at_the_middle = iterable[middle_index]
        if number_at_the_middle == target:
            return middle_index
        elif number_at_the_middle > target:
            high = middle_index + 1
        elif number_at_the_middle < target:
            low = middle_index - 1  
    return None
print(binary_search_two(number_list))