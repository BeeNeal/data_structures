# https://leetcode.com/problems/goat-latin/

def goatlatin(s):
    """ """

    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E',' I', 'O', 'U'])

    words = s.split()
    goatlatin_version = []
    counter = 1
    for word in words:
        if word[0] in vowels:
            goatlatin_version.append(word + 'ma' + 'a' * counter)
        else:
            goatlatin_version.append(word[1:] + word[0] + 'ma' + 'a' * counter)
        counter += 1
    return " ".join(goatlatin_version)
print(goatlatin("I speak Goat Latin"))