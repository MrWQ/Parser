
import MakeList,Stack,AnalysisClass,PrintStack


#构造 二维表
listA = MakeList.makeList(4,5)
#构造 分析表
listA = MakeList.insertList(listA,1,1,'aH')
listA = MakeList.insertList(listA,2,1,'aMd')
listA = MakeList.insertList(listA,2,2,'d')
listA = MakeList.insertList(listA,3,1,'Ab')
listA = MakeList.insertList(listA,3,2,'*')
listA = MakeList.insertList(listA,3,3,'*')
listA = MakeList.insertList(listA,3,4,'Ab')
listA = MakeList.insertList(listA,4,1,'aM')
listA = MakeList.insertList(listA,4,4,'e')

print(listA)
# print(MakeList.getList(listA,1,1))

# 构造分析栈
analysisStack = Stack.Stack()
analysisStack.push('#')
analysisStack.push('S')
# print('分析栈 '+analysisStack.peek())
#构造剩余输入串栈
remainStack = Stack.Stack()
# remainStack = AnalysisClass.pushStack(remainStack,'a#')
# remainStack = AnalysisClass.pushStack(remainStack,'ad#')
remainStack = AnalysisClass.pushStack(remainStack,'aaabd#')

# 声明步骤变量 计数
count=0
# 分析开始
def Analysis(listA,analysisStack,remainStack,count):
    count +=1
    # 分析栈顶变量
    A = analysisStack.pop()
    # 输入栈顶变量
    R = remainStack.pop()
    # 栈的内容转字符串
    strA = analysisStack.stackToStr() + A +'\t'
    strB = R + remainStack.stackToReverseStr() +'\t'
    # strB = strB+'\t'
    # 如果为终结符
    if(AnalysisClass.isTerminator(A)):
        # 如果相等 递归
        if(A == R):
            if(A == '#'):
                print('{}\t{}\t{}\t{}\t'.format('步骤' + str(count), strA, strB, A + '匹配' + R))
                print("是该语法的句子")
                return 0
            else:
                # print('步骤'+str(count)+'\t'+strA+'\t'+strB+'\t'+A+"匹配"+R+'\t')
                print('{}\t{}\t{}\t{}\t'.format('步骤'+str(count),strA,strB,A+'匹配'+R))
                Analysis(listA, analysisStack, remainStack,count)
        # 如果不相等 报错
        else:
            print("Error Number 001")
            print("栈顶内容不匹配")
            return 0
    # 如果为非终结符
    else:
        #把R压回剩余栈
        remainStack.push(R)
        # 得到 行
        AN = AnalysisClass.getLine(A)
        # 得到  列
        RN = AnalysisClass.getColumn(R)
        # 得到分析表中的内容
        text = MakeList.getList(listA,AN,RN)
        # 如果 内容为空白 则报错
        if(text == ''):
            print("Error Number 002")
            print("分析表查到空项")
            return 0
        # 如果为* 则跳过
        elif (text == '*'):
            print('{}\t{}\t{}\t{}\t'.format('步骤' + str(count), strA, strB, '*'))
            Analysis(listA, analysisStack, remainStack,count)
        else:
            print('{}\t{}\t{}\t{}\t'.format('步骤' + str(count), strA, strB, text))
            # 倒序压 分析栈  递归
            analysisStack = AnalysisClass.pushStack(analysisStack, text)
            Analysis(listA,analysisStack,remainStack,count)


# print('步骤\t'+'分析栈\t'+'剩余输入串\t'+'产生式或匹配\t')
print('{}\t{}\t{}\t{}\t'.format('步骤','分析栈','剩余输入串','产生式或匹配'))
Analysis(listA,analysisStack,remainStack,count)