def non_repeating(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None


print(non_repeating("aabcb")) # -> c
print(non_repeating("xxyz")) # -> y
print(non_repeating("aabb")) # -> null
