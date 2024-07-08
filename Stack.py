class Stack:

    def __init__(self) -> None:
        self._arr = []

    def push(self, element):
        self._arr.append(element)

    def pop(self):
        try:
            return self._arr.pop()
        except IndexError:
            return None

    def top(self):
        try:
            return self._arr[-1]
        except IndexError:
            return None

    def isNotEmpty(self):
        if len(self._arr):
            return True
        return False

    def isEmpty(self):
        return not self.isNotEmpty()