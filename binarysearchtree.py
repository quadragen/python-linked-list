import pdb
from node import Node


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
                output_string += str(curr_node) + " "
                curr_node = curr_node.right
            else:
                break
        return output_string

    def is_empty(self):
        return self.root is None

    def iter_insert(self, node):
        if node is None:
            return None

        if self.root is None:
            self.root = node
            self.node_count += 1
            return self.root
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

    def iter_search(self, data):
        if data is None:
            return None

        curr_node = self.root
        while curr_node:
            if data < curr_node.data:
                curr_node = curr_node.left
            elif data > curr_node.data:
                curr_node = curr_node.right
            else:
                return curr_node

    def iter_remove(self, node):
        if node is None:
            return None

        if type(node) is not Node:
            node = self.iter_search(node)
            if node is None:
                return None

        curr_node = node
        prev_node = curr_node.parent

        if curr_node.left is None or curr_node.right is None:
            replacement_node = None

            if curr_node.left is None:
                replacement_node = curr_node.right
            else:
                replacement_node = curr_node.left
            
            if prev_node is None:
                return replacement_node
            
            if curr_node is prev_node.left:
                prev_node.left = replacement_node
                self.node_count -= 1
            else:
                prev_node.right = replacement_node
                self.node_count -= 1

            curr_node = None

        else:
            possible_successor = None
            possible_successor_parent = None
            possible_successor = curr_node.right
            
            while possible_successor.left:
                possible_successor_parent = possible_successor
                possible_successor = possible_successor.left

            if possible_successor_parent:
                possible_successor_parent.left = possible_successor.right
            else:
                curr_node.right = possible_successor.right
            
            curr_node = possible_successor
            possible_successor = None
            self.node_count -= 1

        return self.root

if __name__ == '__main__':
    test_tree = BinarySearchTree()
    test_tree.iter_insert(Node(41))
    test_tree.iter_insert(Node(7))
    test_tree.iter_insert(Node(33))
    test_tree.iter_insert(Node(23))
    test_tree.iter_insert(Node(79))
    print(test_tree)
    pdb.set_trace()