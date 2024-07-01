def print_board(cells):
    print('\n\n')
    for i in range(len(cells)):
        print(cells[i], end='')
        if i==2 or i==5:
            print('\n-----------\n')
        if i!=2 and i!=5 and i!=8:
            print(' | ', end='')
    print('\n\n')


def check_game(cells):
    for i in cells:
        if i==' ':
            return True
    return False


def game_over(cells):
    if cells[0]==cells[1]==cells[2] and cells[0]!=' ' and cells[1]!=' ' and cells[2]!=' ':
        print(f'{cells[0]} wins!')
        return True
    if cells[3]==cells[4]==cells[5] and cells[3]!=' ' and cells[4]!=' ' and cells[5]!=' ':
        print(f'{cells[3]} wins!')
        return True
    if cells[6]==cells[7]==cells[8] and cells[6]!=' ' and cells[7]!=' ' and cells[8]!=' ':
        print(f'{cells[6]} wins!')
        return True
    if cells[0]==cells[3]==cells[6] and cells[0]!=' ' and cells[3]!=' ' and cells[6]!=' ':
        print(f'{cells[0]} wins!')
        return True
    if cells[1]==cells[4]==cells[7] and cells[1]!=' ' and cells[4]!=' ' and cells[7]!=' ':
        print(f'{cells[1]} wins!')
        return True
    if cells[2]==cells[5]==cells[8] and cells[2]!=' ' and cells[5]!=' ' and cells[8]!=' ':
        print(f'{cells[2]} wins!')
        return True
    if cells[0]==cells[4]==cells[8] and cells[0]!=' ' and cells[4]!=' ' and cells[8]!=' ':
        print(f'{cells[0]} wins!')
        return True
    if cells[2]==cells[4]==cells[6] and cells[2]!=' ' and cells[4]!=' ' and cells[6]!=' ':
        print(f'{cells[2]} wins!')
        return True
    return False

cells = [' ']*(9)
print_board(cells)
pos = int(input('X goes first, where do you want to place it? '))
cells[pos] = 'X'
print_board(cells)

game = True
win = False
curr = 'o'
while game and not win:
    pos = int(input(f'Where do you want to place {curr}? '))
    if cells[pos]!=' ':
        print('Already occupied! Enter again.')
        continue
    cells[pos] = curr
    print_board(cells)
    game = check_game(cells)
    if game_over(cells):
        win = True
    if curr=='o':
        curr='X'
    else:
        curr = 'o'

if not win:
    print('Its a tie!')
print('Game Over!')