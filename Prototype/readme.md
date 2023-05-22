### Implement the deep_copy method to create a deep copy of the Line object.

The classes Point and Line are given.

```
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end
```

This method should return **a copy of the Line object** with the copied start and end points.