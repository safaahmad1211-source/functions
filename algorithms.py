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


def login():
    username = input("Username: ")
    password = input("Password: ")
    return username == "admin" and password == "1234"


def main():
    logged_in = False

    def guard():
        if not logged_in:
            print("Please login first!")
            return False
        return True

    def option_1():
        if not guard():
            return
        n = int(input("Enter number: "))
        print("Factorial =", factorial(n))

    def option_2():
        if not guard():
            return
        nums = list(
            map(int, input("Enter numbers (space-separated): ").split()))
        print("Max =", find_max(nums))

    def option_3():
        if not guard():
            return
        nums = list(
            map(int, input("Enter numbers (space-separated): ").split()))
        target = int(input("Enter target: "))
        print("Found:", linear_search(nums, target))

    def option_4():
        if not guard():
            return
        n = int(input("Enter n: "))
        print("Fibonacci =", fibonacci(n))

    def option_5():
        nonlocal logged_in
        logged_in = login()
        print("Login successful!" if logged_in else "Try again.")

    def option_6():
        print("Goodbye!")
        sys.exit(0)

    switch = {
        "1": option_1,
        "2": option_2,
        "3": option_3,
        "4": option_4,
        "5": option_5,
        "6": option_6
    }

    while True:
        print("\n Menu:")
        print("1. Factorial")
        print("2. Find Max")
        print("3. Linear Search")
        print("4. Fibonacci")
        print("5. Login")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        func = switch.get(choice)
        func() if func else print("Invalid option, try again.")


if __name__ == "__main__":
    main()
