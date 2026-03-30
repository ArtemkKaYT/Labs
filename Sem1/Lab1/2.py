CSI = '\x1b['
RESET = f'{CSI}0m'
COLOR = f'{CSI}47m'

def rombs(size):
    prob = size//2
    len = 1
    s = 1
    for _ in range(size):
        if s <= size:
            print(f'{RESET}{' '*prob}{COLOR}{' '*len}{RESET}{' '*prob*2}{COLOR}{' '*len}{RESET}')
            prob -= 1
            len += 2
            s += 2
            if s > size:
                prob += 1
                len -= 2
        else:
            prob += 1
            len -= 2
            print(f'{RESET}{' '*prob}{COLOR}{' '*len}{RESET}{' '*prob*2}{COLOR}{' '*len}{RESET}')
            
print(rombs(9))