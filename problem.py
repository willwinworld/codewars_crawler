# -*- coding: utf-8 -*-
def sum_pairs(ints, s):
    distance = []
    indi = []
    indj = []
    valui = []
    valuj = []
    for idx_i, value_i in enumerate(ints): #遍历列表获得索引和值
        indi.append(idx_i)
        valui.append(value_i)
        for idx_j, value_j in enumerate(ints[idx_i:]):
            indj.append(idx_j)
            valuj.append(value_j)
            if value_i + value_j = s:
                distance.append((idx_j-idx_i))






