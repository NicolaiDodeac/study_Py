# print("Hello world!")
# print("give me green square")
# message = "Hello world!"
# print(message)
# name = "Oleg"
# hello_string = f"hello, {name}!"
# print(hello_string)

# side_a = 10
# side_b = 5
# hypotenuse = (side_a**2 + side_b**2)**0.5
# print(hypotenuse)

# n = 5000

# hours = n // (60 * 60)
# minutes = (n - hours * 60 * 60) // 60
# seconds = n - hours * 60 * 60 - minutes * 60
# print(f"{hours}h:{minutes}m:{seconds}s", end="econds")

# a = input("Рядок запрошення: ")

# a = float(input("Введіть сторону квадрата a: "))
# P = 4 * a
# print(f"Периметр квадрата дорівнює {P}")
# my_list = [1,'hello', 3.16]
# my_list.append("gaga")
# my_list.remove("hello")
# print(my_list)

# some_it = ["a","c","d"]
# numb = ["1","9","6"]
# sornam = sorted(numb)
# first = some_it[0]
# some_it.extend(numb)
# middle = some_it[-1]
# # two_it = some_it.pop(1),
# some_it.insert(2,"g"),
# some_it.insert(1,"f"),
# some_it.insert(3,"f"),
# chars = ["a","c"]
# # some_it.clear()
# # c_ind = some_it.index("c")
# # c_count = some_it.count("c")
# some_it.sort()
# some_it.sort(reverse=True)
# print(sornam)

# words = ["bananan", "apple", "cherry"]
# words.sort(key=len, reverse=True)
# print(words)

# nums = [3, 1, 4, 1, 5, 9, 2]
# sorted_nums = sorted(nums)
# print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

# sorted_nums_desc = sorted(nums, reverse=True)
# print(sorted_nums_desc)  # Виведе [9, 5, 4, 3, 2, 1, 1]

# words = ["banana", "apple", "cherry"]
# sorted_words = sorted(words, key=len)
# print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']

# chars =  ['d', 'a', 'b']
# chars_copy = chars.copy()
# chars_copy.sort()
# chars_copy.reverse()
# print(chars_copy)

# my_dict = {"name": "Nicolai", "age":34, "city":"Telford"}
# my_dict["age"] = 35
# my_dict["email"] = "alice@example.com"
# # del my_dict["age"]
# # print(my_dict["age"])
# # print("age" in my_dict)

# # age = my_dict.pop("age")

# # my_dict.update({"age": 32, 'superpower': 'ukrainian'})
# # print(my_dict)

# name = my_dict.get("name")  # Поверне 'Alice'
# gender = my_dict.get("gender")
# print(name, gender)

# lsst = [1, 2, 3, 1, 2, 2, 3, 4, 1]
# d_lst = set(lsst)
# lst=list(d_lst)
# print(lst)

# numbers = {1, 2, 3}
# b = {3, 4, 5}
# # numbers.discard(2)
# # numbers.add(2)
# # # numbers.remove(3)
# # # numbers.discard(1)
# # print(numbers.intersection(b))
# # print(numbers & b)
# # print(numbers.difference(b))
# # print(numbers - b)
# # print(numbers ^ b)
# # print(numbers | b)

# my_frozenset = frozenset([1, 2, 3, 4, 5])
# a = frozenset([1,2,5,4])
# b = frozenset([3, 4, 5])

# union = a | b  # Об'єднання множин
# intersection = a & b  # Перетин множин
# difference = a - b  # Різниця множин
# symmetric_difference = a ^ b  # Симетрична різниця

# print(union)  # frozenset({1, 2, 3, 4, 5})
# print(intersection)  # frozenset({3})
# print(difference)  # frozenset({1, 2})
# print(symmetric_difference)  # frozenset({1, 2, 4, 5})

# my_tuple = tuple()
# my_tuple = (1,2,3)
# print(my_tuple)
# # x = "kakashka malaska".title()
# x = "kakashka"
# y = x.upper()
# # print(x.lower())S
# # print(y)
# print(x.isdigit())
# print(x.isalpha())
# print(x.isspace())
# # print(x.capitalize())
# # print(y.startswith("k"))
# # print(x.endswith("a"))

# # Просте форматування рядка
# name = 'John'
# print('Hello, {}!'.format(name))

# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))

# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# # Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))

# Просте форматування рядка
name = 'John'
print(f'Hello, {name}!')

# Форматування з декількома аргументами
age = 25
print(f'Hello, {name}. You are {age} years old.')
