import sys
import colorama
from colorama import Style, Fore
call_module = False

colorama.init()


def convert_bytes(num):
    """ bytes for humans """

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'BB', 'GEOPBYTE']:
        if num < 1024.0:
            return str(num)+' '+str(x)
        num /= 1024.0


def super_powers(n=int, positive_exponent=int, value=0):
    """ loop power operation then multiply result to value=n """
    i = 1
    super_power = int(n)
    while i < positive_exponent:
        super_power = int(int(super_power) * int(n))
        i += 1
    return int(super_power), int(super_power*value)


if '-h' in sys.argv:
    print('')
    print('    [SUPER POWER BYTES]\n')
    print('        [BYTES]                            super_bytes -b 1')
    print('        [KILOBYTE]      [KB]               super_bytes -k 1')
    print('        [MEGABYTE]      [MB]               super_bytes -m 1')
    print('        [GIGABYTE]      [GB]               super_bytes -g 1')
    print('        [TERABYTE]      [TB]               super_bytes -t 1')
    print('        [PETABYTE]      [PB]               super_bytes -p 1')
    print('        [EXABYTE]       [EB]               super_bytes -e 1')
    print('        [ZETTABYTE]     [ZB]               super_bytes -z 1')
    print('        [YOTTABYTE]     [YB]               super_bytes -y 1')
    print('        [BRONTOBYTE]    [BB]               super_bytes -bb 1')
    print('        [GEOPBYTE]      [GBP]              super_bytes -gpb 1')
    print('')
    print('        [ANY]           super_bytes bytes power quantity')
    print('        [HELP]          -h')
    print('')
    print('        [AUTHOR] Written by Benjamin Jack Cullen.')

elif sys.argv[1] in ['-b', '-k', '-m', '-g', '-t', '-p', '-e', '-z', '-y', '-bb', '-gpb']:

    positive_exponent = 1.0
    idx = 0
    n_ = 0

    if '-b' in sys.argv:
        idx = sys.argv.index('-b')
        n = 0

    elif '-k' in sys.argv:
        idx = sys.argv.index('-k')
        positive_exponent = 1.0

    elif '-m' in sys.argv:
        idx = sys.argv.index('-m')
        positive_exponent = 2.0

    elif '-g' in sys.argv:
        idx = sys.argv.index('-g')
        positive_exponent = 3.0

    elif '-t' in sys.argv:
        idx = sys.argv.index('-t')
        positive_exponent = 4.0

    elif '-p' in sys.argv:
        idx = sys.argv.index('-p')
        positive_exponent = 5.0

    elif '-e' in sys.argv:
        idx = sys.argv.index('-e')
        positive_exponent = 6.0

    elif '-z' in sys.argv:
        idx = sys.argv.index('-z')
        positive_exponent = 7.0

    elif '-y' in sys.argv:
        idx = sys.argv.index('-y')
        positive_exponent = 8.0

    elif '-bb' in sys.argv:
        idx = sys.argv.index('-bb')
        positive_exponent = 9.0

    elif '-gpb' in sys.argv:
        idx = sys.argv.index('-gpb')
        positive_exponent = 10.0

    print('')
    print('    [SUPER POWER BYTES]')
    value = int(sys.argv[idx+1])

    sp = super_powers(n=int(1024), positive_exponent=int(positive_exponent), value=value)
    str_super_power = str(sp[0])
    int_super_power = int(sp[0])
    str_human_super_power = str(convert_bytes(int(int_super_power)))

    if sp[0] <= 1024 and '-b' in sys.argv:
        print('        [BYTES] (' + str('1') + Style.BRIGHT + Fore.CYAN + '^' + Style.RESET_ALL + str(
            positive_exponent) + ') * ' + str(value) + ') = (' + str(convert_bytes(int(value))) + ') = ' + str(
            int(value)) + ' Bytes')
    else:
        print('        [BYTES] (' + str('1024') + Style.BRIGHT + Fore.CYAN + '^' + Style.RESET_ALL + str(
            positive_exponent) + ') * ' + str(value) + ') = (' + str(convert_bytes(int(sp[1]))) + ') = ' + str(
            int(sp[1])) + ' Bytes')


elif sys.argv[1] not in ['-b', '-k', '-m', '-g', '-t', '-p', '-e', '-z', '-y', '-bb', '-gpb'] and len(sys.argv) >= 3:
    print('[where:not_list]')

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

    if sp[0] <= 1024:
        print('        [BYTES] (' + str('1') + Style.BRIGHT + Fore.CYAN + '^' + Style.RESET_ALL + str(
            positive_exponent) + ') * ' + str(value) + ') = (' + str(convert_bytes(int(value))) + ') = ' + str(
            int(value)) + ' Bytes')
    else:
        print('        [BYTES] (' + str('1024') + Style.BRIGHT + Fore.CYAN + '^' + Style.RESET_ALL + str(
            positive_exponent) + ') * ' + str(value) + ') = (' + str(convert_bytes(int(sp[1]))) + ') = ' + str(
            int(sp[1])) + ' Bytes')
print('')
