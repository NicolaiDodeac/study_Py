import sys
sys.stdout.reconfigure(encoding='utf-8')

# print("hellow")
# num = 15  # приклад значення для num
# if num > 10:
#     print("num більше за 10")
# else:
#     print("num не більше за 10")

# x = int(input('Введіть число: '))

# if x % 2 == 0:
#     print("Число x є парним.")
# else:
#     print("Число x є непарним.")

# a = input('Введіть число')
# a = int(a)
# if a > 0:
#     print('Число додатне')
# elif a < 0:
#     print("Число від'ємне")
# else:
#     print('Це число - нуль')

# money = 0
# if money:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")


# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

# def modify_list(lst: list):    # прибрав -> None
#     lst = lst.copy()
#     lst.append(4)
# my_list = [1, 2, 3]            
# print(my_list)                  # виведе: [1, 2, 3]
# print(modify_list(my_list)) 

# a = 15
# if a % 3 == 0 and a % 5 == 0:
#     print("FizzBuzz")
# elif a % 3 == 0:
#     print("Fizz")
# elif a % 5 == 0:
#     print("Buzz")
# else:
#     print(a)
# x = -23
# y = 3
# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")

# some_data = 2
# msg = some_data or "Не було повернено даних"
# print(msg)

# pets = ("dog", "fish", "cat")

# match pets:
#     case ("dog", "cat", _):
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ("dog", _, _):
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")
 
# fruit = "BananaS"
# for char in fruit:
#     print(char, end =" & ")

# # Зчитування рядка від користувача
# user_input = "Введіть рядок:"

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input) # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")

# k = 0
# while k < 10:
#     k += 1
#     print(k)
#     if k >= 7:
#         break
# a = 1
# while True:
#     if a == 20:
#         print(a)
#         if a >= 20:
#             break
#     print(a, end = ";")
#     a += 1

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break

# number = int(input("number = "))
# while True:
#     print(number)
#     number -= 1
#     if number < 0:
#             break
# for i in range(5):
#     if i == 0:
#         continue
#     print(i)

# for i in range(0, 10):
#     print(i)

# for i in range(3, 10, 3):
#     print(i)

# some_list = ["apple", "banana", "cherry"]
# for value in enumerate(some_list):
#     print(value)

# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]
# for number1, number2 in zip(list2, list1):
# #     print(number1, number2)

# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }
# # for key in numbers:
# #     print(key)
# for key in numbers.items():
#     print(key)
# val = 'a'
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")
# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")

# def greetings(name = "incognito"):
#     print(f"Hello, dear {name}")
# greetings()
# greetings("petro")

# def print_max(a: int, b: int):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 5)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів

# def greet(name: str) -> str:
#     return f"Привіт, {name}!"

# greeting = greet("Олексій")
# print(greeting)  # Виведе: Привіт, Олексій!
# def pover
# greet()

# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print("Ключові аргументи:", kwargs)

# example_function(1, 2, 3, name="Alice", age=25)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
       
# print(factorial(4))

