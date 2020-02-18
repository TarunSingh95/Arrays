'''
Takes an array as an inout and gives the highest continuous sum
'''

def largest_cont_sum(arr):
    
    if len(arr) == 0:
        return 0
    
    current_sum = max_sum = arr[0]
    
    for number in arr:
        current_sum = max( current_sum + number , number )
        max_sum = max( current_sum , max_sum )
    
    return max_sum

print("Largest Continuous Sum is " + str(largest_cont_sum([1,2,-1,3,4,5,-10,10,-5,5])))
