from colorama import Fore, Back, Style
from itertools import zip_longest
import sys
import os

# from diff_func import c, print_hello
# print_hello()
# print(c)
# print(sys.argv)
# print(len(sys.argv))

if len(sys.argv) != 3:
    print(Fore.RED + "Error: please provide file path for file a and file b", Style.RESET_ALL)
    sys.exit(1)

# file_one = sys.argv[1]
# file_two = sys.argv[2]
_, file_one_path, file_two_path = sys.argv

if not os.path.exists(file_one_path) or not os.path.exists(file_two_path):
    print(Fore.RED + "Error: please provide file path for file that exists", Style.RESET_ALL)
    sys.exit(1) 

file_one_lines = []
file_two_lines = []

with open(file_one_path) as file_one:
    file_one_lines = file_one.readlines()

with open(file_two_path) as file_two:
    file_two_lines = file_two.readlines()

# print(file_one_lines)
# print(file_two_lines)

# print("Working on comparing files...")
for index, item in enumerate(zip_longest(file_one_lines, file_two_lines, fillvalue=''), start=1):
    # print(item)
    file_one_line = item[0].strip()
    file_two_line = item[1].strip()
    if file_one_line != file_two_line:
        print(f"Line:{index}")
        print(Fore.RED + '>' + file_one_line + Style.RESET_ALL)
        print(Fore.GREEN + '>' + file_two_line + Style.RESET_ALL)