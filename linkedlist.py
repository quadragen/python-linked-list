from node import Node
# import pdb

class LinkedList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.length = 0

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
                self.length += 1
            else:
                new_node.prev = self.tail
                new_node.prev.next = new_node
                self.tail = new_node
                self.length += 1

    def append(self, data):

        for item in data:
            new_node = Node(item)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
                self.length += 1
            else:
                new_node.next = self.head
                new_node.next.prev = new_node
                self.head = new_node
                self.length += 1

    def linear_search(self, data):
        curr_a = self.head
        curr_b = self.tail

        while (curr_a.data != data and curr_b.data != data) and (curr_a != curr_b):
            curr_a = curr_a.next
            curr_b = curr_b.prev

        if curr_a.data == data:
            return curr_a
        elif curr_b.data == data:
            return curr_b
        elif (curr_a == curr_b) and (curr_a.data != data and curr_b.data != data):
            return None

    def remove(self, item):

        if type(item) is not Node:
            item = self.linear_search(item)

        if item is self.head:
            item.next.prev = None
            self.head = item.next
            self.length -= 1
        elif item is self.tail:
            item.prev.next = None
            self.tail = item.prev
            self.length -= 1
        else:
            item.next.prev = item.prev
            item.prev.next = item.next
            self.length -= 1

if __name__ == '__main__':
    test_list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'a'])
    # pdb.set_trace()
    print(test_list)