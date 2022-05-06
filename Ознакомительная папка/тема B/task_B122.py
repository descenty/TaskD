# Написать функцию clean_string, которая получает строку и обрабатывает ее следующим образом:
# каждый символ # воспринмается как backspace, т.е. символ до # будет удален.
#
# Примеры:
# clean_string("abc#d##c") ==> "ac"

import traceback


def clean_string(s):
    arr = []
    for i in s:
        arr.append(i)
    while '#' in arr:
        del arr[arr.index('#') - 1]
        del arr[arr.index('#')]
    return ''.join(arr)


# Тесты
try:
    assert clean_string("abc#d##c") == "ac"
    assert clean_string("abc####d##c#") == ""
    assert clean_string("########") == ""
    assert clean_string("ab#cde##fgh#ij##") == "acfg"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
