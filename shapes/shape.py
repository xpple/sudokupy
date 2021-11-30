from abc import ABC

from cell import Cell
from const import DIGITS


class Shape(ABC):
    def __init__(self, index: int, cells: list[Cell]):
        self.index = index
        self.cells = cells

    def eliminate(self, value: int) -> None:
        for cell in self.cells:
            cell.booleans[value - 1] = False

    def get_remaining(self) -> set[int]:
        return DIGITS ^ {cell.value for cell in self.cells if cell.value is not None}
