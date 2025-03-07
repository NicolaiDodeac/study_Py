# print("hello\nPyton")
# print("hello\tPyton")
# print("Hello my little\rsis")
# print("Hello \bWorld")

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query) # q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>

# obj_query = {}
# for el in query.split('&'): # q=Cat+and+dog   ie=utf-8  oe=utf-8  aq=t
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)

# user_input = input("Введіть число: ")
# if user_input.isdigit():
#     print("Це дійсно число!")
# else:
#     print("Це не число!")

# for char in "Hello 123":
#     if char.isdigit():
#         print(f"'{char}' - це цифра")
#     else:
#         print(f"'{char}' - не цифра")


# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab,outtab)
# example = "This is string example"
# print(example.translate(trantab))


# intab = "aeioutdsvgsd"
# trantab = str.maketrans('', '', intab)

# str = "This is string example"
# print(str.translate(trantab))


morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди
# table_morze_dict = {}
# for k, v in morze_dict.items():
#     table_morze_dict[ord(k)] = v

# string = "Hello world"

# result = ""

# for ch in string:
#     result = result + ch.upper().translate(table_morze_dict)

# print(result)

# for i in range(8):
#     s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
#     print(s)

# price = 19.99
# quantity = 3.2
# total = f"Total: {price * quantity:.2f}"
# print(total)

# width = 5
# for num in range(12):
#     print(f'{num:^10} {num**2:^10} {num**3:^10}')
