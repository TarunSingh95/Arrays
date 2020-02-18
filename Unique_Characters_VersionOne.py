'''
return False if characters in a string are not unique and True if unique 
'''

def unique_chars(s):
    
    my_set = set()
    
    for letters in s:
        if letters in my_set:
            return False
        else:
            my_set.add(letters)
        
    return True

print("Is the string unique " + unique_chars("abcdef"))
