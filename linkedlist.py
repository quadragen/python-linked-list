from node import Node
from binarysearchtree import BinarySearchTree

class LinkedList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.length = 0
        self.tree = BinarySearchTree()

        if data:
            self.insert(data)

    def __repr__(self):
        output_string = ""

        curr_node = self.head
        while curr_node:
            output_string += str(curr_node) + " "
            curr_node = curr_node.next
        
        return output_string

    def _insert(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            self.tree.iter_insert(node)
            self.length += 1
        else:
            node.prev = self.tail
            node.prev.next = node
            self.tail = node
            self.tree.iter_insert(node)
            self.length += 1

    def _append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.tree.iter_insert(node)
            self.length += 1
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node
            self.tree.iter_insert(node)
            self.length += 1

    def _remove(self, node):
        if node is self.head:
            node.next.prev = None
            self.head = node.next
            self.tree.iter_remove(node)
            self.length -= 1

        elif node is self.tail:
            node.prev.next = None
            self.tail = node.prev
            self.tree.iter_remove(node)
            self.length -= 1

        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.tree.iter_remove(node)
            self.length -= 1

    def is_empty(self):
        return self.head is None and self.tail is None

    def insert(self, data):
        if type(data) is int or type(data) is str:
            new_node = Node(data)
            self._insert(new_node)

        elif type(data) is Node:
            self._insert(data)

        elif type(data) is list:
            for item in data:
                if type(item) is Node:
                    self._insert(item)

                elif type(item) is int or type(item) is str:
                    new_node = Node(item)
                    self._insert(new_node)
                
                elif type(item) is None:
                    continue

        elif type(data) is None:
            return None

    def append(self, data):
        if type(data) is int or type(data) is str:
            new_node = Node(data)
            self._append(new_node)

        elif type(data) is Node:
            self._append(data)

        elif type(data) is list:
            for item in data:
                if type(item) is Node:
                    self._append(item)

                elif type(item) is int or type(item) is str:
                    new_node = Node(item)
                    self._append(new_node)

                elif type(item) is None:
                    continue

        elif type(data) is None:
            return None

    def remove(self, data):
        if type(data) is int or type(data) is str:
            item = self.quick_search(data)
            self._remove(item)
        
        elif type(data) is Node:
            self._remove(data)

        elif type(data) is list:
            for item in data:
                if type(item) is Node:
                    self._remove(item)

                elif type(item) is int or type(item) is str:
                    item = self.quick_search(item)
                    self._remove(item)

                elif type(item) is None:
                    continue

        elif type(data) is None:
            return None

    def linear_search(self, data):
        curr_node_a = self.head
        curr_node_b = self.tail

        while (curr_node_a.data != data and curr_node_b.data != data) and (curr_node_a != curr_node_b):
            curr_node_a = curr_node_a.next
            curr_node_b = curr_node_b.prev

        if curr_node_a.data == data:
            return curr_node_a
        elif curr_node_b.data == data:
            return curr_node_b
        elif (curr_node_a == curr_node_b) and (curr_node_a.data != data and curr_node_b.data != data):
            return None

    def quick_search(self, data):
        return self.tree.iter_search(data)
