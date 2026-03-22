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