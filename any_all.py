nums = [0, False, 5, 0]
result = any(nums)
result2 = all(nums)
print(result, result2)


nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)  
is_all_odd = all(x % 2 == 1 for x in nums) 

print(result)
print(is_all_odd)

words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)
