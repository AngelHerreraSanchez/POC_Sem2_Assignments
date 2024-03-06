class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) -> float:
        return self.__base 
    #YOUDO the get_base method
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return self.__height * self.__base
    #Youdo get_area method
 
 
 
Rectangle_1 = Rectangle(5, 8)
print("Base: ", Rectangle_1.get_base(), "Height: ", Rectangle_1.get_height(), "Perimeter: ", Rectangle_1.get_perimeter(), "Area: ", Rectangle_1.get_area() )

Rectangle_2 = Rectangle(7, 10)
print("Base: ", Rectangle_2.get_base(), "Height: ", Rectangle_2.get_height(), "Perimeter: ", Rectangle_2.get_perimeter(), "Area: ", Rectangle_2.get_area() )

#YOUDO>  create two rectangles.  print their base, height, perimeter, and area
#using only the methods not the fields/property/attributes
