# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
# Examples
#"()"              =>  true
#")(()))"          =>  false
#"("               =>  false
#"(())((()())())"  =>  true

def valid_parentheses(string):
    counter = 0
    for char in string:
        if -1 < counter:
            if char == "(":
                counter += 1
            elif char == ")":
                counter -= 1
        else:
            return False
            break
    return counter == 0