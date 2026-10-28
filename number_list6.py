def find_number(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1

##examples
print(find_number([10, 25, 30, 45],30 ))
print(find_number([5, 8, 5, 9],5 ))
print(find_number([10, 20, 30],99 ))

