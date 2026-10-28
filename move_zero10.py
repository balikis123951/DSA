def move_zeros(numbers):
    result = []
    zero_count = 0

    for num in numbers:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)

    result.extend([0]*zero_count)
    return result

##example
print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 5]))
