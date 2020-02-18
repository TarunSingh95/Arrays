'''
Takes a String and Compresses it
Eg: i/p -> AAABCCaaa
    o/p -> A3B1C2a3
'''

def compress(s):
    
    length = len(s)
    
    if length == 0:
        return 0
        
    if length == 1:
        return s+"1"
        
    r = ''
    count = i = 1
    
    while i < length:
        
        if s[i] == s[i-1]:
            count +=1
        else:
            r = r + s[i-1] + count
            count = 1
        i +=1
    
    r = r + s[i-1] + count
    return r
    
print("Compressed " + compress("AAABCCaaa"))
