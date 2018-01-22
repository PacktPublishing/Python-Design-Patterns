# === abstract shape classes ===
class Shape2DInterface:
    def draw(self): pass

class Shape3DInterface:
    def build(self): pass

# === concrete shape classes ===
class Circle(Shape2DInterface):
    def draw(self):
        print("Circle.draw")

class Square(Shape2DInterface):
    def draw(self):
        print("Square.draw")

class Sphere(Shape3DInterface):
    def build(self):
        print("Sphere.build")

class Cube(Shape3DInterface):
    def build(self):
        print("Cube.build")


# === Abstract shape factory ===
class ShapeFactoryInterface:
    def getShape(sides): pass

# === Concrete shape factories ===
class Shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Square()
        assert 0, "Bad 2D shape creation: shape not defined for " + sides + "sides"

class Shape3DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        """here, sides refers to the number of faces"""
        if sides == 1:
            return Sphere()
        if sides == 6:
            return Cube()
        assert 0, "Bad 3D shape creation: shape not defined for " + sides + "faces"
