# A mixin is an independant class that gets pulled in in the inheritance
# hierarchy but is not going to impact anything that inherits it.
# An example is the below SurfaceAreaMixin.
# The SurfaceAreaMixin provides a single method which is surface_area()
# and has no expectation about construction. All it requires is that somewhere
# in the class that is using it, there is an attibute called surfaces.


class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)
        return surface_area
# Regular class definitions for Rectangle, Square and Triangle
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

    def what_am_i(self):
        return 'Rectangle'

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def what_am_i(self):
        return 'Square'


class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def what_am_i(self):
        return 'Triangle'


# Below is the RightPyramid class modified to use the SurfaceAreaMixin
class RightPyramid(Square, Triangle, SurfaceAreaMixin):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        self.height = slant_height
        self.length = base
        self.width = base

        self.surfaces = [Square, Triangle, Triangle, Triangle, Triangle]

# Below is the Cube class modified to use the SurfaceAreaMixin
class Cube(Square, SurfaceAreaMixin):
    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [Square, Square, Square, Square, Square, Square]
