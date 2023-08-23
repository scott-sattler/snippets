for i in range(101):
    print(f'{i:<3}', str(f'\x1b[{str(i)}m' + 'ABCDEF' + '\x1b[0m'))