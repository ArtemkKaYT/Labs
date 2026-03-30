CSI = '\x1b['
RESET = f'{CSI}0m'
COLOR = f'{CSI}47m'

def f(x):
    y = x+1
    prob = y-1
    for _ in range(y):
        print(f'{RESET}|{' '*prob}{COLOR}{' '}{RESET}')
        prob -= 1
    
    print('|' + '_'*y)

print(f(7))