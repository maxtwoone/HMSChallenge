import math


def reverse(num):
    return int(num != 0) and ((num % 10) * \
                              (10 ** int(math.log(num, 10))) + \
                              reverse(num // 10))


def isPalindrome(num):
    return num == reverse(num)


def palindrome(num):
    global counter
    if isPalindrome(num):
        return num, counter
    else:
        num = num + reverse(num)
        counter += 1
        if num <= 1_000_000_000:
            return palindrome(num)
        else:
            return -1, counter

counter = 0

print(palindrome(196))

