#  Filter list — Return a list containing only even numbers using list comprehension.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_nums = [num for num in nums if num % 2 == 0]
square = [num * num for num in nums]

print(even_nums)
print(square)