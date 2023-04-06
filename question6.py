import math

def calculate_formula(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        result += math.pow(arr[i], i) / math.factorial(i)
    return result

# example usage
arr = [1, 2, 2, 3, 3, 3, 5, 7, 11, 15]
result = calculate_formula(arr)
print("Result is:",result)