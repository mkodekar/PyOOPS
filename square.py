class Square:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def getArea(self):
        return int(self.width) * int(self.height)

    @height.setter
    def height(self, value):
        if str(value).isdigit():
            self.__height = value
        else:
            print('Please enter a number for height')

    @width.setter
    def width(self, value):
        if str(value).isdigit():
            self.__width = value
        else:
            print('Please enter a number for width')


def main():
    square = Square()

    height = input('Enter the height of the square: ')
    width = input('Enter the width of the square :')

    square.height = height
    square.width = width

    print('Height of the square is', square.height)
    print('Width of the square is', square.width)

    print('Area of the square is ', square.getArea())


if __name__ == '__main__':
    main()
