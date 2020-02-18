'''
Reverses the words in a sentence and prints
Eg: i/p -> "Hello World"
    o/p -> "World Hello"
'''

def reverse_sentence(s):

    words = []
    spaces = [" "]
    length = len(s)
    
    i = 0
    
    while i < length:
        
        if s[i] not in spaces:
            word_start = i
         
        while i < length and s[i] not in spaces:
            i +=1
            
        words.append(s[ word_start:i ])
        i +=1
        
    return " ".join(reversed(words))
    
print("Reversed Sentence " + reverse_sentence("Hello World"))


        
