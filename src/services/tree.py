from src.entity.student import Student


class Tree:

    def __init__(self, obj:Student):
        self.left = None
        self.right = None
        self.value = obj

    def insert(self, obj: Student, key:str):
        value = getattr(obj, key)
        if self.value:
            if value < getattr(self.value, key):
                if self.left is None:
                    self.left = Tree(obj)
                else:
                    self.left.insert(obj, key)
            elif value > getattr(self.value, key):
                if self.right is None:
                    self.right = Tree(obj)
                else:
                    self.right.insert(obj, key)
        else:
            self.value = obj

    def find_value(self, value:str|int, key:str):
        if value < getattr(self.value, key):
            if self.left is None:
                return None
            return self.left.find_value(value, key)
        elif value > getattr(self.value, key):
            if self.right is None:
                return None
            return self.right.find_value(value, key)
        else:
            return self.value
