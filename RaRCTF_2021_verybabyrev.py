import string

data = [
0x45481d1217111313,
0x095f422c260b4145,
0x541b56563d6c5f0b,
0x585c0b3c2945415f,
0x402a6c54095d5f00,
0x4b5f4248276a0606,
0x6c5e5d432c2d4256,
0x6b315e434707412d,
0x5e54491c6e3b0a5a,
0x2828475e05342b1a,
0x060450073b26111f,
0x0a774803050b0d04
]

rawdata = b''

# reverse bytes in data in little endian order
for n in data:
    rawdata += n.to_bytes(8, 'little')

# the first character of flag is r
flag = 'r'

# printable chars requipment to find next char of flag
printable = string.printable

# the next character formula
# prev_char ^ next_char must be equal to hex number from data
for i in range(0, len(rawdata)):
    for char in printable:
        if (ord(flag[i]) ^ ord(char)) == rawdata[i]:
            flag += char

print(flag)
