# import random

# both = 0
# fizzbuzz_list = []
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, ' FizzBuzz')
#         both +=1
#         fizzbuzz_list.append(i)
#     if i % 3 == 0:
#         print(i, ' Fizz')
#     elif i % 5 == 0:
#         print(i, ' Buzz')
#     else:
#         print(i)
#
# print('Total FizzBuzz appeared: ', both)
# print('FizzBuzz appeared list: ', fizzbuzz_list)

# mylist = [2, 5, 1, 7, 3, 9, 5]
#
# minnum = min(mylist)
# maxnum = max(mylist)


# difference = maxnum-minnum

# def max_difference(nums):
#     max_diff = 0
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             diff = nums[j] - nums[i]
#             if diff > max_diff:
#                 max_diff = diff
#     return max_diff
#

# max_difference(mylist)
# print('Difference between minimum and maximum number is: ', max_difference(mylist))


# nums = [2, 5, 1, 7, 3, 9, 5]
# target = 10
#
#
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [nums[i], nums[j]]
#
#
# print(two_sum(nums, target))
# TODO = will resolve the problem in morning

# mylist = [3, 5, 2, 8, 1, 23,4,0]
# min_val = mylist[0]
# max_val = mylist[0]
# for i in range(len(mylist)):
#     if mylist[i] < min_val:
#         min_val = mylist[i]
#     if mylist[i] > max_val:
#         max_val = mylist[i]
#
# print(min_val, max_val)


# TODO = Write a Python function to check if a given string is a palindrome or not. A palindrome is a word, phrase,
#  number, or other sequence of characters that reads the same forward and backward


# mystr = "racyuecar"

# if mystr == mystr[::-1]:
#     print('This is Palindrome string')


