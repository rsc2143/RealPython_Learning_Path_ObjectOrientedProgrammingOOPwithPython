class Rectangle():
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        self.length = length
        super().__init__(length = self.length, width = self.length, **kwargs)

class Triangle():
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs['length'] = base
        kwargs['height'] = slant_height
        super().__init__(base=base, **kwargs)
