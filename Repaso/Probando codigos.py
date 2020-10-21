def summation(a, b, f):
    s = 0
    for i in range(a, b+1): s += f(i)
    return s


def square(x):
    return x*x


def cube(x):
    return x*x*x


functions = [square, cube]
for function in functions:
    print(summation(1, 3, function), end=' ')
