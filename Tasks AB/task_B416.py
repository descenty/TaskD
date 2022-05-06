"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""

import re

def wiki_function():
    data = []
    with open('data.txt', 'r') as f:
        # Чтение файла
        for line in [x.strip() for x in f]:
            # Непустые строки добавить в список
            if len(line) != 0:
                data.append(line)
    for i in range(len(data)):
        # Оставить только буквы и пробелы
        reg = re.compile('[^a-zA-Z ]')
        data[i] = str(reg.sub('', data[i]))
    # Объединить все строки в одну через пробел
    data = ' '.join(data)
    # Создать словарь вида 'слово' : количество
    dict = {}
    for word in data.split():
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    # Вывести 10 наиболее популярных слов в виде “ 1 place --- sun --- 15 times \n....”
    sortedList = [str(word) + ' ' + str(count) for word, count in sorted(dict.items(), key = lambda item: item[1], reverse=True)][:10]
    counter = 1
    for item in [x.split() for x in sortedList]:
        print('{} place {} {} times'.format(counter, '{:-^10}'.format(item[0]), item[1]))
        counter += 1
        # Заменить их на Python
        data = ' ' + data
        data = data.replace(' {0} '.format(item[0]), ' PYTHON ')
    # Разбитие на строки по максимум 100 символов
    data = data.split()
    splittedData = []
    index = 0
    while len(data) != 0:
        splittedData.append('')
        while len(data) != 0 and len(splittedData[index] + data[0]) < 100:
            if len(splittedData[index]) != 0:
                splittedData[index] += ' '
            splittedData[index] += data[0]
            del data[0]
        splittedData[index] = splittedData[index].strip()
        index += 1
    # Создать новый текстовый файл
    f = open('newFile.txt', 'w')
    for line in splittedData:
        f.write(line + '\n')


# Вызов функции
wiki_function()