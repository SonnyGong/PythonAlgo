import operator

from PythonAlgo.stack_test import Stack


class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            _ = self.leftChild
            self.leftChild = BinaryTree(newNode)
            self.leftChild.leftChild = _

    def insertRight(self,newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            _ = self.rightChild
            self.rightChild = BinaryTree(newNode)
            self.rightChild.rightChild = _


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootval(self,obj):
        self.key = obj

    def getRootval(self):
        return self.key

def buildParaseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i not in '+-*/)':
            currentTree.setRootval(eval(i))
            parent = pStack.pop()
            currentTree = parent

        elif i in '+-*/':
            currentTree.setRootval(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError('Illegal input'+ i)

    return eTree


def evaluate(parseTree):
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))

    else:
        return parseTree.getRootval()

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeftChild(self):
        return self.leftChild is not None


if __name__ == '__main__':
    test = TreeNode(1,2)
    print(test.hasLeftChild())
    # r = BinaryTree('a')
    # print(r.getRootval())
    # print(r.getLeftChild())
    # r.insertLeft('b')
    # print(r.getLeftChild())
    # print(r.getLeftChild().getRootval())







