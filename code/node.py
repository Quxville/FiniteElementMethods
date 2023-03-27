class Node:
    def __init__(self, x, y, t, BC):
        self.x = x
        self.y = y
        self.t = 0
        self.BC = 0

    def __repr__(self):
        return 'Node: ' + str(self.x) + ' ' + str(self.y) + ' ' + str(self.t) + ' ' + str(self.BC)

