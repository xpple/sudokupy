from sudoku_loader import load_sudoku

player_board = []
solution_board = []

dict_position_names = {}
dict_characteristics = {}

# three dimensional array
# sudoku[2] represents the third row
# sudoku[2][3][0] represents the fourth index of the third row
# sudoku[2][3][n] represents whether the fourth index of the third row can contain the number n
# so if sudoku[2][3][5] is False, the fourth index of the third row cannot contain a 5
sudoku = load_sudoku()


# if a cell has an input, set all its booleans to False
def init():
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j][0] != 0:
                for k in range(1, 10):
                    sudoku[i][j][k] = False


def get_row(r):
    row = []
    for i in range(9):
        row.append(sudoku[r][i][0])
    return row


def get_column(c):
    column = []
    for i in range(9):
        column.append(sudoku[i][c][0])
    return column


# get the entries of the box where the row and column intersect
def get_box(row, column):
    row_min = row // 3 * 3
    column_min = column // 3 * 3
    box = []
    for i in range(3):
        for j in range(3):
            box.append(sudoku[row_min + i][column_min + j][0])
    return box


def create_starting_board():
    for i in range(0, 9):
        row = []
        for k in range(0, 9):
            row.append("0")
        player_board.append(row)


def create_dict_position_names():
    for i in range(0, 81):
        if i < 9:
            dict_position_names["A" + str(i + 1)] = i
        elif i > 8 and i < 18:
            dict_position_names["B" + str(i - 8)] = i
        elif i > 17 and i < 27:
            dict_position_names["C" + str(i - 17)] = i
        elif 26 < i < 36:
            dict_position_names["D" + str(i - 26)] = i
        elif 35 < i < 45:
            dict_position_names["E" + str(i - 35)] = i
        elif 44 < i < 54:
            dict_position_names["F" + str(i - 44)] = i
        elif 53 < i < 63:
            dict_position_names["G" + str(i - 53)] = i
        elif 62 < i < 72:
            dict_position_names["H" + str(i - 62)] = i
        elif i > 71:
            dict_position_names["I" + str(i - 71)] = i


def create_characteristics():
    create_characteristics.i = 0
    while create_characteristics.i != 9:
        dict_characteristics[create_characteristics.i] = [add_position_column()]
        create_characteristics.i = create_characteristics.i + 1


def add_position_column():
    if create_characteristics.i == 0 or 9 or 18 or 27 or 36 or 45 or 54 or 63 or 72:
        return [player_board[0], player_board[9], player_board[18], player_board[27], player_board[36],
                player_board[45], player_board[54], player_board[63], player_board[72]]


"""
def add_position_row():

def add_position_grid():
"""


def show_board():
    print(" 2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 ")
    print(" 2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 ")
    print(" 2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 ")
    print("-----------------------")
    print(" 2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 ")
    print(" 2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 ")
    print(" 2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 ")
    print("-----------------------")
    print(" 2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 ")
    print(" 2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 ")
    print(" 2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 " + "| " + "2 " + "2 " + "2 ")


# def choose_difficulty():


# show_board()
create_starting_board()
