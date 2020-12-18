from collections import deque
import operator

lines = open('input.txt').read().splitlines()
#lines = open(0).read().splitlines()
lines = [line for line in lines if line[0] != '#']

op = {
    '*': operator.mul,
    '+' : operator.add,
}

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.this = None
        self.brackets = False

    def is_leaf(self):
        return self.left == None and self.right == None

    def __repr__(self):
        if self.is_leaf():
            return f"{self.data}"
        msg = f"({self.left if self.left is not None else ''} {self.data} {self.right if self.right is not None else ''})"
        if self.brackets:
            msg = f"({msg})"
        return msg

    def __str__(self):
        return self.__repr__()

def evaluate(tree):
    # print(tree)
    if tree.left is None and tree.right is None:
        return tree.data
    operator = op[tree.data]
    left = evaluate(tree.left)
    right = evaluate(tree.right)
    res = operator(left, right)
    old_tree = str(tree)
    # print(tree, '=', res)
    tree.left = left
    tree.right = right
    # print(f'eval: {left} {operator} {right}')
    print(tree, '=', res, "\t\t\tprev", old_tree)
    return res

def step(parts):
    first = parts.popleft()
    if first[0] == '(':
        # go until next ')'. but what if there are more '(' on the way?
        # parts.appendleft(first)
        count = {'(': first.count('('), ')': 0}
        deeper = deque([first.replace('(', '', 1)])
        while count['('] != count[')']:
            new = parts.popleft()
            count['('] += new.count('(')
            count[')'] += new.count(')')
            deeper.append(new)
        
        # remove last )
        last = deeper.pop()
        deeper.append(last.replace(')', '', 1))
        first = parser(deeper)
        first.brackets = True
    return first, parts

def parser(parts):
    if isinstance(parts, Tree):
        return parts
    if isinstance(parts, str):
        node = Tree()
        node.data = int(parts.replace('(', '').replace(')', ''))
        return node
    if len(parts) == 1:
        return parts[0]
    if len(parts) >= 3:
        left = parts.popleft()
        if isinstance(left, str):
            parts.appendleft(left)
            left, parts = step(parts)

        operator = parts.popleft()

        right = parts.popleft()
        if isinstance(right, str):
            parts.appendleft(right)
            right, parts = step(parts)

        node = Tree()
        node.left = parser(left)
        node.data = operator
        node.right = parser(right)

        if operator == "+":
            print(f'(+ found) left: {node.left}, right {node.right}')

            # reorder tree to give + precedence over *.
            new_node = Tree()
            new_node.data = operator
            new_node.right = node.right
            if node.left.is_leaf():
                # if left is value. then new_node is the new node. 2 + [...]
                new_node.left = node.left
                node = new_node
            else:
                # make sure we dont reorder in the case that the left part is in brackets.
                # (2 * 3) + [...] -> (2 * 3) + [...]
                if not node.left.brackets:
                    # if node to left is a node. then make it the parent and have it point to new_node to the right.
                    # 2 * 3 + [...] -> 2 * (3 + [....])
                    new_node.left = node.left.right
                    # node.left.right = new_node
                    node.data = node.left.data
                    node.right = new_node
                    node.left = node.left.left
            
            print(f'reordered: left: {node.left}, data: {node.data}, right: {node.right}')

        parts.appendleft(node)
        return parser(parts)
    assert False


tot = 0
for line in lines:
    print("line:", line)
    tree = parser(deque(line.split()))
    print("tree:", tree)
    value = evaluate(tree)
    print(value)
    print()
    tot += value
print(tot)