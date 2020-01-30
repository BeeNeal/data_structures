# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from itertools import combinations
def letter_phone_num_combos(num):
    """ """

    nums_to_letters = {
        '1':[],
        '2':['a','b','c'],
        '3':['d','e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j','k', 'l'],
        '6': ['m','n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9':['w', 'x', 'y', 'z']
    }
    combo_array = []
    for item in num:
        for c in nums_to_letters[item]:
            
            combo_array.append()
print(letter_phone_num_combos('23'))