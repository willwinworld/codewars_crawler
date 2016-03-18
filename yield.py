# -*- coding: utf-8 -*-
# def gen():
#     for x in ['a', 'b', 'c', 'd']:
#         tmp = yield x
#         if tmp == 'hello':
#             print 'world'
#         else:
#             # print str(tmp)
#             res = yield 4
#
#
# if __name__ == "__main__":
#     i = gen()
#     print i.send(None)
#     print i.send('hello')
#     print i.send(None)
#     print i.send(9999)
#     # for ii in i:
#     #     print ii

def h():
    print 'Wen Chuan',
    m = yield 5
    print 'bbbbbbb'
    print m
    d = yield 12
    print 'We are together!'

c = h()
mm = c.next()  # 此时mm是5
dd = c.send(None) # m是下一个yield表达式的参数即fighting,如果是c.send(None),m就是None
print 'We will never forget the date', mm, '.', dd  # dd是12