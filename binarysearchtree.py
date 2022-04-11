from random import triangular


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.node_count = 0

    def __repr__(self):
        # iterative in-order traversal
        output_string = ""
        curr_node = self.root
        stack = []
        while True:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            elif stack:
                curr_node = stack.pop()
                output_string += curr_node.data
                curr_node = curr_node.right
            else:
                break
        return output_string

    def is_empty(self):
        return self.root is None

    def iter_insert(self, node):
        curr_node = self.root
        trailing_node = None

        while curr_node:
            trailing_node = curr_node
            if node.data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        if trailing_node is None:
            trailing_node = node
            trailing_node.parent = None
        elif node.data < trailing_node.data:
            trailing_node.left = node
            node.parent = trailing_node
            self.node_count += 1
        else:
            trailing_node.right = node
            node.parent = trailing_node
            self.node_count += 1
        return trailing_node

    def bst_iter_search(self, data):
        curr_node = self.root
        while curr_node:
            if data < curr_node.data:
                curr_node = curr_node.left
            elif data > curr_node.data:
                curr_node = curr_node.right
            else:
                return curr_node
    
    