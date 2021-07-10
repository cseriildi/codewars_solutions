# Complete the solution so that it reverses the string passed into it.


def solution(string):
    reverse = ""
    for char in string:
        reverse = char + reverse
    return reverse