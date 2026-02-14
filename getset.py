class Circle:
    def __init__(self,radius):
        self.radius=radius
    @property
    def radius(self):
        return self._radius
    
    @property
    def area(self):
        return 3.14*(self._radius**2)
    
    @radius.setter
    def radius(self,value):
        if value <=0:
            raise ValueError('Radius must be positive')
        self._radius=value
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius
    
my_circle=Circle(3)
print(my_circle.radius)
my_circle.radius=8
print(my_circle.radius)
print(my_circle.area)
del my_circle.radius # Deleting radius...
print("Radius deleted!") # Radius deleted!
del my_circle.radius # Deleting radius...
print("Radius deleted!") # Radius deleted!