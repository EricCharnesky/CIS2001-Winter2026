class BinaryTree:

    def __init__(self, data, parent=None, left_child=None, right_child=None):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def add_left(self, data):
        if self.left_child is not None:
            raise ValueError()
        self.left_child = BinaryTree(data, self)

    def add_right(self, data):
        if self.right_child is not None:
            raise ValueError()
        self.right_child = BinaryTree(data, self)

    def get_sibling(self):
        if self.parent is None:
            return None
        parent = self.parent
        if parent.left_child is self:
            return parent.right_child
        return parent.left_child

    def depth(self):
        level = 0
        current_tree = self
        while current_tree.parent:
            level += 1
            current_tree = current_tree.parent
        return level

    def print_depth_first(self):
        if self.left_child:
            self.left_child.print_depth_first()
        if self.right_child:
            self.right_child.print_depth_first()
        print(self.data)

    def print_in_order_traversal(self):
        if self.left_child:
            self.left_child.print_depth_first()
        print(self.data)
        if self.right_child:
            self.right_child.print_depth_first()


# depth first L R self

tree = BinaryTree(20)
tree.add_left(30)
tree.add_right(40)
left = tree.left_child
left.add_left(10)
left.add_right(25)
left = left.left_child
left.add_right(1)


tree.print_in_order_traversal()