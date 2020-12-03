import timeit

code_to_test = """
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(f'Время на выполнение кода: {elapsed_time} секунд')
