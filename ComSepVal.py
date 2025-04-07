import csv


# # Дані для запису
# rows = [
#     ["name", "age", "specialty"],
#     ["Василь Гупало", 30, "Математика"],
#     ["Марія Петренко", 22, "Фізика"],
#     ["Олександр Коваленко", 20, "Інформатика"],
# ]

# # Відкриваємо файл для запису
# with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
#     # Створюємо об'єкт writer
#     writer = csv.writer(csvfile, delimiter=",")
#     # Записуємо рядки даних
#     writer.writerows(rows)


# with open("data.csv",newline="", encoding="utf-8") as csvf:
#     reader = csv.reader(csvf, delimiter=",")
#     for row in reader:
#         print(" - ".join(row))


# Запис у CSV файл зі словників
# with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:
#     fieldnames = ["name", "age", "specialty"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({"name": "Олег Олегов", "age": 23, "specialty": "Історія"})
#     writer.writerow({"name": "Анна Сергіївна", "age": 22, "specialty": "Біологія"})

# # Читання з CSV файлу в словники
# with open("students.csv", newline="", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row["name"], row["age"], row["specialty"])

import csv

FILENAME = "users.csv"

users = [
    {"name": "Микола", "age": 22, "gender": "male"},
    {"name": "Марія", "age": 22, "gender": "female"},
    {"name": "Назар", "age": 22, "gender": "male"},
]

with open(FILENAME, "w", encoding="utf-8", newline="") as f:
    columns = users[0].keys()
    writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)

with open(FILENAME, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
