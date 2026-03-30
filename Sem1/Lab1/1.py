CSI = '\x1b['
RESET = f'{CSI}0m'

GREEN = f'{CSI}42m'
RED = f'{CSI}41m'
YELLOW = f'{CSI}43m'

flag_size = 4
for i in range(flag_size):
    if i <= 1:
        print(f'{GREEN}      {YELLOW}         {RESET}')
    else:
        print(f'{GREEN}      {RED}         {RESET}')