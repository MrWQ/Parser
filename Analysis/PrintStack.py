import Stack,copy
# 将栈的内容打印 从栈顶到栈底的序列
def printStack(stackA):
    print(id(stackA))
    stack=copy.copy(stackA)
    print(id(stack))
    stackstr=''
    while(stack.is_empty() ==False):
        stackstr=stackstr+stack.pop()
    return stackstr

# 将栈的内容打印 从栈底到栈顶的序列
def printReverseStack(stackB):
    stack=stackB
    stackstr=''
    while(stack.is_empty() ==False):
        stackstr=stackstr+stack.pop()
        stackstr = stackstr[::-1]
    # print(stackstr)
    return stackstr

# stack = Stack.Stack()
# stack.push('1')
# stack.push('2')
# stack.stackToStr()
# print(stack.stackToStr())
# print(stack.stackToReverseStr())
# print(stack.stackToStr())
# stack1=stack
# print(id(stack))
# print(id(stack1))
# stack2=copy.copy(stack)
# print(id(stack2))
# print(str(stack))

# a=printStack(stack)
# print(str(a))
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())