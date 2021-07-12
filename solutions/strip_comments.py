# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
# Any whitespace at the end of the line should also be stripped out.

def solution(string,markers):
    result = ""
    iscomment = False
    for letter in string:
        if string[string.index(letter):string.index(letter)+1] == '\n':
            iscomment = False
        if letter in markers:
            iscomment = True
            result = result.strip(" ")
        if not iscomment:
            result += letter
    return result
