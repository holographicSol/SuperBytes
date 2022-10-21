import sys
import colorama
from colorama import Style, Fore

colorama.init()


def super_root(num=int, n=float):
    return float(n) ** (1 / float(num))


def convert_bytes(num):
    """ bytes for humans """

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'BB', 'GEOPBYTE']:
        if num < 1024.0:
            return str(num)+' '+x
        elif num == int(1024*1267650600228229401496703205376):
            return str(num) + ') = (GEOPBYTE' + Style.BRIGHT + Fore.CYAN + '*' + Style.RESET_ALL + '1024'
        elif num > int(1024*1267650600228229401496703205376):
            return str(num) + ') = (GEOPBYTE' + Style.BRIGHT + Fore.CYAN + '*' + Style.RESET_ALL + '1024' + Style.BRIGHT + Fore.CYAN + '+!' + Style.RESET_ALL
        num /= 1024.0


if '-h' in sys.argv:
    print('')
    print('    [SUPER ROOT BYTES]\n')
    print('        [N ROOT]     super_root_bytes nth_root n')
    print('        [HELP]       -h')
    print('        [AUTHOR]     Written by Benjamin Jack Cullen.')
    print('')

elif len(sys.argv) == 3:
    x = int(str(sys.argv[1]))
    if sys.argv[2].isdigit():
        y = int(str(sys.argv[2]))
        super_root_bytes = float(super_root(num=x, n=float(y)))
        int_super_root_bytes = super_root_bytes
        print('')
        print('    [SUPER ROOT BYTES]')
        print('        [SUPER ROOT BYTES] (' + str(x) + Style.BRIGHT + Fore.CYAN + str('√') + Style.RESET_ALL + str(y) + ' Bytes) = (' + str(x) + Style.BRIGHT + Fore.CYAN + str('√') + Style.RESET_ALL + str(convert_bytes(float(y))) + ') = (' + str(convert_bytes(round(int_super_root_bytes))) + ')')
        print('        [PRECISION BYTES]  (' + (str(super_root_bytes) + ' Bytes)'))
        print('')
    else:
        print('invalid argument characters.')
else:
    print('invalid argument characters.')
