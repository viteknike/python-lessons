def maxnum(*numbers):
    number = numbers[0]
    for num in numbers:
        if number < num:
            number = num
    return number
def minnum(*numbers):
    number = numbers[0]
    for num in numbers:
        if number > num:
            number = num
    return number
def sumnum(*numbers):
    number = 0
    for num in numbers:
        number += num
    return number


