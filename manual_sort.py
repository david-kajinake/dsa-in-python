"""
Sort a list manually. ( Bubble sort )
"""

my_list = [ 4 , 6 , 8 , 10 , 2 , 9 , 7 , 3 , 12 , 1 , 5 ]

def manual_sort( numbers_list ):
    n = len( numbers_list ) #Get the length of list items
    number_of_runs = 0
    for i in range( n ):
        swapped = False
        for j in range( n - i - 1 ):
            number_of_runs += 1
            if numbers_list[ j ] > numbers_list[ j + 1 ]:
                numbers_list[ j ] , numbers_list[ j + 1 ] = numbers_list[ j + 1 ] , numbers_list[ j ]
                swapped = True
        if not swapped:
            break
    return [ numbers_list , number_of_runs ]

print(manual_sort( my_list )[0])
print(manual_sort(my_list)[1])
        

 