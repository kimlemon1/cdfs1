class node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next):
        self.next = next

    def get_val(self):
        return self.val
    
class linked_list():
    def __init__(self, root_val):
        root_node = node(root_val)
        self.root = root_node

    def push(self, val):
        new_node = node(val)
