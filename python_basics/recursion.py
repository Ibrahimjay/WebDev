from functools import lru_cache
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
# for n in range(1,11):
#     print(n, ':', fibonacci(n))

#memoization
# fibonacci_cache = {}
# def fibonacci(n):
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         value =  fibonacci(n-1) + fibonacci(n-2)
    
#     fibonacci_cache[n] = value
#     return value
# for n in range(1,101):
#     print(n, ':', fibonacci(n)) 

# one line way to add memoization
@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
for n in range(1,101):
    print(n, ':', fibonacci(n))