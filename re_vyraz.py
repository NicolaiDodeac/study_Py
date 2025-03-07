import re

# text = "Вивчення Python може бути веселим."
# pattern = "Python"
# match = re.search(pattern, text)

# if match:
#     print("Знайдено:", match.group())
# else:
#     print("Не знайдено.")

# text = "Вивчення Python може бути веселим."
# pattern = r"в\w*м"
# match = re.search(pattern, text, re.IGNORECASE)

# if match:
#     print("Знайдено:", match.group())


text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    print("Електронна адреса:", match.group())


text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)
print(matches)


text = "Python - це проста, 23 але потужна мова програмування."
pattern = r"\w+"
matches = re.findall(pattern, text)
print(matches)  # Виведе список всіх слів у рядку


phone = """
        Михайло Куліш: 050-171-1634
        Вікторія Кущ: 063-134-1729
        Оксана Гавриленко: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(formatted_phone)

# pat3=r'[\w\._]+@\w+\.\w+'
# прикласти cheat sheet
import re #regular expressions regex regexp

# s='1234+78998 7+++asd1234  ++ ++ 1234sdas 1231 123 123asdasd'
# pat1=r'\w+'
# # d - digit
# # + - 1 і більше
# res1=re.findall(pat1,s)
# res2=re.search(pat1,s)
# print(res1)
# print(res2.group())
# print(res2.span())
# s2='pi is 3.14 and it\'s a constant'\
#     ', .5 is also a constant but has no name'

# pat2=r'\d*\.\d+'
# print(re.findall(pat2,s2))

# mail="j.s_m_ith@stud.mail.com '; drop database; coll_11@10mituesmail.com


