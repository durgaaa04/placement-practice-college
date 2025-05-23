str1 = ""
def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("pushed item:" + item)

def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
  

for i in range(0, 4):
    popped_elem =pop(stack)
    str1 += popped_elem
print("the reverse of the string is :" + str1)





