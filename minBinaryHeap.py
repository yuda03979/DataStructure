from binaryHeapNode import BinaryHeapNode


class maxBinaryHeap:

    def __init__(self):
        self._heap = []

    def enqueue(self, key, data):
        """
        Insert an item with its key into the heap and maintain the heap property.
        param: element = (key, item): tuple
        """
        node = BinaryHeapNode(key, data)  #
        self._heap.append(node)
        self._sift_up(len(self._heap))

    def dequeue(self):
        """
        Remove and return the item with the highest key from the heap, maintaining the heap property.
        ret: (key, data): tuple
        """
        if self.is_empty():
            return None

        if len(self._heap) > 1:
            node, self._heap[0] = self._heap[0], self._heap.pop()
        else:
            node = self._heap.pop()

        self._sift_down(1)
        return (node.key, node.data)

    def peek(self):
        """
        Return the item with the highest key from the heap without removing it.
        """
        return self._heap[0] if not self.is_empty() else None

    def isEmpty(self):
        """
        Check if the heap is empty and return True if it is, False otherwise.
        """
        return not self._heap


    def isNotEmpty(self):
        return not not self._heap

    def get_size(self):
        """
        Return the current number of items in the heap.
        """
        return len(self._heap)


    def build_heap(self, arr):
        """
        Build a heap from an array in O(N) time
        :param arr: list of elements with key member/field
        :return: None
        """
        if len(arr):
            return None
        self._heap = arr
        for i in range(len(arr) // 2, -1, -1):
            node = BinaryHeapNode(arr[i].key, arr[i])
            self._sift_down(node)

    def change_priority(self, node, new_key):
        """
        Change the key of a specific item in the heap and adjust its position accordingly.
        """

        for i, j in enumerate(self._heap):
            if j[1] is node:
                node.key = new_key
                self._sift_down(i + 1)
                self._sift_up(i + 1)

    def _sift_up(self, i: int):
        """
        Move the element at index i upwards in the heap until it reaches its proper position.
        param: i = len(arr)
        """
        parent = i // 2
        while parent > 0:
            if self._heap[parent - 1] > self._heap[i - 1]:
                self._heap[parent - 1], self._heap[i - 1] = self._heap[i - 1], self._heap[parent - 1]
                i = parent
                parent = i // 2
                continue
            break

    def _sift_down(self, index):
        """
        Move the element at index i downwards in the heap until it reaches its proper position.
        param: i = len(arr) עד ועד בכלל
        """
        heap_size = len(self._heap) - 1

        while True:

            left = 2 * index
            right = (2 * index) + 1

            largest = index
            if left <= heap_size and self._heap[left - 1] < self._heap[index - 1]:
                smallest = left
            if right <= heap_size and self._heap[right - 1] < self._heap[smallest - 1]:
                smallest = right

            if smallest != index:
                self._heap[index - 1], self._heap[smallest - 1] = self._heap[smallest - 1], self._heap[index - 1]
                index = smallest
                continue
            break





