"""
Sort a list manually. ( Bubble sort )
"""

my_list = [ 4 , 6 , 8 , 10 , 2 , 9 , 7 , 3 , 12 , 1 , 5 ]

def manual_sort( numbers_list ):
    """
    COMPARE: check the first item and the second item.

    SWAP: If the left item is larger than the right item, swap their positions. If it's smaller, leave them alone.

    MOVE RIGHT: step one position to the right and compare the next pair (the second and third items).

    REPEAT: keep doing this until you reach the end of the list. By the end of this first full "pass," the absolute largest number will have "bubbled" up to the very last position.

    START OVER: start from the beginning again, repeating the process until you can make a full pass through the list without swapping anything. When no swaps are needed, the list is completely sorted.
    """
    n = len( numbers_list ) #Get the length of list items

    for i in range( n ):
        swapped = False
        for j in range( n - i - 1 ):
            if numbers_list[ j ] > numbers_list[ j + 1 ]: #Compare two adjacent elements at a time
                numbers_list[ j ] , numbers_list[ j + 1 ] = numbers_list[ j + 1 ] , numbers_list[ j ] #If the left is bigger than the right , swap them
                swapped = True
        if not swapped:
            break
    return numbers_list 

#print( manual_sort(my_list) )
 