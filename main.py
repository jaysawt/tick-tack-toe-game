import random


def example_position():
    example = [' ', '1', ' ', '|', ' ', '2', ' ', '|', ' ', '3', ' ', '\n',
               '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '\n',
               ' ', '4', ' ', '|', ' ', '5', ' ', '|', ' ', '6', ' ', '\n',
               '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '\n',
               ' ', '7', ' ', '|', ' ', '8', ' ', '|', ' ', '9', ' ']

    for i in example:
        print(i, end='')
    print("\nPlease note the positions to place X and O's\n")


def show_xo(xo):
    global playerX_score, playerO_score, tie_score
    for j in xo:
        print(j, end='')


def place(box, position, value):
    try:
        box_pos = positions[position]
    except KeyError as e:
        print('You have entered position that does not exist, You have lost your chance')
    else:
        if box[box_pos] == ' ':
            box[box_pos] = value
        else:
            print('You have entered wrong position, You have lost your chance')


def check(XO, value):
    # {'1': 1, '2': 5, '3': 9, '4': 25, '5': 29, '6': 33, '7': 49, '8': 53, '9': 57}
    global playerX_score, playerO_score, tie_score
    if XO[1] == XO[5] == XO[9] == value or XO[25] == XO[29] == XO[33] == value or XO[49] == XO[53] == XO[57] == value:
        print(f'\nPlayer {value} wins!!!!!')
        if value == 'X':
            playerX_score += 1
        else:
            playerO_score += 1
        return True
    elif XO[1] == XO[25] == XO[49] == value or XO[5] == XO[29] == XO[53] == value or XO[9] == XO[33] == XO[57] == value:
        print(f'\nPlayer {value} wins!!!!!')
        if value == 'X':
            playerX_score += 1
        else:
            playerO_score += 1
        return True
    elif XO[1] == XO[29] == XO[57] == value or XO[9] == XO[29] == XO[49] == value:
        print(f'\nPlayer {value} wins!!!!!')
        if value == 'X':
            playerX_score += 1
        else:
            playerO_score += 1
        return True
    elif XO[1] != ' ' and XO[5] != ' ' and XO[9] != ' ' and XO[25] != ' ' and XO[29] != ' ' and XO[33] != ' ' and XO[49] != ' ' and XO[53] != ' ' and XO[57] != ' ':
        print("\nIt's a Tie")
        tie_score += 1
        return True
    else:
        return False


def play(player):
    game_over = False
    X_O = [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\n',
           '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '\n',
           ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\n',
           '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '\n',
           ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']
    while not game_over:
        player1 = input('\nPlayer X turn. Which box position would you like to insert x?: ')
        place(X_O, player1, 'X')
        show_xo(X_O)
        game_over = check(X_O, 'X')
        print(f'\n Player X :{playerX_score}     Tie:{tie_score}      Player O:{playerO_score}')
        if game_over:
            break
        if player == '1':
            player2 = input('\nPlayer O turn. Which box position would you like to insert o?: ')
            place(X_O, player2, 'O')
            show_xo(X_O)
            game_over = check(X_O, 'O')
            print(f'\n Player X :{playerX_score}     Tie:{tie_score}      Player O:{playerO_score}')
        else:
            entered = False
            while not entered:
                random_positions = random.choice(list(positions.values()))
                if X_O[random_positions] == ' ':
                    X_O[random_positions] = 'O'
                    entered = True
            show_xo(X_O)
            game_over = check(X_O, 'O')
            print(f'\n Player X :{playerX_score}     Tie:{tie_score}      Player O:{playerO_score}')


def play_game(opp):
    game_end = False
    while not game_end:
        example_position()
        play(opp)
        cont = input('Enter "any key" to play again or Type "q" to quit\n')
        if cont.lower() == 'q':
            game_end = True


print('Welcome to the game of tic-tac-toe')
print('''╔╦╗┬┌─┐┬┌─  ╔╦╗┌─┐┌─┐┬┌─  ╔╦╗┌─┐┌─┐
 ║ ││  ├┴┐───║ ├─┤│  ├┴┐───║ │ │├┤
 ╩ ┴└─┘┴ ┴   ╩ ┴ ┴└─┘┴ ┴   ╩ └─┘└─┘''')
positions = {'1': 1, '2': 5, '3': 9, '4': 25, '5': 29, '6': 33, '7': 49, '8': 53, '9':  57}
playerX_score = 0
tie_score = 0
playerO_score = 0
global opponent
game_type = True
while game_type:
    opponent = input('Enter 1 to play with a friend or Enter 2 to play with Computer\n')
    if opponent == str(1):
        game_type = False
    elif opponent == str(2):
        game_type = False
    else:
        print('You have entered wrong input, Please enter correctly')
play_game(opponent)

