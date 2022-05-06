# Создать список (супермаркет), состоящий из словарей (товары). Словари должны содержать
# как минимум 5 полей
# (например, номер, наименование, отдел продажи, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# market = [{"id":123456, "product":"coca-cola 0.5", "department": "drinks", ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех товарах;
# – вывода информации о товаре по введенному с клавиатуры номеру;
# – вывода количества товаров, продающихся в определенном отделе;
# – обновлении всей информации о товаре по введенному номеру;
# – удалении товара по номеру.
# Провести тестирование функций.

import enum


class GoodsDepartment(enum.Enum):
    drinks = 0
    milk = 1
    snacks = 2
    vegetables_fruits = 3
    sauces = 4
    chocolate = 5
    other = 6


#class GoodsItem:
 #   def __init__(self):
  #      self.id: int = 0
   #     self.product: str = ''
    #    self.department: GoodsDepartment = GoodsDepartment.other

class MarketManager:
    def __init__(self, market: list[dict]):
        self.market = market

    def print_goods(self):
        print('Товары'.center(40, '-'))
        for item in self.market:
            print(item)
        print('-' * 40)

    def print_goods_item_by_id(self, item_id: int):
        print([x for x in self.market if x['id'] == item_id][0])

    def count_goods_in_department(self, department: str):
        print(sum([int(x['count']) for x in self.market if x['department'] == department]))

    def update_goods_item_by_id(self, item_id: int):
        for i in range(len(self.market)):
            if self.market[i]['id'] == item_id:
                for item in list(self.market[i].keys())[1:]:
                    print(f'{item}: ', end='')
                    self.market[i][item] = input().strip()

    def delete_goods_item_by_id(self, item_id: int):
        for i in range(len(self.market)):
            if self.market[i]['id'] == item_id:
                del self.market[i]
                break

    @staticmethod
    def input_int() -> int:
        while True:
            try:
                return int(input())
            except TypeError:
                print('ВВЕДЕНЫ НЕКОРРЕКТНЫЕ ДАННЫЕ')

    def manage(self):
        print('Управление супермаркетом'.center(40, '-'))
        ans = ''
        while ans != '0':
            print('1 - вывод информации о всех товарах, '
                  '2 - вывод информации о товаре по номеру, '
                  '3 - вывод количества товаров в отделе,\n'
                  '4 - обновить информацию о товаре по номеру, '
                  '5 - удалить товар по номеру, '
                  '0 - выход')
            ans = input().strip()
            match ans:
                case '1':
                    self.print_goods()
                case '2':
                    print('ID: ', end='')
                    self.print_goods_item_by_id(self.input_int())
                case '3':
                    print('Отдел: ', end='')
                    department = input().strip()
                    self.count_goods_in_department(department)
                case '4':
                    print('ID: ', end='')
                    self.update_goods_item_by_id(self.input_int())
                case '5':
                    print('ID: ', end='')
                    self.delete_goods_item_by_id(self.input_int())


def main():
    market = [
        {"id": 1, "product": "coca-cola 0.5l", "department": "drinks", 'count': 13},
        {"id": 2, "product": "fanta 0.5l", "department": "drinks", 'count': 24},
        {"id": 3, "product": "milk 1l", "department": "milk", 'count': 30},
        {"id": 4, "product": "milka chocolate", "department": "chocolate", 'count': 56},
        {"id": 5, "product": "tomato", "department": "vegetables_fruits", 'count': 101},
        {"id": 6, "product": "apple", "department": "vegatables_fruits", 'count': 71},
        {"id": 7, "product": "snickers", "department": "snacks", 'count': 73},
        {"id": 8, "product": "chernogolovka 1l", "department": "drinks", 'count': 54},
        {"id": 9, "product": "heinz italian", "department": "sauces", 'count': 37},
        {"id": 10, "product": "soap dove", "department": "other", 'count': 23}
    ]
    market_manager = MarketManager(market)
    market_manager.manage()

main()