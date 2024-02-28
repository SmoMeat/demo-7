def capitalize(chars: str) -> str:
    if len(chars) == 0: return ''
    return chars[0].upper() + chars[1:]

if __name__ == '__main__':
    print( capitalize('allo') )