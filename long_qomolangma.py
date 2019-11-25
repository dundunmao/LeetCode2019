def qomolangma(array):
    start = 0
    res = 1
    for i in range(len(array)):
        if array[i] < array[start]:
            res = max(res, i - start + 1)
            start = i
    if start == len(array) - 1:
        return res
    new_start = len(array) - 1
    for j in range(len(array) - 1, start - 1, -1):
        if array[j] < array[new_start]:
            res = max(res, new_start - j + 1)
            new_start = j
    return res

array = [3,7,4,9,2,1,13] # 5
print(qomolangma(array))
array = [1, 99, 104, 400, 22, 15, 33]
print(qomolangma(array)) # 6
array = [1]
print(qomolangma(array)) # 1
array = [1, 2]
print(qomolangma(array)) # 2
array = [1, 2, 3, 4, 5, 6, 7]
print(qomolangma(array)) # 2

