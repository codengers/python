# function returning function
def foo(x):
    print("x:"+str(x))
    def bar(y):
        print("y:"+str(y))
        return y+x+3
    return bar

f1 = foo(1)
#f2 = foo(3)

print(f1(2))
#print(f2)
