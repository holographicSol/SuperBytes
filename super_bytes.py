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
    print('        [BYTES]                            super_power_bytes 1 1')
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


elif len(sys.argv) >= 3:
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
print('')
