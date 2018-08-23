from sys import maxsize

def createStack():
    stack=[];
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack, item):
    stack.append(item)
    print("pushed to stack"+item)

def pop(stack):
    if(isEmpty(stack)):
         return str(-maxsize-1)

    return stack


stack = createStack()
push(stack, str(10))
push(stack, str(19))
push(stack, str(20))
print(pop(stack))

