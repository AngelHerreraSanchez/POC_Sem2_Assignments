class RightTriangle: 
    def __init__(self, base, height, hypotenuse):
        self.base = base
        self.height = height
        self.hypotenuse = hypotenuse
 
    
    def perimeter(self):
        return self.hypotenuse + self.base + self.height
    

        
triangle_1 = RightTriangle(3, 4, 6)
print("The perimeter of triange_1 is", triangle_1.perimeter())

triangle_2 = RightTriangle(5, 6, 8)
print("The perimeter of triange_2 is", triangle_2.perimeter())
  