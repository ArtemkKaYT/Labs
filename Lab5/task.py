import re


FILE_1 = 'task1-ru.txt'
FILE_2 = 'task2.html'
FILE_3 = 'task3.txt'


def match(pattern, text):
    return re.findall(pattern, text)


def iter(pattern, text):
    return re.finditer(pattern, text)


with open(FILE_1, encoding='UTF-8') as file:
    text = file.read()
    pattern_1 = r'[Рр]ис\.\s*\d+'
    pattern_2 = r'\b[A-Za-zА-Яа-я]{4}\b'
    res = match(pattern_1, text) + match(pattern_2, text)
    print('Задание 1:', len(res))

with open(FILE_2, encoding='UTF-8') as file:
    text = file.read()
    pattern_font = r"font-family:\s*'(.+)';"
    pattern_style = r"font-style:\s*(.+);"
    pattern_weight = r"font-weight:\s*(.+);"
    fonts = match(pattern_font, text)
    styles = match(pattern_style, text)
    weight = match(pattern_weight, text)
    print('Задание 2:')
    for i in range(len(fonts)):
        print(f'{fonts[i]} - {styles[i]}, {weight[i]}')

with open(FILE_3, encoding='UTF-8') as file:
    text = file.read()
