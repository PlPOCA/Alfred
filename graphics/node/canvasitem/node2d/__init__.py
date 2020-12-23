from .....math.vector import Vector2
from .. import CanvasItem


class Node2D(CanvasItem):
    def __init__(self, parent, pos=Vector2(0, 0), scale=1, rotation_degree=0):
        super().__init__(parent, pos)
        self.scale = scale
        self.scale = rotation_degree
