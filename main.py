import collections

# Cat =collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

# cat = Cat('Simon', 4, 'Krabat')

# print(f'This is a cat {cat.nickname}, {cat.age} age, his owner is {cat.owner}')

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1

# print(mark_counts)

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)


# student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)

# print(mark_counts.most_common())
# print(mark_counts.most_common(1))
# print(mark_counts.most_common(2))

# from collections import Counter

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_count = Counter(words)

# # Виведення слова та його частоти
# for word, count in word_count.items():
#     print(f"{word}: {count}")

from collections import defaultdict

# d = defaultdict(list)

# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)

# print(d)
# d = defaultdict(int)

# # Збільшення значення для кожного ключа
# d['a'] += 1
# d['b'] += 1
# d['a'] += 1

# print(d)

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = {}

# for word in words:
#     char = word[0]
#     if char not in grouped_words:
#         grouped_words[char] = []
#     grouped_words[char].append(word)

# print(grouped_words)

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))
