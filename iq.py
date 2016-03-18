# # -*- coding: utf-8 -*-
# def iq_test(numbers):
#     tem = map(int, numbers.split())
#     # print tem, 为什么s = '10',list('10') = ['1', '0']?
#     # new_list = [int(x) for x in tem if x != ' ']
#     # print new_list
#     even = []
#     even_idx = []
#     odd = []
#     odd_idx = []
#     for idx, value in enumerate(tem):
#         if value % 2 == 0:  # 如果是偶数
#             even.append(value)
#             even_idx.append(idx + 1)
#         else:
#             odd.append(value)
#             odd_idx.append(idx + 1)
#     print even
#     print odd
#     print even_idx
#     print odd_idx
#     if len(even) > len(odd):
#         return odd_idx.pop()
#     elif len(even) < len(odd):
#         return even_idx.pop()
#
#
# print iq_test("2 4 7 8 10")
#
#
#
# # li = ['', '', '', 'a']
# # for s in li[:]:
# #     if s == '':
# #         li.remove(s)
# # print li
# # new_list = [x for x in li if x != '']

def gen():
    for x in range(4):
        tmp = yield x
        if tmp == 'hello':
            print 'world'
        else:
            print str(tmp)