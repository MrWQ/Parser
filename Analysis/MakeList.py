
# 构造指定行数列数的空二维表
def makeList(line,column):
    listA = [['' for i in range(column)] for i in range(line)]
    return listA
# 二维表插入特定行列数据
def insertList(list,line,column,text):
    list[line-1][column-1] = text
    return list

# 二维表取出特定行列的数据
def getList(list,line,column):
    # line = int(line)
    # column = int(column)
    text =  list[line-1][column-1]
    return text
