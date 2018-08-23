x=0

class Fruit(object):

    def __init__(self):
        global x
        x=x+1
        print("I am fruit")

class Citrus(Fruit):
    def __init__(self, arg):
        super(Citrus, self).__init__()
        global x
        x=x+2


print(x)
lime=Citrus()
