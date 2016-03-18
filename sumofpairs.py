# def sum_pairs(ints, s):
#     candidates = []
#     for idx, i in enumerate(ints):
#         for idj, j in enumerate(ints[idx:]):
#             if i + j == s:
#                 if idx != idj and i != j:
#                     candidates.append((idj-idx, [i, j]))
#     if len(candidates) == 0:
#         return None
#     return sorted(candidates, cmp=lambda a, b: a[0] - b[0])[0][1]
#
#
# l1= [1, 4, 8, 7, 3, 15]
# l2= [1, -2, 3, 0, -6, 1]
# l3= [20, -13, 40]
# l4= [1, 2, 3, 4, 1, 0]
# l5= [10, 5, 2, 3, 7, 5]
# l6= [4, -2, 3, 3, 4]
# l7= [0, 2, 0]
# l8= [5, 9, 13, -3]
#
# print sum_pairs(l1, 8)
# print sum_pairs(l2, -6)
# print sum_pairs(l5, 10)
# print sum_pairs(l1, 8) , "Basic: %s should return [1, 7] for sum = 8" % l1
# print sum_pairs(l2, -6), "Negatives: %s should return [0, -6] for sum = -6" % l2
# print sum_pairs(l3, -7), "No Match: %s should return None for sum = -7" % l3
# print sum_pairs(l4, 2), "First Match From Left: %s should return [1, 1] for sum = 2 " % l4
# print sum_pairs(l5, 10) , "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5
# print sum_pairs(l6, 8), "Duplicates: %s should return [4, 4] for sum = 8" % l6
# print sum_pairs(l7, 0), "Zeroes: %s should return [0, 0] for sum = 0" % l7
# print sum_pairs(l8, 10), "Subtraction: %s should return [13, -3] for sum = 10" % l8
