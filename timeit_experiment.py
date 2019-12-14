import timeit

def word_score_timeit():
    score = 0
    for char in 'word':
        score += ord(char)
    return score

def alt_word_score_timeit():
    return sum([ord(c) for c in 'word'])

import timeit
print(timeit.timeit(word_score_timeit, number=10000))
print(timeit.timeit(alt_word_score_timeit, number=10000))
# 0.003350863989908248 shows version w/o list comp is faster
# 0.0053685419843532145

print(timeit.timeit('sum([ord(c) for c in "word"])', number=10000))
# 0.004525886004557833 timeit evaluates it quicker w/ string stmt than func call

