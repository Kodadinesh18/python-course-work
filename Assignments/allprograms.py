def kadane_algorithm():
    print("Program: Kadane's Algorithm (Maximum Subarray Sum)")
    print('''\
def kadane(arr):
    max_sum = current_sum = arr[0]
    for x in arr[1:]:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Test Cases
print(kadane([-2, -3, 4, -1, -2, 1, 5, -3]))  # Output: 7
print(kadane([1, 2, 3, -2, 5]))              # Output: 9
print(kadane([-1, -2, -3, -4]))              # Output: -1
''')
    print("Explanation: Kadane’s Algorithm finds the maximum subarray sum by dynamically tracking the maximum sum ending at each position.\n")


def factors_of_number():
    print("Program: Factors of a Number")
    print('''\
def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Test Cases
print(factors(6))   # Output: [1, 2, 3, 6]
print(factors(15))  # Output: [1, 3, 5, 15]
''')
    print("Explanation: The function returns a list of all integers that divide the number without a remainder.\n")


def prime_factors():
    print("Program: Prime Factors")
    print('''\
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Test Cases
print(prime_factors(28))  # Output: [2, 2, 7]
print(prime_factors(60))  # Output: [2, 2, 3, 5]
''')
    print("Explanation: The function finds the prime factors by dividing the number with the smallest prime divisor repeatedly.\n")


def strong_number():
    print("Program: Strong Number")
    print('''\
def strong_number(n):
    import math
    return n == sum(math.factorial(int(d)) for d in str(n))

# Test Cases
print(strong_number(145))  # Output: True
print(strong_number(123))  # Output: False
''')
    print("Explanation: A Strong number is one whose digits' factorial sum equals the number itself.\n")


def merge_sorted_arrays():
    print("Program: Merge 2 Sorted Arrays Without Using Extra Space")
    print('''\
def merge(arr1, arr2):
    n, m = len(arr1), len(arr2)
    i, j = n - 1, 0
    
    # Swap elements to maintain sorted order
    while i >= 0 and j < m and arr1[i] > arr2[j]:
        arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1
    
    # Sort both arrays individually
    arr1.sort()
    arr2.sort()
    return arr1, arr2

# Test Cases
print(merge([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]))  
# Output: ([1, 2, 3, 5, 8, 9], [10, 13, 15, 20])
''')
    print("Explanation: Two sorted arrays are merged without using extra space by swapping elements and re-sorting them.\n")


def perfect_square():
    print("Program: Perfect Square")
    print('''\
def perfect_square(n):
    return int(n**0.5) ** 2 == n

# Test Cases
print(perfect_square(25))  # Output: True
print(perfect_square(20))  # Output: False
''')
    print("Explanation: Checks if the square of the integer square root is equal to the number.\n")


def automorphic_number():
    print("Program: Automorphic Number")
    print('''\
def automorphic(n):
    return str(n * n).endswith(str(n))

# Test Cases
print(automorphic(5))   # Output: True (5^2 = 25)
print(automorphic(76))  # Output: True (76^2 = 5776)
print(automorphic(7))   # Output: False
''')
    print("Explanation: A number is Automorphic if its square ends with the number itself.\n")


def harshad_number():
    print("Program: Harshad Number")
    print('''\
def harshad(n):
    return n % sum(int(d) for d in str(n)) == 0

# Test Cases
print(harshad(18))  # Output: True
print(harshad(21))  # Output: True
print(harshad(19))  # Output: False
''')
    print("Explanation: A number is Harshad if it is divisible by the sum of its digits.\n")


def abundant_number():
    print("Program: Abundant Number")
    print('''\
def abundant(n):
    return sum(i for i in range(1, n) if n % i == 0) > n

# Test Cases
print(abundant(12))  # Output: True
print(abundant(15))  # Output: False
''')
    print("Explanation: A number is Abundant if the sum of its proper divisors is greater than the number.\n")


def friendly_pair():
    print("Program: Friendly Pair")
    print('''\
def sum_of_divisors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

def friendly_pair(a, b):
    return sum_of_divisors(a)/a == sum_of_divisors(b)/b

# Test Cases
print(friendly_pair(6, 28))    # Output: True
print(friendly_pair(30, 140))  # Output: False
''')
    print("Explanation: Two numbers form a Friendly Pair if their divisor-sum ratios are equal.\n")
