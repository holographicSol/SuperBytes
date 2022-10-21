import sys
import colorama
from colorama import Style, Fore
call_module = False

colorama.init()

b_arg = ['-b', '-k', '-m', '-g', '-t', '-p', '-e', '-z', '-y', '-bb', '-gpb']


def convert_bytes(num):
    """ bytes for humans """

    num = 0
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'BB', 'GEOPBYTE']:
        if num <= 1024.0:
            return str(float(num))+' '+str(x)
        num /= 1024.0


def convert_bytes_human(num):
    """ bytes for humans """

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'BB', 'GEOPBYTE']:
        if num < 1024.0:
            return str(num)+' '+x
        elif num >= int(1267650600228229401496703205376*1024):
            return str('[MAX]')

        num /= 1024.0


def super_powers(n=int, positive_exponent=int, value=0):
    """ loop power operation then multiply result to value=n """
    i = 1
    super_power = float(n)
    while i < positive_exponent:
        super_power = float(float(super_power) * float(n))
        i += 1
    return float(super_power), float(super_power*value)


if '-h' in sys.argv:
    print('')
    print('    [SUPER POWER BYTES]\n')
    print('        [BYTES]                            super_bytes 1 1')
    print('        [KILOBYTE]      [KB]               super_bytes 1024 1')
    print('        [MEGABYTE]      [MB]               super_bytes 1024 2')
    print('        [GIGABYTE]      [GB]               super_bytes 1024 3')
    print('        [TERABYTE]      [TB]               super_bytes 1024 4')
    print('        [PETABYTE]      [PB]               super_bytes 1024 5')
    print('        [EXABYTE]       [EB]               super_bytes 1024 6')
    print('        [ZETTABYTE]     [ZB]               super_bytes 1024 7')
    print('        [YOTTABYTE]     [YB]               super_bytes 1024 8')
    print('        [BRONTOBYTE]    [BB]               super_bytes 1024 9')
    print('        [GEOPBYTE]      [GBP]              super_bytes 1024 10')
    print('')
    print('        [ANY]                              super_bytes byte power quantity')
    print('        [HELP]          -h')
    print('')
    print('        [AUTHOR] Written by Benjamin Jack Cullen.')

elif sys.argv[1] in b_arg:
    """ ['-k', '-m', '-g', '-t', '-p', '-e', '-z', '-y', '-bb', '-gpb']: """

    positive_exponent_ = [0.0,
                          1.0, 2.0, 3.0, 4.0, 5.0,
                          6.0, 7.0, 8.0, 9.0, 10]

    positive_exponent = positive_exponent_[0]

    idx = 0
    n_ = 0

    for _ in b_arg:
        if sys.argv[1] == _:
            print('-- matching sys.argv:', _)
            idx = sys.argv.index(_)
    positive_exponent = positive_exponent_[idx]

    print('')
    print('    [SUPER POWER BYTES]')
    value = int(sys.argv[idx+1])

    sp = super_powers(n=int(1024), positive_exponent=int(positive_exponent), value=value)
    str_super_power = str(sp[0])
    int_super_power = int(sp[0])
    str_human_super_power = str(convert_bytes(int(int_super_power)))


elif len(sys.argv) >= 3:
    """ Allow arbitrary bytes, powers, values. """

    print('')
    print('    [SUPER POWER BYTES]')

    n_ = 1
    if sys.argv[1].isdigit():
        n_ = int(sys.argv[1])
    positive_exponent = 1

    if sys.argv[2].isdigit():
        positive_exponent = int(sys.argv[2])

    value = 1
    if len(sys.argv) == 4:
        if sys.argv[3].isdigit():
            value = int(sys.argv[3])

    sp = super_powers(n=int(n_), positive_exponent=int(positive_exponent), value=value)
    str_super_power = str(sp[0])
    int_super_power = int(sp[0])
    str_human_super_power = str(convert_bytes(int(int_super_power)))

    """ Allow if super_powered number seemingly n bytes """
    if sp[0] < 1024:
        str_head = '        [BYTES] (' + str('1') + Style.BRIGHT + Fore.CYAN + '^' + Style.RESET_ALL
        str_ex = str(positive_exponent)
        str_val = ') * ' + str(value) + ') = ('
        str_tails = str(float(value)) + ' * Bytes )'

        print(str_head,
              str_ex,
              str_val,
              str_tails)

    else:
        """ Allow if super_powered number greater than bytes """
        str_head = '        [BYTES] (' + str('1024') + Style.BRIGHT + Fore.CYAN + '^' + Style.RESET_ALL
        str_ex = str(positive_exponent)
        str_val = ') * ' + str(value) + ') = ('
        str_tails = str(int(sp[1])) + ' * Bytes )'

        int_tails = int(int(sp[1]))
        str_human = '        [' + str(convert_bytes_human(int_tails)) + ']'
        print(str_human)

        print(str_head,
              str_ex,
              str_val,
              str_tails)
print('')
