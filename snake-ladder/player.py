class Player:
    """docstring for ."""

    def __init__(self, name, pos=(0,0)):
        self.name = name
        self.pos = pos

    def update_pos(self, pos):
        self.pos = pos
