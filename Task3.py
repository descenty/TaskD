import re
import traceback


def float_check(value: str):
    if (re.search(r'\.', value) or re.search(r'[eE]', value)) and re.search(r'^([-+]?\d*\.?\d+)(?:[eE]([-+]?\d+))?$', value):
        return value + ' is legal'
    else:
        return value + ' is illegal'


# Тесты
try:
    assert float_check('1.2') == '1.2 is legal'
    assert float_check('1.') == '1. is illegal'
    assert float_check("1.0e-55") == '1.0e-55 is legal'
    assert float_check('e-12') == 'e-12 is illegal'
    assert float_check('6.5E') == '6.5E is illegal'
    assert float_check('1e-12') == '1e-12 is legal'
    assert float_check('+4.1234567890E-99999') == '+4.1234567890E-99999 is legal'
    assert float_check('7.6e+12.5') == '7.6e+12.5 is illegal'
    assert float_check('99') == '99 is illegal'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")