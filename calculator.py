#  Simple function — Create a function that takes a list and returns the sum, average and count of numbers.

def calculate(nums):
    total = sum(nums)
    count = len(nums)

    if count == 0:
        return 0, 0, 0

    average = total / count

    return total, average, count


numbers = [10, 20, 30, 40, 50]

total, average, count = calculate(numbers)

print("Sum:", total)
print("Average:", average)
print("Count:", count)