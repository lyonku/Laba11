import timeit

code_to_test = """

def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product

def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(f'Время на выполнение кода: {elapsed_time} секунд')