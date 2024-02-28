def encode_hex(chars: str) -> str | int:
    if ' ' in chars: return -1
    return '0x' + ''.join([hex(ord(char)).removeprefix('0x') for char in chars])

def decode_hex(hex: str) -> str:
    if hex[0:2] != '0x' or ' ' in hex:
        return -1
    
    hex = hex.removeprefix('0x')
    true_table = '0123456789abcdef'
    value = 0

    for i in range(len(hex)):
        digit_value = true_table.find(hex.lower()[i])
        value += digit_value * (16 ** (len(hex) - i - 1))

    return value

def test_decode_hex():
    for i in range(0, 100000, 7):
        assert decode_hex(hex(i)) == i

if __name__ == '__main__':
    print( encode_hex('Allo') )
    print( decode_hex('0xA') )
    test_decode_hex()