# Linus challened me to try solve this recursively
# If n == 0, return 0 (F(0) = 0)
# If n == 1, return 1 (F(1) = 1)
# Initialize a = 0 (two steps back)
# Initialize b = 1 (one step back)
#  then loop from 2 up to n (inclusive):
# The new number is a + b
# move them over: a becomes b, b becomes the new number (a + b)
# when theloop finishes, b will hold the n-th Fibonacci number.
# lastly return b.

# my original solution
# def fibonacci(n):
#     # my base cases
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     # a represents F(i-2), b represents F(i-1) from the readme - I should have paid better attention and used the answer it gave
#     a, b = 0, 1

#     # my unnecessary looping through from 2 up to n
#     for _ in range(2, n + 1):
#         a, b = b, a + b

#     return b

# this was what I thought was a recursive-er version but I was quickly schooled into a much faster way
# def fibonacci(n, sequence=None):
#     if sequence is None:
#         sequence = {}
#         # I want enter my base case
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     if n in sequence:
#         return sequence[n]

#     sequence[n] = fibonacci(n - 1, sequence) + fibonacci(n - 2, sequence)
#     return sequence[n]


# and then Linus told me I was doing way too much :-/
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
