def make_adder(n):
    def add(x):
        return x + n
    return add


if __name__ == '__main__':
    plus_3 = make_adder(3)
    plus_5 = make_adder(5)

    print(plus_3(3))
    print(plus_5(7))
