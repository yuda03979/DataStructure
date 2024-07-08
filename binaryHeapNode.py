
class BinaryHeapNode:

    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __lt__(self, other):
        return True if self.key < other.key else False

    def __le__(self, other):
        return True if self.key <= other.key else False

    def __eq__(self, other):
        return True if self.key == other.key else False

    def __ge__(self, other):
        return True if self.key >= other.key else False

    def __gt__(self, other):
        return True if self.key > other.key else Fals