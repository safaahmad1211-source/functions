import sys


def factorial(n):
    # O(n)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_max(numbers):
    # O(n)
    if not numbers:
        raise ValueError("List cannot be empty")
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num


def linear_search(numbers, target):
    # O(n)
    for num in numbers:
        if num == target:
            return True
    return False


def fibonacci(n):
    # Iterative O(n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
