def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    print e
    print '@@' * 20
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

if __name__ == "__main__":
    iq_test("2 4 7 8 10")
