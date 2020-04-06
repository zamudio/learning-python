def evens_sum(num):
    total = 0
    for number in num:
        if number % 2 == 0:
            total += number
    return total


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(evens_sum(nums))
