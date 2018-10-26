def parent_function(num):

    #print("This is parent function")

    def first_child():

        return "This is first child function"

    def second_child():

        return "This is second child function"

    #first_child()
    #second_child()


    try:
       assert num == 10
       return first_child
    except AssertionError:
       return second_child
    
foo = parent_function(10)
bar = parent_function(11)
print(foo)
print(bar)

print(foo())
print(bar())
