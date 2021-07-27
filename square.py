class Square:
    def __init__(self, w, h):
        self.height = h
        self.__width = w
    def set_side(self,new_side):
        self.height = new_side
        self.__width = new_side

    # def get_height(self):
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, new_value):
    # def set_height(self, h):
        if new_value >= 0:
            self.__height = new_value
        else:
            raise Exception("value needs to be 0 or larger")

square = Square()
# square.__height = 4
