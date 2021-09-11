def is_one_away_same_length(s1, s2):
    count_diff = 0
    for i in range(len(s1)-1):
        if s1[i] != s2[i]:
            count_diff += 1
            if count_diff > 1:
                return False
    return True

def is_one_away_diff_length(s1, s2):
    i = 0
    count_diff = 0
    while i < len(s2):
        # Looks 0 to 1 char ahead if char is different
        if s1[i + count_diff] == s2[i]:
            i += 1
        else:
            count_diff += 1
            if count_diff > 1:
                return False
    return True

def is_one_away(s1, s2):
    # If the list is 2 or more elements larger, return false
    if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:
        return False
    # If same length, checks how many char are different
    elif len(s1) == len(s2):
        return is_one_away_same_length(s1, s2)
    # If s1 is larger (by 1)
    elif len(s1) > len(s2):
        return is_one_away_diff_length(s1, s2)
    # If s2 is larger (by 1)
    else:
        return is_one_away_diff_length(s2, s1)

s1 = "abcde"
s2 = "abfde"
print(is_one_away(s1, s2))