from collections import deque

# # Створення черги
# queue = deque()

# # Enqueue: Додавання елементів
# queue.append('a')
# queue.append('b')
# queue.append('c')

# print("Черга після додавання елементів:", list(queue))

# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.popleft())

# print("Черга після видалення елемента:", list(queue))

# # Peek: Перегляд першого елемента
# print("Перший елемент у черзі:", queue[0])

# # IsEmpty: Перевірка на порожнечу
# print("Чи черга порожня:", len(queue) == 0)

# # Size: Розмір черги
# print("Розмір черги:", len(queue))


# d = deque()

# d.append('middle')
# d.append('list')
# d.append('first')

# print("Черга після додавання елементів:", list(d))
# print("Видалений останній елемент:", d.pop())
# print("Видалений перший елемент:", d.popleft())
# print("Черга після видалення елементів:", list(d))

# d = deque(maxlen=5)
# for i in range(10):
#     d.append(i)

# print(d)

tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]

tasks_queue = deque()
for task in tasks:
    if task["type"] == "fast":
        tasks_queue.appendleft(task)
        print(f"Додано швидке завдання '{task['name']}'")
    else:
        tasks_queue.append(task)
        print(f"Додано {task['type']} завдання '{task['name']}'")

while tasks_queue:
    task = tasks_queue.popleft()
    print(f'Виконується завдання: "{task['name']}"')

