def rotation_gauche(table):
    first_element = table[0]
    for i in range(len(table)-1):
        table[i] = table[i+1]
    table[-1] = first_element
    return table

def rotation_droite(table):
    last_element = table[-1]
    for i in range(len(table)-1, 0, -1):
        table[i] = table[i-1]
    table[0] = last_element
    return table

if __name__ == '__main__':
    tablex = [1,2,3,4,5,6,7]
    left = rotation_gauche(tablex.copy())
    right = rotation_droite(tablex.copy())

    print(left, right)