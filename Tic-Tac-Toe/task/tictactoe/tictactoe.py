symbols = ['_' for x in range(9)]

field = [[symbols[0], symbols[1], symbols[2]], [symbols[3], symbols[4], symbols[5]],
         [symbols[6], symbols[7], symbols[8]]]


def print_field():
    print(f'''---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------''')


def check_wins():
    global symbols
    symbols = ''.join([y for x in field for y in x])
    wins = [symbols[0:3], symbols[3:6], symbols[6:9],
            symbols[::3], symbols[1::3], symbols[2::3],
            symbols[::4], symbols[2:7:2]]
    if 'XXX' not in wins and 'OOO' not in wins and '_' not in symbols:
        print('Draw')
    elif 'XXX' in wins:
        print('X wins')
    elif 'OOO' in wins:
        print('O wins')
    elif '_' in symbols:
        return True
    return False


print_field()
i = -1
j = -1
check = 0
whose_turn = 'O'

while check_wins():
    coordinates = input('Enter the coordinates: > ').split()
    for XorY in range(2):
        if coordinates[XorY].isdecimal():
            if 0 < int(coordinates[XorY]) <= 3:
                if XorY == 0:
                    j = int(coordinates[XorY]) - 1
                elif XorY == 1:
                    i = 3 - int(coordinates[XorY])
                    if field[i][j] == '_':
                        if whose_turn == 'O':
                            whose_turn = 'X'
                        else:
                            whose_turn = 'O'
                        field[i][j] = whose_turn
                    else:
                        print('This cell is occupied! Choose another one!')
                        break
            else:
                print('Coordinates should be from 1 to 3!')
                break
        else:
            print('You should enter numbers!')
            break
    print_field()
