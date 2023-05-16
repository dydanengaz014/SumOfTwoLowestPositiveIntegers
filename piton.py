def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]

#Example

numbers_1 = [19, 5, 42, 2, 77]
result_1 = sum_two_smallest_numbers(numbers_1)
print(result_1)  # Output: 7
