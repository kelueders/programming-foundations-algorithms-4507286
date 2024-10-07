# Example file for Programming Foundations: Algorithms by Joe Marini
# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    # MY METHOD
    m = min(a, b)
    for x in range(1, m):
        y = m / x
        if a % y == 0 and b % y == 0:
            return int(y)

    # ANSWER KEY
    # while (b != 0):
    #     t = a       # set aside the value of a
    #     a = b       # set a equal to b
    #     b = t % b   # divide t (which is a) by b

    return a


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
