'''
FINDING THE MISSING ELEMENT IN ARRAY
CONDITION: ARR2 LENGTH SHOULD BE ONE LESS THAN ARR1
'''
def missing(arr1, arr2):
    arr1= sorted(arr1)
    arr2= sorted(arr2)
    print(str(arr2))

    for num1, num2 in zip(arr1, arr2):
        if num1!=num2:
            return num1;
    return arr1[-1]

def missingTwo(arr1, arr2):

    arr1= sorted(arr1)
    arr2= sorted(arr2)
    print(arr1)
    print(arr2)

    my_dict= {}

    for num in arr2:
        if num in my_dict:
            my_dict[num] +=1
        else:
            my_dict[num] = 1
    print(my_dict)

    for num in arr1:
        if num in my_dict:
            my_dict[num] -=1
        else:
            my_dict[num] = 1
    print(my_dict)

    for k in my_dict:
        if my_dict[k] != 0:
            return k

print(missing([1,2,3,4,5],[1,3,4,2]))
print(missingTwo([1,4,3,2,5,6],[1,2,3,4,5]))
