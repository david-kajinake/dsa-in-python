import time 
"""
Find two indices , in a list ,  whose values can be added up to get the target
"""
num_list = [ 2 , 8 , 10 , 15  , 7 , 13 , 11 , 4  ]
target = 15

#Return all pairs that can be summed up to get the target

#Approach 1
def two_sum_one( num_list , target ):
    num_list.sort()
    pairs_found = []
    for i in range(len(num_list)-1) :
        the_other_number = target - num_list[i]
        if the_other_number in num_list:
            pairs_found.append(( num_list[i] , the_other_number ))
        else:
            continue
    return pairs_found or None
print(two_sum_one( num_list=num_list , target=target ))

