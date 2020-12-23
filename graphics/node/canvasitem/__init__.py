from .. import Node


class CanvasItem(Node):
    def __init__(self, parent, pos):
        super().__init__(parent)
        self.pos = pos
