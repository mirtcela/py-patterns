import copy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        new_start = Point(self.start.x, self.start.y)
        new_end = Point(self.end.x, self.end.y)
        return Line(new_start, new_end)
    
    # another solution
    # def deep_copy(self):
    #     new_start = Point(self.start.x, self.start.y)
    #     new_end = Point(self.end.x, self.end.y)
    #     return Line(new_start, new_end)
    
    def __str__(self):
        return f'Line from start: {self.start} to end: {self.end}'
    

def main():
    p1 = Point(10, 10)
    p2 = Point(10, 20)
    print(p1)
    print(p2)
    line1 = Line(p1, p2)
    print(line1)
    line2 = line1.deep_copy()
    print(line2)

main()