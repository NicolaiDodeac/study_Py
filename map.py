# numbers = [1, 2, 3, 4, 5]

# for i in map(lambda x: x ** 2, numbers):
#     print(i)


# squared_nums = list(map(lambda x: x ** 2, numbers))
# print(squared_nums)

nums = [1, 2, 3, 4, 5]
squared_nums = [x ** 3 for x in nums] #! Comprehension
print(squared_nums)


# nums1 = [1, 2, 3, 14]
# nums2 = [4, 5, 6]
# sum_nums = map(lambda x, y: x + y, nums1, nums2) #! Map

# print(list(sum_nums))

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)] #! Comprehension
print(sum_nums)
