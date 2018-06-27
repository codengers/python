class Stack():

    def __init__(self):

        self.items=[]


    def push(self, item):

        self.items.append(item)

    def isEmpty(self):

        return self.items ==[]

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def pop(self):

        self.items.pop()

    def get_stack(self):

        return self.items

#

#s = Stack()
#s.push("A")
#s.push("B")
#print(s.get_stack())
#s.push("C")
#s.push("D")
#s.push("E")
#print(s.get_stack())
#s.pop()
#print(s.get_stack())
#print(s.peek())
#

