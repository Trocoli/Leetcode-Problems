"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(nums, target):
    d = {}
    for index, value in enumerate(nums):  # enumerate function returns a tuples of key values of a list
        index_number = target - value   # if target = index 1 + index 2  then index 1 = target - index 2
        if index_number in d:
            return [d[index_number], index]
        else:
            d[value] = index

#  testing

l = [*range(1, 11, 1)]
print(l)
result = two_sum(l, 5)
print(result)
