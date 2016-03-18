# -*- coding: utf-8 -*-
def multiplication_table(row, col):
    res = []
    # item = [] 一开始初始化一个列表，始终不变是有很大区别的
    for i in range(1, row+1):
        item = []  # 每次循环初始化一个列表
        for j in range(1, col+1):
            item.append(i*j)
        res.append(item)
    return res

sss = multiplication_table(5, 5)
print sss
