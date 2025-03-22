# def complicated(x: int, y: int) -> int:
#     return x + y

# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner

# complicated = logger(complicated)
# print(complicated(2, 3))

# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: ")
#         return result

#     return inner

# @logger
# def complicated(x: int, y: int) -> int:
#     return x + y

# print(complicated(2, 3))
# print(complicated(2, 5))

# from functools import wraps

# def logger(func):
#     @wraps(func)
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner

# @logger
# def complicated(x: int, y: int) -> int:
#     return x + y

# print(complicated(2, 3))
# print(complicated.__name__)

'''написати декоратор для виведення логів'''
from datetime import datetime
from functools import wraps
# print ('2024-01-22 13:30:30 INFO userLogged in')
def log_decorator(level: str):
    def actual_log_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            operation_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            print(f'{operation_time} {level} Calling function {func.__name__} with arguments: {args}, {kwargs} and result:')
            return result
        return wrapper
    return actual_log_decorator

@log_decorator("Debug")
def  sum_numbers(num_a: int, num_b: int) -> int:
    '''Function that returns sum of two numbers'''
    return num_a + num_b
print(sum_numbers(5,3))
# print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
# print(dir(sum_numbers))
print(sum_numbers.__name__)