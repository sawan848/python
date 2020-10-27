class Person(object):
    def __init__(self,firstname,lastname):
        self.first=firstname
        self.last=lastname

    def __cmp__(self,other):
        return cmp((self.last,self.first),(other.last,other.first))

    def __repr__(self):
        return "%s %s" %(self.first,self.last)


actors=Person('Eric','Idle')
print(actors)