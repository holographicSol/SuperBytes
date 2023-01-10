import datetime
import sys
import colorama
from colorama import Style, Fore
import timeit
import time
call_module = False

colorama.init()


def convert_bytes(num):
    """ bytes for humans """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'BB', 'GEOPBYTES']:
        if num < 1024:
            return str(num)+' '+x
        elif num >= int(1024) and str(x) == 'GEOPBYTES':
            return str(Style.BRIGHT + Fore.CYAN + 'OVER-MAX' + Style.RESET_ALL)
        num //= 1024


def super_root(num=float, n=float):
    return float(n) ** (1 / float(num))


def super_powers(n=float, positive_exponent=float, quantity=0):
    """ loop power then multiply result by quantity """

    i = 1
    super_power = int(n)
    while i < positive_exponent:
        super_power = int(int(super_power) * int(n))
        i += 1
    return int(super_power), int(super_power*quantity)


def func_help():
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
    print('        [GEOPBYTE]      [GPB]              superpower 1024 10 1')
    print('')
    print('        [SUPER POWER]   [EXAMPLE]          superpower 1024 4 1')
    print('        [NTH ROOT]      [EXAMPLE]          superpower 4 1099511627776')
    print('        [CONVERT]                          superpower 1024')
    print('        [HELP]                             -h')
    print('')
    print('        [AUTHOR] Written by Benjamin Jack Cullen.')


if '-h' in sys.argv:
    func_help()

elif len(sys.argv) == 4:
    """ Allow arbitrary bytes, powers, values. """

    print('')
    print('    [SUPER POWER BYTES]')
    start_time = str(time.time())

    # n
    n_ = 1
    if sys.argv[1].isdigit():
        n_ = int(sys.argv[1])

    # exponent
    positive_exponent = 1
    if sys.argv[2].isdigit():
        positive_exponent = int(sys.argv[2])

    # quantity
    quantity = 1.0
    if len(sys.argv) == 4:
        if sys.argv[3].isdigit():
            quantity = int(sys.argv[3])

    # super power = (( n ^ x ) * quantity)
    sp = super_powers(n=int(n_), positive_exponent=int(positive_exponent), quantity=quantity)
    str_super_power = str(sp[0])
    int_super_power = int(sp[0])
    str_human_super_power = str(convert_bytes(int(int_super_power)))

    """ SUPER_POWER_RESULT < 1024 """
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
        print('    [TIME] ' + str(float(float(time.time()) - float(start_time))))

    else:
        """ SUPER_POWER_RESULT  > 1024 """
        str_head = '        [BYTES] ( ' + str(n_) + Style.BRIGHT + Fore.CYAN + ' ^' + Style.RESET_ALL
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
        print('        [TIME] ' + str(float(float(time.time()) - float(start_time))))

elif len(sys.argv) == 3:
    start_time = str(time.time())

    x = 1
    y = 1
    if sys.argv[1].isdigit():
        x = int(str(sys.argv[1]))
    if sys.argv[2].isdigit():
        y = int(str(sys.argv[2]))
    super_root_bytes = float(super_root(num=x, n=float(y)))
    int_super_root_bytes = super_root_bytes
    print('')
    print('    [SUPER ROOT BYTES]')
    print('        [NTH ROOT] [' + str(convert_bytes(float(super_root_bytes))) + ']')
    print('        [BYTES]  (' + (str(int(super_root_bytes)) + ' Bytes)'))
    print('        [TIME] ' + str(float(float(time.time()) - float(start_time))))

elif len(sys.argv) == 2:
    """ SUPER SIZE """

    start_time = str(time.time())

    num = 1
    if sys.argv[1].isdigit():
        num = int(str(sys.argv[1]))
    print('')
    print('    [SUPER SIZE BYTES]')
    print('        [SIZE] [' + str(convert_bytes(num)) + ']')
    print('        [TIME] ' + str(float(float(time.time()) - float(start_time))))

else:
    func_help()
print('')
