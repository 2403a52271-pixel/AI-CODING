def area_rectangle(x, y):
    return x * y

def area_square(x):
    return x * x

def area_circle(x):
    return 3.14 * x * x

def calculate_area(shape, x, y=0):
    dispatch = {
        "rectangle": lambda: area_rectangle(x, y),
        "square": lambda: area_square(x),
        "circle": lambda: area_circle(x)
    }
    if shape in dispatch:
        return dispatch[shape]()
    else:
        raise ValueError("Unknown shape")


# Example usage:
print(calculate_area("rectangle", 4, 5))
print(calculate_area("square", 4))
print(calculate_area("circle", 3))