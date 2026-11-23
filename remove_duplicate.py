# Remove duplicates — Remove duplicate elements from a list while preserving order.

def get_unique(nums):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique


# Example usage:
nums = [1, 2, 2, 3, 4, 1, 5, 3]
result = get_unique(nums)
print(result)  
