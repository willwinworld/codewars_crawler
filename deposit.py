# -*- coding: utf-8 -*-
# import tika
# tika.initVM()
#
# from tika import parser
# parsed = parser.from_file(r'C:/Users/Administrator/lpthw/ia/test.pdf')
# print parsed

# def f(x):
#     return x + 1
# def g(x):
#     return x
# def compose(f, g):
#     return lambda x: f(g(x))
#
# res = compose(f, g)(0) == 1
# print res

#
# def digitize(n):
#     return [e for e in reversed([i for i in str(n)])]
#
# res = digitize(345346)
# print res
#
#
# ll = list(range(0, 10))
#
# print ll[::-1]

# from operator import add

#
# def tickets(people):
#     deposit = [0, 0, 0]
#     print people
#     for p in people:
#         if p == 25:
#             deposit = map(add, deposit, [1, 0, 0])
#         elif p == 50:
#             deposit = map(add, deposit, [-1, 1, 0])
#         else:
#             # if deposit[0] >= 1 and deposit[1] >= 1:
#             #    deposit = map(add, deposit, [-1, -1, 1])
#             # elif deposit[1] == 0 and deposit[0] >= 3:
#             #    deposit = map(add, deposit, [-3, 0, 1])
#             # else:
#             deposit = map(add, deposit, [-3, 0, 1])
#     print deposit
#     # if deposit[0] < 0 or deposit[1] < 0 or deposit[2] < 0: return 'NO'
#     if deposit[0]*25 + deposit[1]*50<0: return 'No'
#     return 'YES'
#
# print tickets([100, 50, 25, 25])
# print tickets([25, 25, 50])
# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.
#
# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
#
# Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?
#
# Return YES, if Vasya can sell a ticket to each person and give the change. Otherwise return NO.
# ### Python ###
#
# tickets([25, 25, 50]) # => YES
# tickets([25, 100])
#          # => NO. Vasya will not have enough money to give change to 100 dollars
#
# from operator import add
# def tickets(people):
#     deposit = [0, 0, 0]
#     print people
#     for money in people:
#         if money == 25:
#             deposit = map(add, deposit, [1, 0, 0])
#         elif money == 50:
#             deposit = map(add, deposit, [-1, 1, 0])
#         else:
#             deposit = map(add, deposit, [-3, 0, 1]) or map(add, deposit, [-1, -1, 1])
#     print deposit
#     if (deposit[0]*25 + deposit[1]*50 + deposit[2]*100) < 0:
#         return 'NO'
#     else:
#         return 'YES'

# print tickets([50, 50, 50, 50, 50, 50, 50, 50, 50, 50])
# print tickets([100, 50, 25, 25])


def tickets(people):
    change = 'YES' # 设定一开始有找零
    twentyfive, fifty, onehundred = 0, 0, 0

    for cash in people:
        if change == 'NO':
            break

        if cash == 25:
            twentyfive += 1
        elif cash == 50 and twentyfive > 0:
            twentyfive -= 1
            fifty += 1
        elif cash == 100:
            if fifty > 0 and twentyfive > 0:
                fifty -= 1
                twentyfive -= 1
                onehundred += 1
            elif twentyfive > 2:
                twentyfive -= 3
                onehundred += 1
            else:
                change = 'NO'
        else:
            change = 'NO'

    return change

print tickets([50, 50, 50])