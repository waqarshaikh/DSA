# Does this code has time complexity of Big O(n) ?

array = [0, 1, 2, 0, 0, 2, 2, 2 , 2, 2, 0, 0, 0]
zeros = ones = 0

for num in array:
    if num == 0:
        zeros += 1
    if num == 1:
        ones += 1

for i in range(len(array)):
    if i < zeros:
        array[i] = 0
    elif i < zeros + ones:
        array[i] = 1
    else:
        array[i] = 2
