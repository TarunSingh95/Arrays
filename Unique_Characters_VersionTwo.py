def unique_chars(s):

    return len( set(s) )  ==  len( s )
    
print("Is the string Unique " + unique_chars("abcdea"))
