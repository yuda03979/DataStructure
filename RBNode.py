from enum import Enum

class RBNode:

    def __init__(self, key: int, data, sentry):
        self.key = key
        self.data = data
        self.color = Color.RED
        self.size = 1

        self.left = sentry
        self.right = sentry
        self.parent = None


    def exchange_key_data(self, node):
        """

        :param node:
        :return:
        """
        node.key, node.data, node.size, self.key, self.data, self.size = self.key, self.data, self.size, node.key, node.data, node.size


    def isSentry(self):
        return False


    def __repr__(self):
        return f'{self.key}, {self.size} ' + str(self.color)[6:]

    def __lt__(self, other):
        if isinstance(other, RBNode):
            return True if self.key < other.key else False

    def __le__(self, other):
        if isinstance(other, RBNode):
            return True if self.key <= other.key else False

    def __eq__(self, other):
        if isinstance(other, RBNode):
            return True if self.key == other.key else False

    def __ge__(self, other):
        if isinstance(other, RBNode):
            return True if self.key >= other.key else False

    def __gt__(self, other):
        if isinstance(other, RBNode):
            return True if self.key > other.key else False


class Sentry():
    def __init__(self):
        self.key = "."
        self.parent = self
        self.left = self
        self.right = self
        self.color = Color.BLACK
        self.size = 1

    def isSentry(self):
        return True



class Color(Enum):
    RED = 0
    BLACK = 1
