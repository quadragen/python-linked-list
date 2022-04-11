from node import Node
import pdb

class LinkedList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.length = 0

        if data:
            for item in data:
                self.insert(item)

    def __repr__(self):
        output_string = ""

        curr_node = self.head
        while curr_node:
            output_string += str(curr_node)
            curr_node = curr_node.next
        
        return output_string

    def insert(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail = new_node

if __name__ == '__main__':
    test_list = LinkedList([1, 2, 3, 4])
    print(test_list)