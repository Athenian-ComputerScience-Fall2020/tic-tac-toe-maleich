# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.
board = {'tl': ' ', 'tm': ' ', 'tr': ' ',
         'ml': ' ', 'mm': ' ', 'mr': ' ',
         'bl': ' ', 'bm': ' ', 'br': ' '}


def print_board(gb):
    print(gb['tl'] + '|' + gb['tm'] + '|' + gb['tr'])
    print('--' + '+' + '--' + '+' + '--')
    print(gb['ml'] + '|' + gb['mm'] + '|' + gb['mr'])
    print('--' + '+' + '--' + '+' + '--')
    print(gb['bl'] + '|' + gb['bm'] + '|' + gb['br'])


def check_win(gb):
    if gb['tl'] == gb['tm'] == gb['tr'] and gb['tl'] != ' ':    # across top row
        return True
    elif gb['ml'] == gb['mm'] == gb['mr'] and gb['ml'] != ' ':    # across middle row
        return True
    elif gb['bl'] == gb['bm'] == gb['br'] and gb['bl'] != ' ':    # across bottom row
        return True
    elif gb['tl'] == gb['ml'] == gb['bl'] and gb['tl'] != ' ':    # down left column
        return True
    elif gb['tm'] == gb['mm'] == gb['bm'] and gb['tm'] != ' ':    # down middle column
        return True
    elif gb['tr'] == gb['mr'] == gb['br'] and gb['tr'] != ' ':    # down right column
        return True
    elif gb['tl'] == gb['mm'] == gb['br'] and gb['tl'] != ' ':    # upper left to lower right
        return True
    elif gb['tr'] == gb['mm'] == gb['bl'] and gb['tr'] != ' ':    # lower left to upper right
        return True


def player_turn():
    print("hi")


print_board(board)

print("O goes next. Choose a space")
move = input()
board[move] = "O"
print_board(board)
