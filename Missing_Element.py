'''
Missing Element from an Array
Eg: input -> arr1 = [1,2,3,4] & arr2 = [1,2,4]
    output -> missing element is 4
'''

def missing_element(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    
    my_dict = {}
    
    for num in arr2:
        if num in my_dict:
            my_dict[num] += 1
        else:
            my_dict[num] = 1
    
    for num in arr1:
        if num in my_dict:
            my_dict[num] -= 1
        else:
            my_dict[num] = 1
       
    for num in my_dict:
        if my_dict[num] != 0:
            return num
            
    return arr1[-1]
    
print("The missing element is " + str(missing_element([2,1,3,4,6,5] , [2,3,4,6,5])))
