import Stack


# 字符串反转  倒序 返回列表
def reverse(text):
    textA = str(text)
    textA = textA[::-1]
    return list(textA)

# 字符串 倒序压栈
def pushStack(stack,text):
    text = reverse(text)
    for i in text:
        # print(i)
        stack.push(i)
    return stack

# 判定是否为终结符
def isTerminator(text):
    listT = 'adbe#'
    listT = list(listT)
    # print(listT)
    if text in listT:
        return True
    else:
        return False

# 根据内容得到二维表的行
def getLine(text):
    text = str(text)
    text = text.strip()#去掉空格
    listT = 'SHMA'
    listT = list(listT)
    j = 0
    for i in listT:
        j+=1
        if (i == text):
            return j

# 根据内容得到二维表的列
def getColumn(text):
    text = str(text)
    text = text.strip()
    listT =  'adbe#'
    listT = list(listT)
    j = 0
    for i in listT:
        j+=1
        if (i == text):
            return j




# print(isTerminator('a'))
# print(isTerminator('d'))
# print(isTerminator('b'))
# print(isTerminator('e'))
# print(isTerminator('#'))
# print(isTerminator('c'))


# a=rever
# for i in a:
#     print(i)

# stack1 = Stack.Stack()
# print(stack1.is_empty())

# stack1.push(1)
# stack1.push(2)
# print(stack1)
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())

# stack1 = pushStack(stack1,'123456')
# print(stack1.is_empty())
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())