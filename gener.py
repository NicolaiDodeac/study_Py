# import time
# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()

# print(next(gen)) 
# print(next(gen)) 
# print(next(gen)) 

# def count_down(start):
#     while start > 0:
#         yield start
#         time.sleep(1)
#         start -= 1

# for number in count_down(5):
#     print(number)

def read_lines(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip()

for line in read_lines("./my_file.txt"):
    print(line)
