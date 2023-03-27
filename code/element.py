
class Element:

    def __init__(self, value1, value2, value3, value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        self.values = [value1, value2, value3, value4]

    def __repr__(self):
        return 'Element: ' + str(self.value1) + ' ' + str(self.value2) + ' ' + str(self.value3) + ' ' + str(self.value4)


