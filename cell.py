class Cell:
    def __init__(self, row_index: int, column_index: int, box_index: int, value: int or None):
        self.row_index = row_index
        self.column_index = column_index
        self.box_index = box_index
        self.value = value
        self.booleans = [True] * 9 if value is None else [False] * 9

    def set_value(self, value: int):
        self.value = value
        self.booleans = [False] * 9
