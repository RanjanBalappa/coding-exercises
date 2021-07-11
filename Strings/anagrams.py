#Anagrams
# Two strings are said to be anagrams of one another if you can turn the
# first string into the second by rearranging its letters.
# For example, "table" and "bleat" are anagrams, as are "tear" and "rate."
# Your job is to write a function that takes in two strings as input and
# determines whether they're anagrams of one another.

# Solution should run in O(n1 + n2)


def anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    char_dict = {}
    for s1 in str1:
        char_dict[s] = char_dict(s, 0) + 1

    for s2 in str2:
        if s2 not in str1 or char_dict[s2] <= 0:
            return False

        char_dict[s] -= 1

    return True