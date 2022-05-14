#You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.


def get_middle(s):
    middle = ""
    mid = len(s) // 2
    if len(s) % 2 == 0:
        middle = s[mid - 1 : mid + 1]
    else:
        middle = s[mid]
    return middle