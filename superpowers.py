import sys
import colorama
from colorama import Style, Fore
call_module = False

colorama.init()


def convert_bytes(num):
    """ bytes for humans """

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'BB', 'GEOPBYTES']:

        if num < 1024.0:
            return str(num)+' '+x

        elif num >= int(1024) and str(x) == 'GEOPBYTES':
            return str('MAX] ' + str(x) + ' ' + str(num))

        num /= 1024.0


def super_root(num=int, n=float):
    return float(n) ** (1 / float(num))


def super_powers(n=int, positive_exponent=int, quantity=0):
    """ loop power operation then multiply result to quantity=n """
    i = 1
    super_power = float(n)
    while i < positive_exponent:
        super_power = float(float(super_power) * float(n))
        i += 1
    return float(super_power), float(super_power*quantity)


if '-h' in sys.argv:
    print('')
    print('    [SUPER POWER BYTES]\n')
    print('        [BYTES]                            superpower 1 1 1')
    print('        [KILOBYTE]      [KB]               superpower 1024 1 1')
    print('        [MEGABYTE]      [MB]               superpower 1024 2 1')
    print('        [GIGABYTE]      [GB]               superpower 1024 3 1')
    print('        [TERABYTE]      [TB]               superpower 1024 4 1')
    print('        [PETABYTE]      [PB]               superpower 1024 5 1')
    print('        [EXABYTE]       [EB]               superpower 1024 6 1')
    print('        [ZETTABYTE]     [ZB]               superpower 1024 7 1')
    print('        [YOTTABYTE]     [YB]               superpower 1024 8 1')
    print('        [BRONTOBYTE]    [BB]               superpower 1024 9 1')
    print('        [GEOPBYTE]      [GBP]              superpower 1024 10 1')
    print('')
    print('        [SUPER POWER]   [EXAMPLE]          superpower 1024 4 1')
    print('        [NTH ROOT]      [EXAMPLE]          superpower 4 1099511627776')
    print('        [CONVERT]                          superpower 1024')
    print('        [HELP]          -h')
    print('')
    print('        [AUTHOR] Written by Benjamin Jack Cullen.')


elif len(sys.argv) == 4:
    """ Allow arbitrary bytes, powers, values. """

    print('')
    print('    [SUPER POWER BYTES]')

    # check n
    n_ = 1
    if sys.argv[1].isdigit():
        n_ = int(sys.argv[1])

    # check exponent
    positive_exponent = 1
    if sys.argv[2].isdigit():
        positive_exponent = int(sys.argv[2])

    # check quantity
    quantity = 1.0
    if len(sys.argv) == 4:
        if sys.argv[3].isdigit():
            quantity = int(sys.argv[3])

    # power n by exponent and multiply by quantity
    sp = super_powers(n=int(n_), positive_exponent=int(positive_exponent), quantity=quantity)
    str_super_power = str(sp[0])
    int_super_power = float(sp[0])
    str_human_super_power = str(convert_bytes(float(int_super_power)))

    """ < 1024 """
    if sp[0] < 1024:
        str_head = '        [BYTES] ( ' + str('1') + Style.BRIGHT + Fore.CYAN + ' ^' + Style.RESET_ALL
        str_ex = str(positive_exponent)
        str_val = ') * ' + str(quantity) + ' ) = ('
        ap = ' Byte )'
        if quantity > 1:
            ap = ' Bytes )'
        str_tails = str(int(quantity)) + ap
        str_human = '        [' + str(convert_bytes(quantity)) + ']'
        print(str_human)
        print(str_head,
              str_ex,
              str_val,
              str_tails)

    else:
        """ > 1024 """
        str_head = '        [BYTES] ( ' + str('1024') + Style.BRIGHT + Fore.CYAN + ' ^' + Style.RESET_ALL
        str_ex = str(positive_exponent)
        str_val = ') * ' + str(quantity) + ' ) = ('
        str_tails = str(int(sp[1])) + ' Bytes )'
        int_tails = int(sp[1])
        str_human = '        [' + str(convert_bytes(int_tails)) + ']'
        print(str_human)
        print(str_head,
              str_ex,
              str_val,
              str_tails)

elif len(sys.argv) == 2:
    num = int(str(sys.argv[1]))
    print('')
    print('    [SUPER SIZE BYTES]')
    print('        [SIZE] [' + str(convert_bytes(num)) + ']')

elif len(sys.argv) == 3:
    x = int(str(sys.argv[1]))
    if sys.argv[2].isdigit():
        y = int(str(sys.argv[2]))
        super_root_bytes = float(super_root(num=x, n=float(y)))
        int_super_root_bytes = super_root_bytes
        print('')
        print('    [SUPER ROOT BYTES]')
        print('        [NTH ROOT] [' + str(convert_bytes(float(super_root_bytes))) + ']')
        print('        [BYTES]  (' + (str(int(super_root_bytes)) + ' Bytes)'))
        print('')
    else:
        print('invalid argument characters.')

print('')