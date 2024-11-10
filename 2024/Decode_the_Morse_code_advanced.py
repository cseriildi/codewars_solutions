# Decode the Morse code, advanced
# https://www.codewars.com/kata/54b72c16cd7f5154e9000457
# Difficulty: 4 kyu

from preloaded import MORSE_CODE #provided by Codewars but I also created the dictionary in preloaded.py

def get_rate_for(separator, bits):
    chunks = set(filter(None, bits.split(separator)))

    return 0 if len(chunks) == 0 else min([len(i) for i in chunks])

def get_rate(bits):
    zeros = get_rate_for('1', bits)
    ones = get_rate_for('0', bits)

    return min(zeros, ones) if zeros and ones else max(1, zeros, ones)
    
def decode_bits(bits):
    bits = bits.strip("0")
    rate = get_rate(bits)
    
    DASH = "111" * rate
    DOT = "1" * rate
    SPACE = "0" * rate
    
    return bits.replace(DASH , '-').replace(DOT, '.').replace(SPACE, ' ')

def decode_word(word):
    LETTER_SEPARATOR = " " * 3
    return ''.join([MORSE_CODE[letter.replace(" ", "")] for letter in word.split(LETTER_SEPARATOR)])

def decode_morse(morseCode):
    WORD_SEPARATOR = " " * 7
    word_list = morseCode.split(WORD_SEPARATOR)
                   
    return ' '.join([decode_word(word) for word in word_list])