# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case


def is_isogram(string):
    i = 1
    str = string.lower()
    result = True
    
    if str != "":
        for char in str:
            if char not in str[i:]:
                i += 1
            else:
                result = False
    return result