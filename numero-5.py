def analyse(words: list[str]) -> dict:
    words_count = {}
    for word in words:
        word = word.lower()
        if word not in words_count.keys():
            words_count[word] = 0
        words_count[word] += 1
    return words_count

def parse_sentence(chars: str) -> list[str]:
    new_string = ''
    for char in chars:
        if char in [',', '.', '!', '?']:
            continue
        new_string += char
    return new_string.split(' ')

def print_repetition(words_count: dict) -> None:
    for key, value in words_count.items():
        print(key, value)


if __name__ == '__main__':
    sentence = 'Salut, la vie est salut'

    x = analyse(parse_sentence(sentence))

    print_repetition(x)