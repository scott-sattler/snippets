
class S:
    # backgrounds '__;__;4?'
    # foregrounds '__;3?;__'
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    GREY = 7

    def __init__(self, background, foreground):
        self.bg = background
        self.fg = foreground

    @property
    def c(self):
        return f'00;3{self.fg};4{self.bg}'


if __name__ == '__main__':
    # for i in range(8):
    #     for j in range(8):
    #         text = 'foo'
    #         print(f'\x1b[00;3{i};4{j}m' + str(text) + '\x1b[0m', f'\ti:{i}; j:{j}')
    #     print()

    ctxt = lambda txt='', cc='6;30;41': f'\x1b[{cc}m' + str(txt) + '\x1b[0m'  # noqa


    class Style: RED_BLACK = '6;30;41'; RED = '0;33;31'; YELLOW_BLACK = '5;30;43'  # noqa
    cprint = lambda txt='', code='': print(f'\x1b[{code}m' + str(txt) + '\x1b[0m')  # noqa
    # print(ctxt('PASSED ARGS'))


    # print(ctxt('COLORS', S(S.RED, S.BLACK).c))
    cprint('COLORS', S(S.RED, S.BLACK).c)
