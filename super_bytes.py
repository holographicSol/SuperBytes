import sys
import colorama
from colorama import Style, Fore
call_module = False

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


def super_powers(n=int, positive_exponent=int, value=0):

    if positive_exponent != int:
        i = 1
        super_power = int(n)
        while i < positive_exponent:
            super_power = int(int(super_power) * int(n))
            i += 1

        return int(super_power), int(super_power*value)


def module_function(n=int, positive_exponent=int, value=int):
    global call_module
    call_module = True

    return super_powers(n=int(n), positive_exponent=int(positive_exponent), value=0)


if call_module is False:
    allow_bool = False

    if '-h' in sys.argv:
        print('')
        print('    [SUPER BYTES]\n')
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
        print('        [GEOPBYTE]      [GBP]              super_bytes -geopbyte 1')
        print('')
        print('        [ANY]           super_bytes --super-power 1 --positive-exponent 1 --value 1')
        print('        [CONVERT BYTES] super_bytes --human-size 1024')
        print('')
        print('        [HELP]                             -h')
        print('        [AUTHOR] Written by Benjamin Jack Cullen.')

    elif '--human-size' in sys.argv:
        print('')
        print('    [SUPER BYTES]')
        idx = sys.argv.index('--human-size')
        if sys.argv[idx + 1].isdigit():
            num = sys.argv[idx + 1]
            print('        [HUMAN SIZE] ' + str(convert_bytes(int(num))))

    elif '--super-power' in sys.argv:
        print('')
        print('    [SUPER BYTES]')

        idx = sys.argv.index('--super-power')
        if sys.argv[idx + 1]:
            n_ = sys.argv[idx + 1]

            if '--positive-exponent' in sys.argv:
                idx = sys.argv.index('--positive-exponent')
                if sys.argv[idx + 1]:
                    positive_exponent = sys.argv[idx + 1]

                    if '--value' in sys.argv:
                        idx = sys.argv.index('--value')
                        if sys.argv[idx + 1].isdigit():
                            value = int(sys.argv[idx + 1])

                            str_super_power = str(super_powers(n=int(n_), positive_exponent=int(positive_exponent), value=value)[0])
                            int_super_power = int(super_powers(n=int(n_), positive_exponent=int(positive_exponent), value=value)[0])
                            int_multiplied_super_power = int(super_powers(n=int(n_), positive_exponent=int(positive_exponent), value=value)[1])
                            str_human_super_power = str(convert_bytes(int(int_super_power)))

                            print('        [POWER] super_power = (' + str(n_) +Style.BRIGHT+Fore.CYAN + '^'+Style.RESET_ALL + str(int(positive_exponent)) + ') = (' + str_super_power + ' Bytes) = (' + str_human_super_power + ')')
                            if int(value) == int(n_):
                                print('        [MULTIPLIER] (' + str(value) + Style.BRIGHT+Fore.CYAN + '^' + Style.RESET_ALL + '2) = (' + convert_bytes(
                                    int_multiplied_super_power) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')
                            else:
                                print('        [MULTIPLIER] (' + str(value) + Style.BRIGHT+Fore.CYAN + '*' + Style.RESET_ALL + str(int_super_power) + ') = (' + convert_bytes(
                                    int_multiplied_super_power) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')

    elif '-b' in sys.argv:
        print('')
        print('    [SUPER BYTES]')

        positive_exponent = 1.0
        idx = sys.argv.index('-b')
        n_ = int(sys.argv[idx + 1])
        str_super_power = str(super_powers(n=int(n_), positive_exponent=int(positive_exponent), value=1)[0])
        int_super_power = int(super_powers(n=int(n_), positive_exponent=int(positive_exponent), value=1)[0])
        int_multiplied_super_power = int(super_powers(n=int(n_), positive_exponent=int(positive_exponent), value=1)[1])
        str_human_super_power = str(convert_bytes(int(int_super_power)))
        print('        [POWER] super_power = (' + str(n_) +Style.BRIGHT+Fore.CYAN + '^'+Style.RESET_ALL+ str(int(positive_exponent)) + ') = (' + str_super_power + ' Bytes) = (' + str_human_super_power + ')')
        if int(1) == int(n_):
            print('        [MULTIPLIER] (' + str('1') +Style.BRIGHT+Fore.CYAN + '^'+Style.RESET_ALL+'2) = (' + convert_bytes(
                int_multiplied_super_power) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')
        else:
            print('        [MULTIPLIER] (' + str('1') + Style.BRIGHT+Fore.CYAN + '*' + Style.RESET_ALL + str(n_) + ') = (' + convert_bytes(
                int_multiplied_super_power) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')

    else:
        positive_exponent = 0
        n_ = 0

        if '-k' in sys.argv:
            idx = sys.argv.index('-k')
            positive_exponent = 1.0
            n_ = 1024
            allow_bool = True

        elif '-m' in sys.argv:
            idx = sys.argv.index('-m')
            positive_exponent = 1.0
            n_ = 1048576
            allow_bool = True

        elif '-g' in sys.argv:
            idx = sys.argv.index('-g')
            positive_exponent = 1.0
            n_ = 1073741824
            allow_bool = True

        elif '-t' in sys.argv:
            idx = sys.argv.index('-t')
            positive_exponent = 1.0
            n_ = 1099511627776
            allow_bool = True

        elif '-p' in sys.argv:
            idx = sys.argv.index('-p')
            positive_exponent = 1.0
            n_ = 1125899906842624
            allow_bool = True

        elif '-e' in sys.argv:
            idx = sys.argv.index('-e')
            positive_exponent = 1.0
            n_ = 1152921504606846976
            allow_bool = True

        elif '-z' in sys.argv:
            idx = sys.argv.index('-z')
            positive_exponent = 1.0
            n_ = 1180591620717411303424
            allow_bool = True

        elif '-y' in sys.argv:
            idx = sys.argv.index('-y')
            positive_exponent = 1.0
            n_ = 1208925819614629174706176
            allow_bool = True

        elif '-bb' in sys.argv:
            idx = sys.argv.index('-bb')
            positive_exponent = 1.0
            n_ = 1237940039285380274899124224
            allow_bool = True

        elif '-geopbyte' in sys.argv:
            idx = sys.argv.index('-geopbyte')
            positive_exponent = 1.0
            n_ = 1267650600228229401496703205376
            allow_bool = True

        if allow_bool is True:
            print('')
            print('    [SUPER BYTES]')

            value = int(sys.argv[idx + 1])
            str_super_power = str(super_powers(n=int(n_), positive_exponent=int(positive_exponent), value=value)[0])
            int_super_power = int(super_powers(n=int(n_), positive_exponent=int(positive_exponent), value=value)[0])
            int_multiplied_super_power = int(super_powers(n=int(n_), positive_exponent=int(positive_exponent), value=value)[1])
            str_human_super_power = str(convert_bytes(int(int_super_power)))
            print('        [POWER] super_power = (' + str(n_) +Style.BRIGHT+Fore.CYAN + '^'+Style.RESET_ALL + str(int(positive_exponent)) + ') = (' + str_super_power + ' Bytes) = (' + str_human_super_power + ')')
            if int(value) == int(n_):
                print('        [MULTIPLIER] (' + str(value) +Style.BRIGHT+Fore.CYAN + '^'+Style.RESET_ALL+'2) = (' +  str(convert_bytes(int_multiplied_super_power)) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')
            else:
                print('        [MULTIPLIER] (' + str(value) + Style.BRIGHT+Fore.CYAN + '*' + Style.RESET_ALL + str(n_) + ') = (' + str(convert_bytes(int_multiplied_super_power)) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')

    print('')


# example module use
# example_bytes = int(super_powers(n=int(8.0), positive_exponent=int(10.0), value=24)[0])
# example_human_bytes = str(convert_bytes(int(example_bytes)))
# example_multiplied_super_power = int(super_powers(n=int(8.0), positive_exponent=int(10.0), value=24)[1])
# print(str('[BYTES]       ') + str(example_bytes))
# print(str('[HUMAN BYTES] ') + str(example_human_bytes))
# print(str('[MULTIPLIER]  [' + str('24') + ' ' + example_human_bytes.split(' ')[1] + '] ' + str(example_multiplied_super_power)))