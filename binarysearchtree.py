class BinarySearchTree:
    def __init__(self):
        self.root = None

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