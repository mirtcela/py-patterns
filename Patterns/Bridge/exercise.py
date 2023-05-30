from abc import ABC

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

class Shape:
    def __init__(self, renderer):
        self.name = None
        self.renderer = renderer

class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'
    
    def __str__(self):
        return f'Drawing {self.name} as {self.renderer}'


class Square(Shape):
    def __init__(self,  renderer):
        super().__init__(renderer)
        self.name = 'Square'

    def __str__(self):
        return f'Drawing {self.name} as {self.renderer}'


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'
    
    def __str__(self):
        return 'lines'


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'
        
    def __str__(self):
        return 'pixels'

# imagine VectorTriangle and RasterTriangle are here too
        
def main():
    raster = RasterRenderer()
    vector = VectorRenderer()
    square = str(Square(RasterRenderer()))

    print(square)