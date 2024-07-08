

class BinomialHeap:
    def __init__(self):
        self.size = 0
        self.min = None # its the index of the smallest value
        self.binomial_heap = [[None, None, None]]

    def buildHeap(self, array:list):
        for i in array:
            self.enqueue(i)

    def enqueue(self, key, data):
        self.size += 1
        node = BinomialHeapNode(key, data)
        self.correct_heap_degree(0, node)
        self.define_min()


    def dequeue(self):
        if self.size == 1:
            self.size -= 1
            self.min = None
            return self.binomial_heap[0][0]

        if self.size == 0:
            raise Exception("Heap is empty")

        self.size -= 1
        min = self.binomial_heap[self.min][0]
        heap2 = self.linked_list_to_array_from_root(min)
        self.merge(heap2)
        self.define_min()
        return min

    def peek(self):
        return self.binomial_heap[min][0]

    def increase_key(self, key):
        pass

    def decrease_key(self, key):
        pass

    def merge(self, heap2):
        k = 0
        for i in range(len(heap2.binomial_heap)):
            k = 0 if self.binomial_heap[i][0] == None else 1
            # if degree i in the destination heap is None, just put it. else insert on index 1.
            self.binomial_heap[i][k] = heap2.binomial_heap[i][0]
        for i in len(self.binomial_heap): # need to check if its O(lg(n) ** 2)
            self.correct_heap_degree(i)

        self.define_min()
        # need to handeling the size. since in my case the size dont change, i didnt handle it


# private:

    def define_min(self):
        min = float('inf')
        for i in range(len(self.binomial_heap)):
            if self.binomial_heap[i][0].get_key() < min:
                min = self.binomial_heap[i][0].get_key()
                self.min = i


    def linked_list_to_array_from_root(self, node:BinomialHeapNode):

        node = node.get_left_child()
        if node == None:
            linked_list_array = [[None, None, None]]
        else:
            # initialize the array of heap2
            linked_list_array = [[None, None, None] for i in range(node.get_rightest_child().get_degree())] # assuming the rightest child has the bigest degree

            while node.get_right_sibling() is not None:
                linked_list_array[node.get_degree()][0] = node
                node = node.get_right_sibling()
            linked_list_array[node.get_rightest_child().get_degree()][0] = [node, None, None] # adding the last node

        heap2 = BinomialHeap()
        heap2.binomial_heap = linked_list_array
        return heap2


    def correct_heap_degree(self, i, node=None):

        if len(self.binomial_heap) <= i: # because if we are merging two roots they move to the next i
            self.binomial_heap.append([node, None, None])

        for j in range(3):
            # putting the new node in his place. theres must be maximum 2 nodes, and their alwise in the beginning.
            if self.binomial_heap[i][j] == None:
                self.binomial_heap[i][j] = node

        if self.binomial_heap[i][1] != None:
            # taking care in case that their 2 nodes with th same degree
            if self.binomial_heap[i][0].get_key() > self.binomial_heap[i][1].get_key():
                self.binomial_heap[i][0].set_rightest_child(self.binomial_heap[i][1])
            else:
                self.binomial_heap[i][1].set_rightest_child(self.binomial_heap[i][0])
                self.binomial_heap[i][0] = self.binomial_heap[i][1]
            new_node = self.binomial_heap[i][0]
            self.binomial_heap[i][0] = None
            self.binomial_heap[i][1] = None
            self.correct_heap_degree(i + 1, new_node)

            if self.binomial_heap[i][2] != None:
                # taking care in case that their 3 nodes with th same degree
                new_node2 = self.binomial_heap[i][2]
                self.binomial_heap[i][2] = None
                self.correct_heap_degree(i + 1, new_node2)







class BinomialHeapNode:

    def __init__(self, key, data, left_child=None, right_sibling=None):
        self.key = key
        self.data = data
        self.left_child = None
        self.right_sibling = None


    def set_left_child(self, node):
        self.left_child = node


    def set_right_sibling(self, node):
        self.right_sibling = node


    def set_rightest_child(self, new_node):
        print(new_node)
        node = self.get_left_child()
        if node is None:
            self.set_left_child(new_node)
            return
        while node.get_right_sibling() is not None:
            node = node.get_right_sibling()
        node.set_right_sibling(new_node)


    def get_left_child(self):
        return self.left_child


    def get_right_sibling(self):
        print("helloo")
        return self.right_sibling


    def get_key(self):
        return self.key


    def get_rightest_child(self):
        node = self.get_left_child()
        while node.get_right_sibling() is not None:
            node = node.get_right_sibling()
        return node


    def get_degree(self):
        degree = 0
        node = self
        while node.get_left_child() != None:
            node = node.get_left_child()
            degree += 1
        return degree


    def __lt__(self, other):
        return True if self.key < other.key else False

    def __le__(self, other):
        return True if self.key <= other.key else False

    def __eq__(self, other):
        return True if self.key == other.key else False

    def __ge__(self, other):
        return True if self.key >= other.key else False

    def __gt__(self, other):
        return True if self.key > other.key else False

