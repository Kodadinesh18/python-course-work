def power_of_number():
    print("Program: Power of a Number")
    print('''\
def power(base, exponent):
    return base ** exponent

# Test Cases
print(power(2, 3))  # Output: 8
print(power(5, 0))  # Output: 1
print(power(7, 2))  # Output: 49
''')
    print("Explanation: The function uses the exponentiation operator '**' to return the result of base raised to exponent.\n")


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


def perfect_number():
    print("Program: Perfect Number")
    print('''\
def perfect_number(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

# Test Cases
print(perfect_number(6))   # Output: True
print(perfect_number(28))  # Output: True
print(perfect_number(10))  # Output: False
''')
    print("Explanation: A Perfect number equals the sum of its proper divisors excluding itself.\n")


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
