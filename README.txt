[SuperPowers]
	
    A bytes converter toolset to quantify bytes and scaled bytes.


    [SUPER POWER BYTES]

        [BYTES]                            superpowers 1 1 1
        [KILOBYTE]      [KB]               superpowers 1024 1 1
        [MEGABYTE]      [MB]               superpowers 1024 2 1
        [GIGABYTE]      [GB]               superpowers 1024 3 1
        [TERABYTE]      [TB]               superpowers 1024 4 1
        [PETABYTE]      [PB]               superpowers 1024 5 1
        [EXABYTE]       [EB]               superpowers 1024 6 1
        [ZETTABYTE]     [ZB]               superpowers 1024 7 1
        [YOTTABYTE]     [YB]               superpowers 1024 8 1
        [BRONTOBYTE]    [BB]               superpowers 1024 9 1
        [GEOPBYTE]      [GBP]              superpowers 1024 10 1

        [SUPER POWER]   [EXAMPLE]          superpowers 1024 4 1
        [NTH ROOT]      [EXAMPLE]          superpowers 4 1099511627776
        [CONVERT]                          superpowers 1024
        [HELP]          -h

        [AUTHOR] Written by Benjamin Jack Cullen.


[RETURN BYTES] [EXAMPLE] [SUPER POWER]

    [1 BYTE] superpowers 1 1
    [1 BYTE] superpowers 1 1 1
    [2 BYTE] superpowers 2 1
    [2 BYTE] superpowers 2 1
    [3 BYTE] superpowers 3 1
    [3 BYTE] superpowers 3 1
    [1 KB]   superpowers 1024 1
    [1 MB]   superpowers 1024 2
    [1 GB]   superpowers 1024 3
    [1 TB]   superpowers 1024 4
    [1 PB]   superpowers 1024 5
    [1 EB]   superpowers 1024 6
    [1 ZB]   superpowers 1024 7
    [1 YB]   superpowers 1024 8
    [1 BB]   superpowers 1024 9
    [1 GEOBYTE] superpowers 1024 10


[RETURN BYTES] [EXAMPLE]  [ SUPER POWER * QUANTITY ]

    [120 BYTE] superpowers 1 1 120
    [120 KB]   superpowers 1024 1 120
    [120 MB]   superpowers 1024 2 120
    [120 GB]   superpowers 1024 3 120
    [120 TB]   superpowers 1024 4 120
    [120 PB]   superpowers 1024 5 120
    [120 EB]   superpowers 1024 6 120
    [120 ZB]   superpowers 1024 7 120
    [120 YB]   superpowers 1024 8 120
    [120 BB]   superpowers 1024 9 120
    [120 GEOBYTE] superpowers 1024 10 120


[SUPER POWER BYTES] [EXAMPLE] [ INVERSION ]
       
        Step 1. SUPER_POWER = (Nbytes^X) * z)
        
        command: superpowers 1024 10 1

        output: 1267650600228229401496703205376 Bytes


        Step 2. SUPER_ROOT = Invert step 1.
        
        command: super_root_bytes 10 1267650600228229401496703205376

        output: 1024 Bytes

