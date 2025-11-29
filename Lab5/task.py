import re


FILE_1 = 'task1-ru.txt'


def match(pattern, text):
    return re.findall(pattern, text)


with open(FILE_1, encoding='UTF-8') as file:
    text = file.read()
    pattern_1 = r'рис\.\s*\d+'
    pattern_2 = r'\b[A-Za-zА-Яа-я]{4}\b'
    res = match(pattern_1, text) + match(pattern_2, text)
    print(len(res))

