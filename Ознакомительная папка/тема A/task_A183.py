# Написать функцию two_identical(start, finish), которая определяет количество чисел
# в интервале между числами start и finish (их не считая), в записи которых есть хотя бы две одинаковые цифры.
#
# Примеры:
# max_multiple(20,33) ==> 1 (число 22)
# max_multiple(0,101) ==> 10

import traceback


def two_identical(start, finish):
    return sum([str(x).count(str(y)) >= 2 for x in range(start + 1, finish) for y in range(10)])


# Тесты
try:
    assert two_identical(20, 33) == 1
    assert two_identical(0, 10) == 0
    assert two_identical(0, 101) == 10
    assert two_identical(0, 1000) == 261
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")