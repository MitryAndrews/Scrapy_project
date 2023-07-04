import time


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Время работы функции {dt} сек')
        return res
    return wrapper

# def some_func(x):
#     x = x * x
#     y = x * x * x
#     print(f'we solve something {x}')
#     return y
@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

# get_nod = test_time(get_nod)
# get_fast_nod = test_time(get_fast_nod)
a, b = 1000000, 3
res = get_nod(a, b)
res2 = get_fast_nod(a, b)
print(res, res2)
