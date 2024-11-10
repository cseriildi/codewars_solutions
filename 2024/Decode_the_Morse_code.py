# Decode the Morse code
# https://www.codewars.com/kata/54b724efac3d5402db00065e
# Difficulty: 6 kyu

from preloaded import MORSE_CODE #provided by Codewars but I also created the dictionary in preloaded.py

def decode_word(word):
    return ''.join([MORSE_CODE[letter] for letter in word.split(' ')])

def decode_morse(morse_code):
    word_list = morse_code.strip().split("   ")
                   
    return ' '.join([decode_word(word) for word in word_list])