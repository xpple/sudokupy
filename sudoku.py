from shapes.box import Box
from cell import Cell
from shapes.column import Column
from shapes.row import Row


class Sudoku:
    def __init__(self, rows: list[Row], columns: list[Column], boxes: list[Box]):
        self.rows = rows
        self.columns = columns
        self.boxes = boxes

    @classmethod
    def from_rows(cls, rows: list[Row]):
        columns = []
        boxes = []
        for n in range(9):
            columns.append(Column(n, []))
            boxes.append(Box(n, []))
        for row in rows:
            for cell in row.cells:
                columns[cell.column_index].cells.append(cell)
                boxes[cell.box_index].cells.append(cell)

        return cls(rows, columns, boxes)

    @classmethod
    def from_columns(cls, columns: list[Column]):
        rows = []
        boxes = []
        for m in range(9):
            rows.append(Row(m, []))
            boxes.append(Box(m, []))
        for column in columns:
            for cell in column.cells:
                rows[cell.row_index].cells.append(cell)
                boxes[cell.box_index].cells.append(cell)

        return cls(rows, columns, boxes)

    @classmethod
    def from_json(cls, json):
        match json["data_type"]:
            case "rows":
                rows = []
                for m in range(9):
                    rows.append(Row(m, []))
                    for n in range(9):
                        rows[m].cells.append(Cell(m, n, m // 3 * 3 + n // 3, json["data"][m][n]))
                return Sudoku.from_rows(rows)
            case "columns":
                columns = []
                for n in range(9):
                    columns.append(Column(n, []))
                    for m in range(9):
                        columns[m].cells.append(Cell(m, n, m // 3 * 3 + n // 3, json["data"][m][n]))
                return Sudoku.from_columns(columns)
            case _:
                raise IOError

    def print(self):
        for row in self.rows:
            for cell in row.cells:
                print(0 if cell.value is None else cell.value, end="  ")
            print()

    def solve_logic(self):
        for box in self.boxes:
            for cell in box.cells:
                value = cell.value
                if value is None:
                    continue
                box.eliminate(value)
                self.rows[cell.row_index].eliminate(value)
                self.columns[cell.column_index].eliminate(value)

        for shapes in (self.rows, self.columns, self.boxes):
            for shape in shapes:
                for digit in shape.get_remaining():
                    booleans = [cell.booleans[digit - 1] for cell in shape.cells]
                    if booleans.count(True) == 1:
                        cell = shape.cells[booleans.index(True)]
                        cell.set_value(digit)
                        if isinstance(shape, Row):
                            self.columns[cell.column_index].eliminate(digit)
                            self.boxes[cell.box_index].eliminate(digit)
                        elif isinstance(shape, Column):
                            self.rows[cell.row_index].eliminate(digit)
                            self.boxes[cell.box_index].eliminate(digit)
                        else:
                            self.rows[cell.row_index].eliminate(digit)
                            self.columns[cell.column_index].eliminate(digit)

    def solve_brute(self):
        pass  # todo
