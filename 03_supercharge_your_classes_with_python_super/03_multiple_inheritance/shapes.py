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

class Cube(Square):
    def surface_area(self):
        face_area = self.area()
# We can also do face_area = super().area(), its the same here
        return face_area * 6

    def volume(self):
        face_area = super().area()
# We can also do face_area = self.area(), its the same here
        return face_area * self.length

    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        print('what')
#        return 'I am {self.__class__.__name__} and I am a child of '.format(self=self) + super(Cube, self).what_am_i() # This line works. Here we hard coded Cube inside super(Cube, self), which is not desirable. So better use the shortform version.
#        return 'I am {self.__class__.__name__} and I am a child of '.format(self=self) + super(self.__class__.__name__, self).what_am_i() # This line wont work, since self.__class__.__name__ inside super will return a str, whereas we want Cube type, as written in above statement
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/Users/rohit/Downloads/Study/Python/Object_Oriented_Programming/RealPython_Learning_Path_ObjectOrientedProgrammingOOPwithPython/03_supercharge_your_classes_with_python_super/02_super_and_inheritance_hierarchy/shapes.py", line 44, in family_tree
#     return 'I am {self.__class__.__name__} and I am a child of '.format(self=self) + super(self.__class__.__name__, self).what_am_i()
# TypeError: super() argument 1 must be type, not str

        return 'I am {self.__class__.__name__} and I am a child of '.format(self=self) + super(Cube, self).what_am_i()

class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def what_am_i(self):
        return 'Triangle'

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def what_am_i(self):
        return 'RightPyramid'

# (RealPython_Learning_Path_ObjectOrientedProgrammingOOPwithPython) (base) rohit@Rohits-MacBook-Air 03_multiple_inheritance % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from shapes import Rectangle, Square, Cube, RightPyramid
# >>> rp = RightPyramid(3,4)
# >>> super(RightPyramid, rp).what_am_i()
# 'Triangle'
# >>> RightPyramid.__class__
# <class 'type'>
# >>> rp.__class__
# <class 'shapes.RightPyramid'>
# >>> rp.__class__.__bases__
# (<class 'shapes.Triangle'>, <class 'shapes.Square'>)
# >>> rp.__mro__
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'RightPyramid' object has no attribute '__mro__'
# >>> RightPyramid.__mro__
# (<class 'shapes.RightPyramid'>, <class 'shapes.Triangle'>, <class 'shapes.Square'>, <class 'shapes.Rectangle'>, <class 'object'>)
# >>> rp.area()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/Users/rohit/Downloads/Study/Python/Object_Oriented_Programming/RealPython_Learning_Path_ObjectOrientedProgrammingOOPwithPython/03_supercharge_your_classes_with_python_super/03_multiple_inheritance/shapes.py", line 60, in area
#     return 0.5 * self.base * self.height
# AttributeError: 'RightPyramid' object has no attribute 'height'
