import json


def load_sudoku():
    with open('sudoku.json') as sudoku_json:
        data = json.load(sudoku_json)
    sudoku = []
    for i in range(len(data["rows"][0])):
        sudoku.append([])
        for j in range(len(data["rows"][0]["row{}".format(i)][0])):
            sudoku[i].append([])
            sudoku[i][j].append(data["rows"][0]["row{}".format(i)][0]["cell{}".format(j)])
            for k in range(9):
                sudoku[i][j].append(True)
    return sudoku
