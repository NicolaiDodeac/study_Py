'''
рахувати вік людини
'''
from datetime import datetime as dtdt, timedelta as td

# варіант мій
# def calculate_person_age(d_of_b_str: str) -> int:
#     d_of_birth = dtdt.strptime(d_of_b_str, "%Y-%m-%d")
#     dob_delta = td(days=(d_of_birth.toordinal()))
#     today = dtdt.now()
#     today_delta = td(days=(today.toordinal()))
#     age = (today_delta - dob_delta).days // 365
#     return age


# варіант викладача
# def calculate_person_age(d_of_b_str: str) -> int:
#     d_of_birth = dtdt.strptime(d_of_b_str, "%Y-%m-%d")
#     today = dtdt.now()
#     d_of_birth_this_year = d_of_birth.replace(year=today.year)
#     # print(d_of_birth_this_year)
#     age = today.year - d_of_birth.year
#     # print(d_of_birth_this_year, today)
#     if (d_of_birth_this_year > today):
#         age -= 1
#     return age

# варіант геніальний з LLM
def calculate_person_age(d_of_b_str: str) -> int:
    d_of_birth = dtdt.strptime(d_of_b_str, "%Y-%m-%d") 
    today = dtdt.now()

    age = today.year - d_of_birth.year - ((today.month, today.day) < (d_of_birth.month, d_of_birth.day)) # якщо сьогоднішня дата ще не відбулася і є меншою то тру перетворитьчя на одиницю і ми віднімемо її від років

    return age

# Example Usage
print(calculate_person_age("2000-03-04"))  #  24
print(calculate_person_age("1995-12-10"))  #  29
print(calculate_person_age("2019-06-27")) # 5
assert calculate_person_age("2019-06-27") == 5