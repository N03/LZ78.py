# LZ78 implementation
# Université de Fribourg, Suisse
# AUTHOR: Noé Zufferey - noe.zufferey@gmail.com
# CREATION: april 2018 
# USAGE: python3 LZ78.py '<string to encode>'

import sys

def compress(data):
    comp_data = []
    dictionnary = ['']
    word = ''
    i = 0
    for char in data:
        i += 1
        word += char
        if not word in dictionnary:
            dictionnary.append(word)
            comp_data.append([dictionnary.index(word[:-1]), word[-1]])
            word = ''
        elif i == len(data):
            comp_data.append([dictionnary.index(word), ''])
            word = ''
    return comp_data

def add_zeros(code, nbr):
    pre = ''
    i = 0
    while i < nbr - len(code):
        pre += '0'
        i += 1
    return pre + code

def to_bits(data, h=False):
    len_ind = 1
    result = ''
    for word in data:
      pre = add_zeros(bin(word[0])[2:], len_ind)
      result += pre
      len_ind = len(pre)
      if h : result += ','
      next_char = add_zeros(bin(ord(word[1]))[2:], 8)
      result += next_char
      if h : result += '|'
    return result

if __name__ == '__main__':
    data =sys.argv[1]
    comp_data = compress(data)
    print(comp_data)
    print(to_bits(comp_data, True))
    print(to_bits(comp_data))