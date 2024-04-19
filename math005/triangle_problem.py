

def triangle_area(A: tuple, B:tuple, C:tuple ):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    # print(f'({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3})')
    area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2 
    return area


def is_inside_triangle() -> bool:
    O: tuple = (0, 0)
    A: tuple = (2, 0)
    B: tuple = (-2, -2)
    C: tuple = (2, -2)

    area_OAB: int = triangle_area(O, A, B)
    print(area_OAB)

    area_OAC: int = triangle_area(O, A, C)
    print(area_OAC)
    
    area_OBC: int = triangle_area(O, B, C)
    print(area_OBC)

    area_ABC: int = triangle_area(A, B, C)
    print(area_ABC)

    return area_ABC == area_OAB + area_OAC + area_OBC

is_inside_triangle()

