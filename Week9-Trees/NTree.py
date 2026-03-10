class NTree:

    def __init__(self, data, parent=None, children=None):
        self.data = data
        self.parent = parent
        if children:
            self.children = children
        else:
            self.children = []

    def add_child(self, data):
        self.children.append(NTree(data, self))

    # O(n)
    def depth(self):
        level = 0
        current_tree = self
        while current_tree.parent:
            level += 1
            current_tree = current_tree.parent
        return level

    def _breadth_first_traversal(self, nodes = None):
        if not nodes:
            nodes = []
        nodes.extend(self.children)
        for child in self.children:
            child._breadth_first_traversal(nodes)
        return nodes

    # O(n^2)
    def height(self):
        nodes = self._breadth_first_traversal()
        return max(node.depth() for node in nodes)

tree = NTree(10)
tree.add_child(20)
tree.add_child(30)
child = tree.children[0]
child.add_child(40)
child.add_child(50)
child = child.children[0]
child.add_child(60)

print(tree.height())





