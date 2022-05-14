#This time no story, no theory. The examples below show you how to write function accum:
#Examples:
#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    result = s[0]
    result = result.upper()
    counter = 0
    for letter in s:
        result += '-' + letter.upper() + (letter.lower() * counter)
        counter += 1
    return result[2:]