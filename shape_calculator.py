# Rectangle class definition
class Rectangle:
    def __init__(self, width, height):
        # initialize a rectangle with given width and height
        self.width = width
        self.height = height

    def set_width(self, width):
        # set width of rectangle
        self.width = width

    def set_height(self, height):
        # set height of rectangle
        self.height = height

    def get_area(self):
        # calculate and return area of rectangle
        return self.width * self.height

    def get_perimeter(self):
        # Calculate and return perimeter the rectangle
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # calculate and return diagonal of rectangle
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # return a string representation of rectangle using "*"
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for _ in range(self.height):
                picture += "*" * self.width + "\n"
            return picture

    def get_amount_inside(self, shape):
        # calculate then return the number of times the given shape can fit inside the rectangle
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit

    def __str__(self):
        # return string representation of rectangle
        return f"Rectangle(width={self.width}, height={self.height})"


# Square class, subclass of Rectangle
class Square(Rectangle):
    def __init__(self, side):
        # initialize a square with a given side length
        # set side as both width and height of the square
        super().__init__(side, side)

    def set_side(self, side):
        # set both width and height when setting the side of a square
        self.width = side
        self.height = side

    def set_width(self, width):
        # overwrite set_width to set both width and height for square
        self.set_side(width)

    def set_height(self, height):
        # now overwrite set_height to set both width and height for square
        self.set_side(height)

    def __str__(self):
        # returns string representation for the square
        return f"Square(side={self.width})"
