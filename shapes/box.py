from cell import Cell
from shapes.shape import Shape


class Box(Shape):
    def __init__(self, index: int, cells: list[Cell]):
        super().__init__(index, cells)
