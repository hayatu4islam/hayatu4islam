# def factorial(n):
#     result = 1
#     if n < 0:
#         return "The argument must be non-negative integer"
#     for v in range(1,n+1):
#         result *= v
#     return result

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))