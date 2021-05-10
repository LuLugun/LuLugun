from GeometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self,height,width,color,filled):
        super().__init__(color,filled)
        self.__height=height
        self.__width=width
        
    def getWidth(self):
        return self.__width
        
    def getHeight(self):
        return self.__height
        
    def setWidth(self,width):
        self.__width=width
        
    def setHeight(self,height):
        self.__height=height
        
    def getArea(self):
        return self.__width*self.__height
        
    def getPerimeter(self):
        return (self.__width+self.__height)*2