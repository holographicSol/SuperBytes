import sys
import colorama
from colorama import Style, Fore

colorama.init()


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
    print('    [SUPER SIZE BYTES]\n')
    print('        [CONVERT BYTES] super_size 1024')
    print('        [HELP]                             -h')
    print('        [AUTHOR] Written by Benjamin Jack Cullen.')
    print('')

elif len(sys.argv) == 2:
    x = int(str(sys.argv[1]))
    print('')
    print('    [SUPER SIZE BYTES]')
    print('        [SIZE] ' + str(convert_bytes(x)))
    print('')
