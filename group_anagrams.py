# https://leetcode.com/problems/group-anagrams/
# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

def group_anagrams(words):
    """Given an array of strings, output a list of grouped anagrams."""

    groups = {}
    for item in words:
        ordered_word = ''.join(sorted(item))
        if ordered_word in groups:
            groups[ordered_word] += [item]
        else:
            groups[ordered_word] = [item]
    return groups.values()

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# lessons learned:
# CAN sort strings

