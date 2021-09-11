def is_rotation(a1, a2):
    if len(a1) != len(a2): return False
    key = a1[0]
    key_i = -1

    for i in range((len(a2)-1)):
        if a2[i] == key:
            key_i = i
            break
    if key_i == -1:
        return False
    for i in range((len(a1) - 1)):
        j = (key_i + i) % len(a1) # Gets the corrisponding index of B using modulus
        if a1[i] != a2[j]:
            return False
    return True

a1 = [1, 2, 3, 4, 5, 6, 7]
a2 = [4, 5, 6, 7, 1, 2, 3]
print(is_rotation(a1, a2))