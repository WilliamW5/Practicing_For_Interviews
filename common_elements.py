def common_elements(a1, a2):
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] == a2[p2]:
            result.append(a1[p1])
            p1 += 1
            p2 += 2
        elif a1[p1] < a2[p2]:
            p1 += 1
        else:
            p2 += 1
    return result
    a1.le

a1= [1, 3, 4, 6, 7, 9, 12]
a2= [1, 2, 4, 5, 9, 10, 11, 11, 12]
print(common_elements(a1, a2))