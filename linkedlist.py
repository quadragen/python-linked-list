from node import Node

class LinkedList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.length = 0

        for item in data:
            self.insert(item)

    def __repr__(self):
        output_string = ""

        if self.head is None:
            return None

        curr_node = self.head
        while curr_node:
            output_string += curr_node
            curr_node = curr_node.next
        
        return output_string

    def insert(self, data):
        new_node = Node(data)
        
        if self.tail is None:
            
        
        