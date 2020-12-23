from ..node import Node


def get_scene_class(node_class=Node):

    class Scene(node_class):
        def __init__(self):
            self.app = None
            super().__init__(self)

    return Scene