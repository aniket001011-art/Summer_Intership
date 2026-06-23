l = int(input("enter the length of the rectangle-->"))
b = int(input("enter the breath of the rectangle-->"))
class rectangle:
    def __init__(self,l,b):
        self.l = l 
        self.b = b
object1 = rectangle(l,b)
print(object1.l*object1.b)

        