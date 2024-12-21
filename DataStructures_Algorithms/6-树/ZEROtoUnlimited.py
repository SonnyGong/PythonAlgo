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



if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.getRootval())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootval())







