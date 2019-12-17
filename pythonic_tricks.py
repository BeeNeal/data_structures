from math import floor, ceil



def count_by(arr, fn=lambda x: x):
    """Counts elements in array by whatever function given."""

    key = {}
    for el in map(fn, arr):
        key[el] = 0 if el not in key else key[el]
        key[el] += 1
    return key

def word_score(word):
    score = 0
    for char in word:
        score += ord(char)
    return score

def alt_word_score(word):
    return sum([ord(c) for c in word])


print(count_by([8.1, 8.4, 9.0, 5.2, 5, 6, 8.2], floor))
print(count_by(['one', 'two', 'three', 'four'], len))
print(count_by(['abba', 'baba', 'bobo', 'bbaa'], word_score))
# demonstrates lambda, and passing function into function

for word in ['brittany', 'neal', 'omar', 'shishani']:
    print(len(word))



def chunk(lst, size):
    """Take in list and return a list of lists of specified size."""

    # math.ceil rounds up to greatest integer value (-13.1 -> -13, 103.4 -> 104)
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))


def find_substring(test_str, sub):
    res = [i for i in range(len(test_str)) if test_str.startswith(sub, i)]
    return res

print(find_substring('omarshishaniisinthissstringomarishere omar is here', 'omar'))
