numbers_list = [5, 6, 0, 1, 2, 4, 3, 9, 8, 7]

for j in range(0, 10):
    flag = False
    for a in range(0, 9):
        if numbers_list[a] > numbers_list[a + 1]:
            swap = numbers_list[a]
            numbers_list[a] = numbers_list[a + 1]
            numbers_list[a + 1] = swap
            flag = True
    if flag == False:
        break

print(numbers_list)