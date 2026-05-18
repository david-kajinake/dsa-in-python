"""
HashMap is a widely used data structure that stores data in key-value pairs,
allowing for efficient insertion, removal, and lookup, typically in (O(1)) average time.
"""

"""
Given a list of items , calculate how many times each item appears in that list
"""

#Example: a list of fruits
data = [ 
"banana", "lemon", "orange", "guava" , "apple", "lemon", "orange", "avocado", "lime", "passion" ,"guava"  
       ]

def check_item_count( data_list: list ) -> dict:
    """
    Define a hash table.
    Loop through all items in the list. for each item, if it doesn't exist in the hash table , insert with its times of occurence. 
    if ti exists update it exists update its times of occurence.
    """
    items_map = {}
    for item in data_list:
        if item not in items_map:
            items_map[item] = 1
        else:
            items_map[item] += 1

    return items_map


#Test it 
print( check_item_count( data_list= data ) )

#OUTPUT: {'banana': 1, 'lemon': 2, 'orange': 2, 'guava': 2, 'apple': 1, 'avocado': 1, 'lime': 1, 'passion': 1}