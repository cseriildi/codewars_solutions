# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. The string can contain any char.

def xo(s):
    string = s.lower()
    count = 0
    for char in string:
        if char == "x":
            count += 1
        elif char == "o":
            count -= 1
            
    if count == 0:
        return True
    else:
        return False