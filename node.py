class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return self.data