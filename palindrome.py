"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

"""


def palindrome(x):
    s = str(x)
    rs = "".join(list(reversed(s)))
    if rs != s:
        return False
    return True

print(palindrome(121))
print(palindrome(1211))
