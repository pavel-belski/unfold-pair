import random

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
board = []
values = []

# get cards
for x in range(3):
    char1 = abc[random.randint(0, 25)]
    char2 = str(random.randint(0, 9))
    values.append(char1 + char2)
    values.append(char1 + char2)

random.shuffle(values)

#init board
for x in range(2):
    row = []
    for y in range(3):
        row.append(values.pop())

    board.append(row)

for x in range(2):
    row = ''
    for y in range(3):
        row += 'XX '

    print(row)

is_second_unfold = False
game_finished = False
open_cards = []
prev_input_x = None
prev_input_y = None


while True:
    input_pos = input('Select cell in format (row_number column_number)')
    if len(input_pos) != 3 or not input_pos[0].isdigit() or not input_pos[2].isdigit():
        continue

    # let player input values starting from 1, not 0
    input_x = int(input_pos[0]) - 1
    input_y = int(input_pos[2]) - 1

    if [input_x, input_y] in open_cards:
        continue

    if prev_input_x is not None and input_x == prev_input_x and prev_input_y is not None and input_y == prev_input_y:
        continue

    # render board
    for x in range(2):
        row = ''
        for y in range(3):
            if [x, y] in open_cards:
                row += '__ '
                continue

            if (x == input_x and y == input_y) \
                    or (is_second_unfold and x == prev_input_x and y == prev_input_y):
                row += board[x][y] + ' '
            else:
                row += 'XX '

        print(row)

    # check if there is a match
    if is_second_unfold and \
            board[input_x][input_y] == board[prev_input_x][prev_input_y]:

        open_cards.append([input_x, input_y])
        open_cards.append([prev_input_x, prev_input_y])

    if len(open_cards) == 6:
        print('Congratulations! The game is finished.')
        break

    is_second_unfold = not is_second_unfold

    if is_second_unfold:
        prev_input_x = input_x
        prev_input_y = input_y
    # just in case
    else:
        prev_input_x = None
        prev_input_y = None

