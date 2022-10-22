import sys


def convert_bytes(num):
    """ bytes for humans """

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'BB', 'GEOPBYTES']:

        if num < 1024.0:
            return str(num)+' '+x

        elif num >= int(1024) and str(x) == 'GEOPBYTES':
            return str('MAX] [' + str(x) + ' ' + str(num))

        num /= 1024.0


if '-h' in sys.argv:
    print('')
    print('    [SUPER SIZE BYTES]\n')
    print('        [CONVERT BYTES] super_size 1024')
    print('        [HELP]          -h')
    print('')
    print('        [AUTHOR] Written by Benjamin Jack Cullen.')
    print('')

elif len(sys.argv) == 2:
    num = int(str(sys.argv[1]))
    print('')
    print('    [SUPER SIZE BYTES]')
    print('        [SIZE] [' + str(convert_bytes(num)) + ']')
    print('')
