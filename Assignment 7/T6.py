class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base

    def get_height_base(self):
        return "Height: "+str(self.height)+",Base: "+str(self.base)
#write your code here
class triangle(Shape):
    def calcArea(self):
        self.area = 0.5*self.height*self.base
    def printDetail(self):
        details = ["Shape name: "+str(self.name),self.get_height_base(),"Area: "+str(self.area)]
        return "\n".join(details)
    
class trapezoid(Shape):
    def __init__(self, name="Default",height=0,base=0,side_a=0):
        Shape.__init__(self,name,height,base)
        self.side_a=side_a
    def calcArea(self):
        self.area = 0.5*(self.base+self.side_a)*self.height
    def printDetail(self):
        details = ["Shape name: "+str(self.name),self.get_height_base()+",Side_A: "+str(self.side_a),"Area: " + str(self.area)]
        return "\n".join(details)

tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())