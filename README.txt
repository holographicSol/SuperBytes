[SuperPowerBytes]

    [SUPER POWER BYTES]

        [BYTES]                            super_bytes -b 1
        [KILOBYTE]      [KB]               super_bytes -k 1
        [MEGABYTE]      [MB]               super_bytes -m 1
        [GIGABYTE]      [GB]               super_bytes -g 1
        [TERABYTE]      [TB]               super_bytes -t 1
        [PETABYTE]      [PB]               super_bytes -p 1
        [EXABYTE]       [EB]               super_bytes -e 1
        [ZETTABYTE]     [ZB]               super_bytes -z 1
        [YOTTABYTE]     [YB]               super_bytes -y 1
        [BRONTOBYTE]    [BB]               super_bytes -bb 1
        [GEOPBYTE]      [GBP]              super_bytes -gpb 1

        [ANY]           super_bytes bytes power quantity

        [HELP]                             -h
        [AUTHOR] Written by Benjamin Jack Cullen.


[SuperRootBytes]

    [SUPER ROOT BYTES]

        [N ROOT]     super_root_bytes nth_root n
        [HELP]       -h
        [AUTHOR]     Written by Benjamin Jack Cullen


[SuperSizeBytes]

    [SUPER SIZE BYTES]

        [CONVERT BYTES] super_size 1024
        [HELP]                             -h
        [AUTHOR] Written by Benjamin Jack Cullen.


[NOTES]
	
    A bytes converter toolset to quantify bytes and scaled bytes.


[EXAMPLE] Scaling 1.

    [1 BYTE] super_power_bytes 1 1
    [2 BYTE] super_power_bytes 2 1
    [3 BYTE] super_power_bytes 3 1
    [1 KB]   super_power_bytes 1024 1
    [1 MB]   super_power_bytes 1024 2
    [1 GB]   super_power_bytes 1024 3
    [1 TB]   super_power_bytes 1024 4
    [1 PB]   super_power_bytes 1024 5
    [1 EB]   super_power_bytes 1024 6
    [1 ZB]   super_power_bytes 1024 7
    [1 YB]   super_power_bytes 1024 8
    [1 BB]   super_power_bytes 1024 9
    [1 GEOBYTE]   super_power_bytes 1024 10


[EXAMPLE] Scaling 2 - Scaling with Quantity.

    [120 BYTE] super_power_bytes 1 1 120
    [120 KB]   super_power_bytes 1024 1 120
    [120 MB]   super_power_bytes 1024 2 120
    [120 GB]   super_power_bytes 1024 3 120
    [120 TB]   super_power_bytes 1024 4 120
    [120 PB]   super_power_bytes 1024 5 120
    [120 EB]   super_power_bytes 1024 6 120
    [120 ZB]   super_power_bytes 1024 7 120
    [120 YB]   super_power_bytes 1024 8 120
    [120 BB]   super_power_bytes 1024 9 120
    [120 GEOBYTE]   super_power_bytes 1024 10 120