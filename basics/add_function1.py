class Ruler(object):
    
    def __init__(self,feet,inches):
        self.feet=feet
        self.inches=inches

    def __add__(self,other):
        f=self.feet+other.feet
        i=self.inches+other.inches
        return Ruler(f+i // 12,i%12)

    def __str__(self):
        return str(self.feet)+ "'"+str(self.inches) +'"'

r1=Ruler(2,9)
r2=Ruler(3,7)
r3=r1+r2
print(r3)