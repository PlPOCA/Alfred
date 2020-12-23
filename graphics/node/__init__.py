class Node:
    def __init__(self, parent):
        self.parent = parent
        self.children = []
        self.parent.add_child(self)
        for subclass in self.__class__.__subclasses__():
            subclass(self)

    def add_child(self, *children):
        if self.parent not in children:
            self.children.extend(children)

    def process(self, event):
        pass

    def _set_app(self, app):
        for child in self.children:
            child._set_app(app)
