from sudoku_loader import load_sudoku

# three dimensional array
# sudoku[2] represents the third row
# sudoku[2][3][0] represents the fourth index of the third row
# sudoku[2][3][n] represents whether the fourth index of the third row can contain the number n
# so if sudoku[2][3][5] is False, the fourth index of the third row cannot contain a 5
sudoku = load_sudoku()


def init():
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            # if a cell has an input...
            if sudoku[i][j][0] != 0:
                for k in range(9):
                    # ...set all its booleans to False
                    sudoku[i][j][k + 1] = False
                    # ...set the booleans for the input in the entire row to False
                    sudoku[i][k][sudoku[i][j][0]] = False
                    # ...set the booleans for the input in the entire column to False
                    sudoku[k][j][sudoku[i][j][0]] = False
                for k in range(3):
                    for l in range(3):
                        # ...set the booleans for the input in the entire box to False
                        sudoku[i // 3 * 3 + k][j // 3 * 3 + l][sudoku[i][j][0]] = False


def solve():
    # list all the booleans of...
    for i in range(9):
        for j in range(9):
            # ...row i for any input j + 1, if there is only one True...
            if (row_bool := [sudoku[i][k][j + 1] for k in range(9)]).count(True) == 1:
                # ...set the input of row i, where the index is the index(True), to j + 1
                sudoku[i][row_bool.index(True)][0] = j + 1
                update(i, row_bool.index(True), j + 1)
            # if there are two Trues...
            elif row_bool.count(True) == 2:
                # ...check if they are in the same box...
                if (indices := [k for k, l in enumerate(row_bool) if l])[0] // 3 * 3 == indices[1] // 3 * 3:
                    # ...and set the booleans for j + 1 in that box to False
                    for k in range(3):
                        for l in range(3):
                            if i // 3 * 3 + k != i:
                                sudoku[i // 3 * 3 + k][row_bool.index(True) // 3 * 3 + l][j + 1] = False
            # if there are three Trues...
            elif row_bool.count(True) == 3:
                # ...check if they are in the same box...
                if (indices := [k for k, l in enumerate(row_bool) if l])[0] // 3 * 3 == indices[1] // 3 * 3 == indices[2] // 3 * 3:
                    # ...and set the booleans for j + 1 in that box to False
                    for k in range(3):
                        for l in range(3):
                            if i // 3 * 3 + k != i:
                                sudoku[i // 3 * 3 + k][row_bool.index(True) + l][j + 1] = False
            # ...column i for any input j + 1, if there is only one True...
            if (column_bool := [sudoku[k][i][j + 1] for k in range(9)]).count(True) == 1:
                # ...set the input of column i, where the index is the index(True), to j + 1
                sudoku[column_bool.index(True)][i][0] = j + 1
                update(column_bool.index(True), i, j + 1)
            # if there are two Trues...
            elif column_bool.count(True) == 2:
                # ...check if they are in the same box...
                if (indices := [k for k, l in enumerate(column_bool) if l])[0] // 3 * 3 == indices[1] // 3 * 3:
                    # ...and set the booleans for j + 1 in that box to False
                    for k in range(3):
                        for l in range(3):
                            if i // 3 * 3 + l != i:
                                sudoku[column_bool.index(True) // 3 * 3 + k][i // 3 * 3 + l][j + 1] = False
            # if there are three Trues...
            elif column_bool.count(True) == 3:
                # ...check if they are in the same box...
                if (indices := [k for k, l in enumerate(column_bool) if l])[0] // 3 * 3 == indices[1] // 3 * 3 == indices[2] // 3 * 3:
                    # ...and set the booleans for j + 1 in that box to False
                    for k in range(3):
                        for l in range(3):
                            if i // 3 * 3 + l != i:
                                sudoku[column_bool.index(True) + k][i // 3 * 3 + l][j + 1] = False
            # ...the box intersected by i and j for any input j + 1, if there is only one True...
            if (box_bool := [sudoku[i // 3 * 3 + k][j // 3 * 3 + l][j + 1] for k in range(3) for l in range(3)]).count(True) == 1:
                # ...determine the row and column, and set the input to j + 1
                sudoku[i // 3 * 3 + box_bool.index(True) // 3][j // 3 * 3 + box_bool.index(True) % 3][0] = j + 1
                update(i // 3 * 3 + box_bool.index(True) // 3, j // 3 * 3 + box_bool.index(True) % 3, j + 1)
            # if there are two Trues...
            elif box_bool.count(True) == 2:
                # ...check if they are in the same row
                if (indices := [k for k, l in enumerate(box_bool) if l])[0] // 3 == indices[1] // 3:
                    # ...and set the booleans for j + 1 in that row to False
                    for k in range(9):
                        if j // 3 * 3 != k // 3 * 3:
                            sudoku[i // 3 * 3 + box_bool.index(True) // 3][k][j + 1] = False
                # ...check if they are in the same column
                elif indices[0] % 3 == indices[1] % 3:
                    # ...and set the booleans for j + 1 in that column to False
                    for k in range(9):
                        if i // 3 * 3 != k // 3 * 3:
                            sudoku[k][j // 3 * 3 + box_bool.index(True) % 3][j + 1] = False
            # if there are three Trues...
            elif box_bool.count(True) == 3:
                # ...check if they are in the same row
                if (indices := [k for k, l in enumerate(box_bool) if l])[0] // 3 == indices[1] // 3 == indices[2] // 3:
                    # ...and set the booleans for j + 1 in that row to False
                    for k in range(9):
                        if j // 3 * 3 != k // 3 * 3:
                            sudoku[i // 3 * 3 + box_bool.index(True) // 3][k][j + 1] = False
                # ...check if they are in the same column
                elif indices[0] % 3 == indices[1] % 3 == indices[2] % 3:
                    # ...and set the booleans for j + 1 in that column to False
                    for k in range(9):
                        if i // 3 * 3 != k // 3 * 3:
                            sudoku[k][j // 3 * 3 + box_bool.index(True) % 3][j + 1] = False
            # ...the cell intersected by i and j for any input j + 1, if there is only one True...
            if (cell_bool := [sudoku[i][j][k] for k in range(1, 10)]).count(True) == 1:
                # ...set the input of that cell to j + 1
                sudoku[i][j][0] = cell_bool.index(True) + 1
                update(i, j, cell_bool.index(True) + 1)


def update(i, j, value):
    print("Found", value, "at row", i + 1, "column", j + 1)
    # whenever a new input for a cell is found...
    for k in range(9):
        # ...set all its booleans to False
        sudoku[i][j][k + 1] = False
        # ...set the booleans for the input in the entire row to False
        sudoku[i][k][value] = False
        # ...set the booleans for the input in the entire column to False
        sudoku[k][j][value] = False
    for k in range(3):
        for l in range(3):
            # ...set the booleans for the input in the entire box to False
            sudoku[i // 3 * 3 + k][j // 3 * 3 + l][value] = False


def get_unsolved():
    num = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j][0] == 0:
                num += 1
    return num


def print_grid():
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j][0], end="  ")
        print()


init()
# arbitrary range
for _ in range(10):
    solve()

is_valid = lambda data: sum([a for a in map(lambda x: len(set(x)) == 9,
                            data + [[a[i] for a in data] for i in
                            range(9)] + [[data[x * 3 + dx][y * 3 + dy]
                            for dx in range(3) for dy in range(3)]
                            for x in range(3) for y in range(3)])]) == 27
print(is_valid([[sudoku[i][j][0] for i in range(9)] for j in range(9)]))

print_grid()
