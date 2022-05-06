# Написать функцию morse, которая расшифровывает строку, закодированную азбукой Морзе
# a .-      h ....    o ---     u ..-      1 .----     6 -....
# b -...    i ..      p .--.    v ...-     2 ..---     7 --...
# c -.-.    j .---    q --.-    w .--      3 ...--     8 ---..
# d -..     k -.-     r .-.     x -..-     4 ....-     9 ----.
# e .       l .-..    s ...     y -.--     5 .....     0 -----
# f ..-.    m --      t -       z --..
# g --.     n -.
#
# Пример:
# morse("..  .- --  .-  - . ... -") ==> "i am a test"
import traceback

#Создание словаря
unfilt = 'a .-      h .... o ---     u ..-      1 .----     6 -.... b -...    i ..      p .--.    v ...-     2 ..---     7 --... c -.-.    j .---    q --.-    w .--      3 ...--     8 ---.. d -..     k -.-     r .-.     x -..-     4 ....-     9 ----. e .       l .-..    s ...     y -.--     5 .....     0 ----- f ..-.    m --      t -       z --.. g --.     n -.'
unfilt = unfilt.split()
morseDict = {}
counter = 0
last = ''
for i in unfilt:
    if counter % 2 == 0:
        last = i
    else:
        morseDict[last] = i
    counter += 1
morseDict = {v: k for k, v in morseDict.items()}
#

def morse(text):
    value = ''
    for i in text.replace('  ', ' _ ').split():
            value += ' ' if i == '_' else morseDict[i]
    return value


# Тесты
try:
    assert morse(".... . .-.. .-.. ---  .-- --- .-. .-.. -..") == "hello world"
    assert morse(".---- ... -  .- -. -..  ..--- -. -..") == "1st and 2nd"
    assert morse(".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.") \
        == "abcdefghijklmnopqrstuvwxyz0123456789"
    assert morse("") == ""
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
