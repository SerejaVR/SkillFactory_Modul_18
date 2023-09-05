from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

S = Circle(20)
print(S.s_circle())

print(square_1.get_area_square(), square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2, S]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.s_circle())
    else:
        print(figure.get_area())










