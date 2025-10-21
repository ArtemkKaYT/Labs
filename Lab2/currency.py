from xml.dom import minidom

def parse(xml_file):
    data = minidom.parse(xml_file)
    valutes = data.getElementsByTagName('Valute')
    for string in valutes:
        char_code = string.getElementsByTagName('CharCode')[0].firstChild.nodeValue
        nominal = string.getElementsByTagName('Nominal')[0].firstChild.nodeValue
        print(f'{char_code} - {nominal}')

if __name__ == '__main__':
    with open('currency.xml', encoding='windows-1251') as xml_file:
        parse(xml_file)