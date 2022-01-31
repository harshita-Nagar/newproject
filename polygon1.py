class Polygon:
    def __init__(self,sides):
        self.sides=sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines ")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges.")


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        Polygon.display_info(self)


t1=Triangle([6, 8, 9])
perimeter=t1.get_perimeter()
print("perimeter:", perimeter)
t1.display_info()

q1=Quadrilateral([3,9,6,1])
perimeter=q1.get_perimeter()
print("perimeter:", perimeter)
q1.display_info()

