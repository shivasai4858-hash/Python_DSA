
def group_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    return list(anagram_groups.values())
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )



"""def anagram(s,t):
    d = {}
    e = "".join(sorted(s))
    d[e] = True
    a = "".join(sorted(t))
    if a in d:
        return d[e]
    else:
        return False
    
print(anagram("abc","cbaew"))
"""


  