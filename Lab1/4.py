CSI = '\x1b['
COLOR = f'{CSI}47m'
RESET = f'{CSI}0m'

file = open('sequence.txt')
text = file.read().splitlines()
m1 = []
m2 = []
for i in range(len(text)):
    if 0 <= float(text[i]) <= 5:
        m1.append(float(text[i]))
    elif -5 <= float(text[i]) <= 0:
        m2.append(float(text[i]))

file.close()

print(f'|  от 0 до 5   | {COLOR}{' '*(len(m1))}{RESET}  {len(m1)}%')
print(f'|  от 0 до -5  | {COLOR}{' '*(len(m2))}{RESET}  {len(m2)}%')