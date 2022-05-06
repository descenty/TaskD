# Написать функцию highest_rank(arr), которая возвращает самое часто встречающееся число в списке,
# если таких чисел несколько - вернуть наибольшее.
#
# Пример:
# highest_rank([1,0,1,0,1,0,1) => 1


import traceback


def highest_rank(arr):
    values_dict = {}
    for i in arr:
        if i not in values_dict:
            values_dict[i] = 1
        else:
            values_dict[i] += 1
    values = sorted(values_dict.items(), key=lambda x: x[1], reverse=True)
    max_value = max([x[1] for x in values])
    return max([x[0] for x in values if x[1] == max_value])


# Тесты
try:
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]) == 12
    assert highest_rank([2, 10, 8, 2, 7, 6, 4, 10, 2, 10]) == 10
    assert highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]) == 3
    assert highest_rank([1, 2, -3, 1, 2, -3, 1, 2, -3, 1, 2, -3]) == 2
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")