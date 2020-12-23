from .app import App


def start(*args, **kwargs):
    App(*args, **kwargs).mainloop()
