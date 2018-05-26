class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        if (self.is_empty() == False):
            return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 把新的元素堆进栈里面（压栈，入栈，进栈……）
    def push(self, item):
        self.items.append(item)

    # 把栈顶元素丢出去（出栈……）
    def pop(self):
        if (self.is_empty() == False):
            return self.items.pop()
    def stackToStr(self):
        if (self.is_empty() == False):
            strA = "".join(self.items)
            return (strA)
        else:
            return ''
    def stackToReverseStr(self):
        if (self.is_empty() == False):
            strA = "".join(self.items)
            strA = strA[::-1]
            return (strA)
        else:
            return ''

# stack = Stack()
# stack.push('a')
# print(stack.stackToStr())
# stack.push('b')
# stack.push('c')
# print(stack.is_empty())
# print(stack.peek())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.is_empty())
#
# print(stack.pop())

