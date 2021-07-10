# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    result = "#"
    listofwords =[]
    if 0<len(s)<141:
        listofwords = s.split(" ")
        for word in listofwords:
            result += word.capitalize()
    else:
        result = False
    return result