import re
import csv


FILE_1 = 'task1-ru.txt'
FILE_2 = 'task2.html'
FILE_3 = 'task3.txt'
FILE_4 = 'task_add.txt'
FILE_OUTPUT = 'task_3.csv'


def match(pattern, text):
    return re.findall(pattern, text)


with open(FILE_1, encoding='UTF-8') as file:
    text = file.read()
    pattern_fig = r'[Рр]ис\.\s*\d+'
    pattern_word = r'\b[A-Za-zА-Яа-я]{4}\b'
    figs = match(pattern_fig, text)
    words = match(pattern_word, text)

    print(f'Задание 1:\n{figs}\n{words}\n')

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
    pattern_ID = r'(?!\d{4}-)\b\d+\b(?<!\d{2}-\d{2})'
    pattern_name = r'(?<![A-Za-z0-9._@:/-])\b[A-Za-z]+\b(?![A-Za-z0-9._@:/-])'
    pattern_mail = r'\b\w+@[A-Za-z-_]+\.\w+\b'
    pattern_date = r'\b\d{4}-\d{2}-\d{2}\b'
    pattern_site = r'https?:\/\/[^\s]+?\/'
    Id = match(pattern_ID, text)
    names = match(pattern_name, text)
    mails = match(pattern_mail, text)
    dates = match(pattern_date, text)
    sites = match(pattern_site, text)

    output = []
    for i in range(len(Id)):
        output.append([Id[i], names[i], mails[i], dates[i], sites[i]])
    with open(FILE_OUTPUT, 'w', newline='', encoding='UTF-8') as file_output:
        writer = csv.writer(file_output)
        writer.writerow(['ID', 'Name', 'Mail', 'Date', 'Site'])
        writer.writerows(output)

with open(FILE_4, encoding='UTF-8') as file:
    text = file.read()
    pattern_date = r'\d{2,4}(?:-|\.|\/)\d{2,4}(?:-|\.|\/)\d{2,4}'
    pattern_mail = r'\b\w+@[A-Za-z]+\.[A-Za-z]+\b'
    pattern_site = r'\bhttps?:\/\/[A-Za-z]+\.[A-Za-z]+'
    dates = match(pattern_date, text)
    mails = match(pattern_mail, text)
    sites = match(pattern_site, text)
    
    print(f'\nДополнительное задание')
    print(f'{dates}\n{mails}\n{sites}')
