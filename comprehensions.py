

# sq = []
# for i in range(1, 6):
#     sq.append(i**2)

# print(sq)
#! List Comprehensions
# [new_item for item in iterable if condition]

# sq = [x**2 for x in range(1, 6)]
# print(sq)

# even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
# print(even_squares)

# even_squares = []
# for x in range(1, 10):
#     if x % 2 == 0:
#         even_squares.append(x**2)

# print(even_squares)  # Виведе [4, 16, 36, 64]

#! Set Comprehensions
# {new_item for item in iterable if condition}

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
# sq1 = [i ** 2 for i in numbers]
print(sq)
# print(sq1)

odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)




# print("\033[H\033[J", end='')  # Переміщує курсор у верхній лівий кут і очищує екран
# 
# !Dictionary Comprehensions
# {key: value for item in iterable if condition}

sq = {x: x**2 for x in range(1, 10)}
print(sq)

sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict)

