class Rectangle:
    __counter = 0 


    def get_count():
        return Rectangle.__counter
    



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

    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return self.__height * self.__base
    
    def __str__(self) -> str:
        return "Rectangle with base:" + str(self.__base) + ", height:" + str(self.__height)

    
 
 
 
Rectangle_1 = Rectangle(5, 8)
print(Rectangle_1)


Rectangle_2 = Rectangle(7, 10)
print(Rectangle_2)


print(Rectangle.get_count())
