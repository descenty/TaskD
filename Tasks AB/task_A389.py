# Задан список автобусных остановок, который состоит из списков из двух элементов:
# количество пассажиров, которые зашли и вышли из автобуса.
# Написать функцию bus, которая вычисляет сколько осталось
# пассажиров в автобусе к последней остановке.


import traceback


def bus(bus_stops):
    return sum(x[0] - x[1] for x in bus_stops)


# Тесты
try:
    assert bus([[10,0],[3,5],[5,8]]) == 5
    assert bus([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) == 17
    assert bus([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) == 21
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
