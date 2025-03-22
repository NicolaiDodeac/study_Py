# def my_function():
#     print("Hello, world!")

# f = my_function
# f()

from typing import Callable, Dict

# def add(a: int, b: int) -> int:
#     return a + b

# def multiply(a: int, b: int) -> int:
#     return a * b

# # def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
# #     return operation(a, b)

# # # Використання
# # result_add = apply_operation(4, 3, add)
# # result_multiply = apply_operation(5, 3, multiply)

# # print(result_add, result_multiply)

# def power(exponent: int) -> Callable[[int], int]:
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner

# # Використання
# square = power(2)
# cube = power(3)

# operations: Dict[str, Callable] = {
#     'add': add,
#     'multiply': multiply,
#     'square': square,
#     'cube': cube
# }

# result_add = operations['add'](10, 20)  # 30
# result_square = operations['square'](5)  # 25
# result_cube = operations['cube'](8)

# print(result_add)  
# print(result_square)  
# print(result_cube)  


# 
