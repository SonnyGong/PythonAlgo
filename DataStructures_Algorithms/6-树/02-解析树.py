# -*- coding: utf-8 -*-

from operator import add, sub, mul, truediv

from pythonds.basic import Stack
from pythonds.trees import BinaryTree

op = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}


# 构建解析树
def build_parse_tree(exp_string):
    exp_list = exp_string.split()  # 表达式符号列表
    parent_stack = Stack()  # 存储父节点的栈
    parse_tree = BinaryTree('')  # 解析树
    node = parse_tree  # 当前节点

    for char in exp_list:
        if char == '(':
            # 创建并切换到左子节点
            parent_stack.push(node)
            node.insertLeft('')
            node = node.leftChild
        elif char in '+-*/':
            # 切换回父节点，设置父节点的值
            node = parent_stack.pop()
            node.data = char
            # 创建并切换到右子节点
            parent_stack.push(node)
            node.insertRight('')
            node = node.rightChild
        elif char in ')':
            # 切换回父节点
            node = parent_stack.pop()
        elif char.isdigit():
            # 设置当前节点的值
            node.data = eval(char)
        else:
            raise ValueError(f'Unknown character: {char}')

    return parse_tree


# 计算解析树的结果
def evaluate(parse_tree: BinaryTree):
    left, right = parse_tree.leftChild, parse_tree.rightChild
    if left is None and right is None:
        return parse_tree.data

    return op[parse_tree.data](evaluate(left), evaluate(right))


# 通过后序遍历计算解析树
def postorder_eval(tree: BinaryTree):
    if tree is None:
        return
    left, right = postorder_eval(tree.leftChild), postorder_eval(tree.rightChild)
    if left is None and right is None:
        return tree.data

    return op[tree.data](left, right)


# 通过中序遍历还原表达式
def inorder_exp(tree: BinaryTree):
    if tree is None:
        return ''
    if tree.leftChild is None and tree.rightChild is None:
        return tree.data

    exp_list = ['(', str(inorder_exp(tree.leftChild)),
                tree.data, str(inorder_exp(tree.rightChild)), ')']
    return ' '.join(exp_list)


if __name__ == '__main__':
    exp_string = '( 3 + ( 4 * 5 ) )'
    ptree = build_parse_tree(exp_string)
    print(f'{exp_string} = {evaluate(ptree)}')
    print(f'{exp_string} = {postorder_eval(ptree)}')
    print(f'{inorder_exp(ptree)}')

    exp_string = '( ( 7 + 3 ) * ( 5 - 2 ) )'
    ptree = build_parse_tree(exp_string)
    print(f'{exp_string} = {evaluate(ptree)}')
    print(f'{exp_string} = {postorder_eval(ptree)}')
    print(f'{inorder_exp(ptree)}')
