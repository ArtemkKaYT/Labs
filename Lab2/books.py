import csv

def count(books):
    counter = 0
    reader = csv.DictReader(books, delimiter=";")
    for row in reader:
        if len(row['Название']) > 30:
            counter += 1
    print(counter)
    
def search(books):
    el = True
    reader = csv.DictReader(books, delimiter=";")
    author = input('Введите имя автора: ').lower()
    for row in reader:
        if (row['Дата поступления'][6:10] == '2015' or row['Дата поступления'][6:10] == '2018') and\
            author in row['Автор'].lower():
                print(f'{row['Автор (ФИО)']} - {row['Название']}')
                el = False
    if el == True:
        print('Not found')

def generator(books):
     reader = csv.DictReader(books, delimiter=";")
     number = 1
     for row in reader:
          if number <= 20:
               print(f'{number}. {row['Автор (ФИО)']} - {row['Название']} - {row['Дата поступления'][6:10]} год')
               number += 1

if __name__ == '__main__':
     with open('books.csv', encoding="windows-1251") as books:
        #count(books)
        #search(books)
        generator(books)