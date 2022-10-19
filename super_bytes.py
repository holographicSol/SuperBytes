import sys
import colorama
from colorama import Style, Fore
call_module = False

colorama.init()


def convert_bytes(num):
    """ bytes for humans """

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if num < 1024.0:
            return str(num)+' '+x
        num /= 1024.0


def super_powers(n=float, positive_exponent=float, value=0):

    if positive_exponent != int:
        i = 1
        n_power = float(n)
        while i < positive_exponent:
            n_power = float(float(n_power) * float(n))
            i += 1

        return float(n_power), float(n_power*value)


def module_function(n=float, positive_exponent=float, value=int):
    global call_module
    call_module = True

    return super_powers(n=float(n), positive_exponent=float(positive_exponent), value=0)


if call_module is False:
    print('')
    print('[SUPER BYTES]')

    allow_bool = False

    if '--human-size' in sys.argv:
        idx = sys.argv.index('--human-size')
        if sys.argv[idx + 1].isdigit():
            num = sys.argv[idx + 1]
            print('    [HUMAN SIZE] ' + str(convert_bytes(int(num))))

    elif '--super-power' in sys.argv:
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

                            str_super_power = str(super_powers(n=float(n_), positive_exponent=float(positive_exponent), value=value)[0])
                            int_super_power = float(super_powers(n=float(n_), positive_exponent=float(positive_exponent), value=value)[0])
                            int_multiplied_super_power = float(super_powers(n=float(n_), positive_exponent=float(positive_exponent), value=value)[1])
                            str_human_super_power = str(convert_bytes(int(int_super_power)))

                            print('    [POWER] n_power = (' + str(n_) +Style.BRIGHT+Fore.CYAN + '^'+Style.RESET_ALL + str(positive_exponent) + ') = (' + str_super_power + ' Bytes) = (' + str_human_super_power + ')')
                            if int(value) == int(n_):
                                print('    [MULTIPLIER] (' + str(value) + Style.BRIGHT+Fore.CYAN + '^' + Style.RESET_ALL + '2) = (' + convert_bytes(
                                    int_multiplied_super_power) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')
                            else:
                                print('    [MULTIPLIER] (' + str(value) + Style.BRIGHT+Fore.CYAN + '*' + Style.RESET_ALL + str(int_super_power) + ') = (' + convert_bytes(
                                    int_multiplied_super_power) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')
                            print('')

    elif '-b' in sys.argv:
        positive_exponent = 1.0
        idx = sys.argv.index('-b')
        n_ = int(sys.argv[idx + 1])
        str_super_power = str(super_powers(n=float(n_), positive_exponent=float(positive_exponent), value=1)[0])
        int_super_power = float(super_powers(n=float(n_), positive_exponent=float(positive_exponent), value=1)[0])
        int_multiplied_super_power = float(super_powers(n=float(n_), positive_exponent=float(positive_exponent), value=1)[1])
        str_human_super_power = str(convert_bytes(int(int_super_power)))
        print('    [POWER] n_power = (' + str(n_) +Style.BRIGHT+Fore.CYAN + '^'+Style.RESET_ALL+ str(positive_exponent) + ' = (' + str_super_power + ' Bytes) = (' + str_human_super_power + ')')
        if int(1) == int(n_):
            print('    [MULTIPLIER] (' + str(1) +Style.BRIGHT+Fore.CYAN + '^'+Style.RESET_ALL+'2) = (' + convert_bytes(
                int_multiplied_super_power) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')
        else:
            print('    [MULTIPLIER] (' + str(1) + Style.BRIGHT+Fore.CYAN + '*' + Style.RESET_ALL + str(n_) + ') = (' + convert_bytes(
                int_multiplied_super_power) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')
        print('')

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

        if allow_bool is True:

            value = int(sys.argv[idx + 1])
            str_super_power = str(super_powers(n=float(n_), positive_exponent=float(positive_exponent), value=value)[0])
            int_super_power = float(super_powers(n=float(n_), positive_exponent=float(positive_exponent), value=value)[0])
            int_multiplied_super_power = float(super_powers(n=float(n_), positive_exponent=float(positive_exponent), value=value)[1])
            str_human_super_power = str(convert_bytes(int(int_super_power)))
            print('    [POWER] n_power = (' + str(n_) +Style.BRIGHT+Fore.CYAN + '^'+Style.RESET_ALL + str(positive_exponent) + ')  = (' + str_super_power + ' Bytes) = (' + str_human_super_power + ')')
            if int(value) == int(n_):
                print('    [MULTIPLIER] (' + str(value) +Style.BRIGHT+Fore.CYAN + '^'+Style.RESET_ALL+'2) = (' +  convert_bytes(int_multiplied_super_power) + ') = (' + str(int_multiplied_super_power) + ') Bytes')
            else:
                print('    [MULTIPLIER] (' + str(value) + Style.BRIGHT+Fore.CYAN + '*' + Style.RESET_ALL + str(n_) + ') = (' + convert_bytes(int_multiplied_super_power) + ') = (' + str(int_multiplied_super_power) + ' Bytes)')
            print('')

    print('')


# example module use
# example_bytes = float(super_powers(n=float(8.0), positive_exponent=float(10.0), value=24)[0])
# example_human_bytes = str(convert_bytes(int(example_bytes)))
# example_multiplied_super_power = float(super_powers(n=float(8.0), positive_exponent=float(10.0), value=24)[1])
# print(str('[BYTES]       ') + str(example_bytes))
# print(str('[HUMAN BYTES] ') + str(example_human_bytes))
# print(str('[MULTIPLIER]  [' + str('24') + ' ' + example_human_bytes.split(' ')[1] + '] ' + str(example_multiplied_super_power)))