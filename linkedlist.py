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

    def is_empty(self):
        return self.head is None and self.tail is None

    def insert(self, data):

        for item in data:
            new_node = Node(item)

            if self.tail is None:
                self.head = new_node
                self.tail = new_node
                self.tree.iter_insert(new_node)
                self.length += 1
            else:
                new_node.prev = self.tail
                new_node.prev.next = new_node
                self.tail = new_node
                self.tree.iter_insert(new_node)
                self.length += 1

    def append(self, data):

        for item in data:
            new_node = Node(item)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
                self.tree.iter_insert(new_node)
                self.length += 1
            else:
                new_node.next = self.head
                new_node.next.prev = new_node
                self.head = new_node
                self.tree.iter_insert(new_node)
                self.length += 1

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

    def remove(self, item):

        if type(item) is not Node:
            item = self.quick_search(item)

        if item is self.head:
            item.next.prev = None
            self.head = item.next
            self.tree.iter_remove(item)
            self.length -= 1
        elif item is self.tail:
            item.prev.next = None
            self.tail = item.prev
            self.tree.iter_remove(item)
            self.length -= 1
        else:
            item.next.prev = item.prev
            item.prev.next = item.next
            self.tree.iter_remove(item)
            self.length -= 1
