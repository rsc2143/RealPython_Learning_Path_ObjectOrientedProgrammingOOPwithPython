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


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

# (RealPython_Learning_Path_ObjectOrientedProgrammingOOPwithPython) (base) rohit@Rohits-MacBook-Air 01_object_inheritance_in_python % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> # If I define Square before Rectangle class, then I get below error
# >>> from shapes_with_super_function import Square, Rectangle
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/Users/rohit/Downloads/Study/Python/Object_Oriented_Programming/RealPython_Learning_Path_ObjectOrientedProgrammingOOPwithPython/03_supercharge_your_classes_with_python_super/01_object_inheritance_in_python/shapes_with_super_function.py", line 1, in <module>
#     class Square(Rectangle):
# NameError: name 'Rectangle' is not defined
# >>> from shapes_with_super_function import Square, Rectangle
# >>> square = Square(4)
# >>> square
# Square, 4, 4
# >>> print(square)
# Class is Square, length is 4, width is 4
# >>> dir(square)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'length', 'perimeter', 'width']
# >>> square.width
# 4
# >>> square.length
# 4
# >>> square.area()
# 16
# >>> square.__class__.__bases__
# (<class 'shapes_with_super_function.Rectangle'>,)
# >>> # __bases__ attribute gives us the class from which the given class is inherited from
