from src.entity.student import Student


class TreeNode:

    def __init__(self, obj: Student):
        self.left = None
        self.right = None
        self.value = obj

    def insert(self, obj: Student, key: str):
        value = getattr(obj, key)
        if self.value:
            if value < getattr(self.value, key):
                if self.left is None:
                    self.left = TreeNode(obj)
                else:
                    self.left.insert(obj, key)
            elif value > getattr(self.value, key):
                if self.right is None:
                    self.right = TreeNode(obj)
                else:
                    self.right.insert(obj, key)
        else:
            self.value = obj

    def tree_search(self, value: str | int, key: str):
        if value < getattr(self.value, key):
            if self.left is None:
                return None
            return self.left.tree_search(value, key)
        elif value > getattr(self.value, key):
            if self.right is None:
                return None
            return self.right.tree_search(value, key)
        else:
            return self.value
