def move_zeros(numbers):
    insert_pos = 0


    for num in numbers:
        if num != 0:
            numbers[insert_pos] = num
            insert_pos += 1


    while insert_pos < len(numbers):
        numbers[insert_pos] = 0
        insert_pos += 1


numbers1 = [0, 1, 0, 3, 12]
move_zeros(numbers1)
print(numbers1)


numbers2 = [4, 0, 5, 0, 2]
move_zeros(numbers2)
print(numbers2)


numbers3 = [1, 2, 3]
move_zeros(numbers3)
print(numbers3)


numbers4 = [0, 0, 0]
move_zeros(numbers4)
print(numbers4)


