<<<<<<< Updated upstream
def sum_num(value):
    res = 0

    while value != 0:
        res += value % 10
        value //= 10

    return res
arr = [i**3 for i in range(1, 1001, 2)]

res_1 = sum(filter(lambda num: sum_num(num) % 7 == 0, arr))
res_2 = sum(filter(lambda num: sum_num(num + 17) % 7 == 0, arr))

print(res_1)
=======
def sum_num(value):
    res = 0

    while value != 0:
        res += value % 10
        value //= 10

    return res
arr = [i**3 for i in range(1, 1001, 2)]

res_1 = sum(filter(lambda num: sum_num(num) % 7 == 0, arr))
res_2 = sum(filter(lambda num: sum_num(num + 17) % 7 == 0, arr))

print(res_1)
>>>>>>> Stashed changes
print(res_2)