def shuffle(table):
    return table[::2] + table[1::2]

if __name__ == '__main__':
    table = [1,2,3,4,5,6,7]
    x = shuffle(table)

    print(x)