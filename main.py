from sudoku import Sudoku
import json


def main():
    with open("sudoku.json", 'r') as file:
        data = json.load(file)
        sudoku = Sudoku.from_json(data)
        for _ in range(5):
            sudoku.solve_logic()
        sudoku.print()


if __name__ == '__main__':
    main()
