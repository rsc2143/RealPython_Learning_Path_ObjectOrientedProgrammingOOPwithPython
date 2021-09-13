class Square:
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return 'Class is {self.__class__.__name__}, length is {self.length}'.format(self=self)

    def __repr__(self):
        return '{self.__class__.__name__}, {self.length}'.format(self=self)

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return self.length * 4

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return 'Class is {self.__class__.__name__}, length is {self.length}, width is {self.width}'.format(self=self)

    def __repr__(self):
        return '{self.__class__.__name__}, {self.length}, {self.width}'.format(self=self)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width
