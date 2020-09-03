class MaxSizeList(object):

    def __init__(self,max):
        self.max_size=max
        self.innerList=[]
        #super().__init__()

    def push(self,obj):
        self.innerList.append(obj)
        if len(self.innerList)>self.max_size:
            self.innerList.pop(0)

    def get_list(self):
        return self.innerList

a=MaxSizeList(3)
b=MaxSizeList(1)

a.push('hey')
a.push('hi')
a.push('let`s')
a.push('go')

b.push('hey')
b.push('hi')
b.push('let`s')
b.push('go')

print(a.get_list())
print(b.get_list())
