"""Finding the area and perimeter of different geometrical shapes """
import math


class Circle:
    """creating a Circle class"""
    def find_area(self, radius_):
        """finding area of circle"""
        area = math.pi * radius_ * radius_
        print("Area of a circle is ", area)

    def find_circum(self, radius_):
        """finding circum of circle"""
        circum = 2 * math.pi * radius_
        print("Circumference of a circle is", circum)


class Square:
    """creating a Square class"""
    def find_area(self, side_):
        """finding area of square"""
        area = side * side_
        print("area of square is ", area)

    def find_perimeter(self, side_):
        """finding perimeter of square"""
        perimeter = 4 * side_
        print("perimeter of square is", perimeter)


class Rectangle:
    """creating a Rectangle class"""
    def find_area(self, length_, breadth_):
        """finding area of rectangle"""
        area = length_ * breadth_
        print("area of rectangle is ", area)

    def find_perimeter(self, length_, breadth_):
        """finding perimeter of rectangular"""
        perimeter = 2 * (length_ + breadth_)
        print("perimeter of rectangle is", perimeter)


class Triangle:
    """creating a Triangle class"""
    def find_area(self, side_1, side_2, side_3):
        """finding area of triangle"""
        semi_peri = (side_1 + side_2 + side_3) / 2
        area = (semi_peri * (semi_peri - side_1) * (semi_peri - side_2) * (semi_peri - side_3))**0.5
        print("area of Triangle is ", area)

    def find_perimeter(self, side_1, side_2, side_3):
        """finding perimeter of triangle"""
        perimeter = side_1 + side_2 + side_3
        print("perimeter of square is", perimeter)




while True:

    print('1.circle \n2. square \n3. rectangle \n4. triangle')

    choice = int(input('please select one of the following:'))
    if choice == 1:
        obj = Circle()
        radius = int(input('Enter radius'))
        obj.find_area(radius)
        obj.find_circum(radius)


    elif choice == 2:
        obj = Square()
        side = int(input("Enter side : "))
        obj.find_area(side)
        obj.find_perimeter(side)

    elif choice == 3:
        obj = Rectangle()
        length = int(input('Enter the length'))
        breadth = int(input('Enter the breadth'))
        obj.find_area(length,breadth)
        obj.find_perimeter(length, breadth)

    elif choice == 4:
        obj = Triangle()
        side1 = int(input('Enter first side'))
        side2 = int(input('Enter the second side'))
        side3 = int(input('Enter the third side'))
        obj.find_area(side1, side2, side3)
        obj.find_perimeter(side1, side2, side3)


    else:
        print('invalid option')

print()
